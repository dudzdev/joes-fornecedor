import tabula


class PDFService:

    def __init__(self, file_name: str):
        tabula.environment_info()
        self.__file_name = file_name

    def read_tables(self, pages: str) -> list:
        return tabula.read_pdf(self.__file_name, pages=pages)
