from langchain_core.tools import tool


@tool(description="Confirmar criação da lista de compras")
def confirmar_inscricao_comunidade() -> str:
    return f"Sua lista de compras foi criado com sucesso! Parabéns, um importante passo pra não dar ruim no final"