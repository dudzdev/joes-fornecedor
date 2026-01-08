from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_groq import ChatGroq
from langgraph_sdk import get_sync_client

from src import config
from src.agent.tools import confirmar_inscricao_comunidade


class Elvis:

    system_prompt = """
    Você é um assistente de criação de lista de compras da Joes Burger.
    Joes Burger é uma hamburgueria com sede na cidade de Caieiras.
    """

    def __init__(self):
        model = ChatGroq(
            temperature=0.3,
            model="llama-3.3-70b-versatile",
            api_key=config.LLM_KEY
        )

        self.agent = create_agent(
            model=model,
            tools=[confirmar_inscricao_comunidade],
            system_prompt=self.system_prompt,
            middleware=[
                SummarizationMiddleware(
                    model=model,
                    max_tokens_before_summary=1000,
                    messages_to_keep=5
                )
            ]
        )


def get():
    return Elvis().agent


if __name__ == '__main__':
    elvis = Elvis()
    for chunk in elvis.agent.stream(
            {"messages": [{"role": "user", "content": "Como faço para criar uma lista de compras?"}]},
            stream_mode="updates",
    ):
        for key in chunk.keys():
            if not chunk[key]:
                continue
            if 'messages' in chunk[key]:
                for message in chunk[key]['messages']:
                    message.pretty_print()
        # print(chunk.data) # Uncomment to see full data
