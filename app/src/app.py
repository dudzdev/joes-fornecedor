import random
import time

from gspread.exceptions import APIError
from pydantic import ValidationError

from src.google.services import GoogleSheetsService
from src.models import Product
from src.pdf.services import PDFService


if __name__ == '__main__':
    pdf_pmg_file_location = "F:\\trampos\\Joes\\fornecedores\\pmg\\GERAL_0.pdf"
    pdf_service = PDFService(pdf_pmg_file_location)
    tables = pdf_service.read_tables(pages="all")
    table_count = 0
    products = []
    errors = []

    for table in tables:

        if table_count > 0: # Desconsidera somente o primeiro header
            columns = table.columns

            product = {
                "cod": str(columns[0]),
                "name": str(columns[1]),
                "unit": str(columns[2]),
                "price": str(columns[3]).replace("R$", "").replace(",", ".").strip()
            }

            try:
                products.append(Product(**product))
            except ValidationError as e:
                errors.append(product)

        for index, row in table.iterrows():

            product = {
                "cod": str(row[0]),
                "name": str(row[1]),
                "unit": str(row[2]),
                "price": str(row[3]).replace("R$", "").replace(",", ".").strip()
            }

            try:
                products.append(Product(**product))
            except ValidationError as e:
                errors.append(product)

        table_count += 1

    google_sheet_service = GoogleSheetsService()

    worksheet = google_sheet_service.get_worksheet(
        title="Base de Fornecedores",
        folder_id="1WbdlvsFusX7x3zBsNx8KSDGD0Z-m8n2C"
    )

    worksheet_head = [
        "Codigo",
        "Nome",
        "Unidade",
        "Preço"
    ]

    google_sheet_service.append_row(worksheet, worksheet_head)

    flag_completed = True

    for product in products:

        attempt = 0
        attempt_max = 10
        maximum_backoff = 64

        while attempt < attempt_max:
            try:

                google_sheet_service.append_row(worksheet, [
                    product.get_cod(),
                    product.get_name(),
                    product.get_unit(),
                    '${:,.2f}'.format(product.get_price())
                ])
                print(f"added success - {product}")
                break

            except APIError as e:
                attempt += 1
                jitter = random.randint(0, 1000) / 1000  # de 0 até 1 segundo
                wait = min((2 ** attempt) + jitter, maximum_backoff)
                print(f"attempt {attempt} fail: {e}")
                print(f"waiting {wait:.2f} seconds before next attempt...\n")
                time.sleep(wait)

        if attempt == 10:
            flag_completed = False
            break

    print("insert completed!!") if flag_completed else print("attempt max exceeded")
    print(f"errors: {len(errors)}")
    print(f"total products: {len(products)}")
    print(errors)

