from typing import Optional
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from nutritionist.models import User
from nutritionist.repositories import (
    MealEntryRepository,
    ReportRepository,
    UserRepository,
    WeightHistoryRepository
)


class ReportTool(BaseTool):
    name: str = "report_tool"
    description: str = (
        "Use esta ferramenta para gerar um relatório para um usuário. "
        "Entrada: data para a qual o relatório é solicitado (opcional) no formato ISO para ser usada na função datetime.fromisoformat."
    )

    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        self._meal_entry_repo = MealEntryRepository()
        self._weight_history_repo = WeightHistoryRepository()
        self._report_repo = ReportRepository()

    def _run(self, telegram_id: int, report_date: str) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if not user:
                return "Usuário não encontrado. Por favor, registre-se primeiro."

            meal_entries = self._meal_entry_repo.get_meal_entry_by_id(telegram_id)
            weight_history = self._weight_history_repo.get_weight_history(telegram_id)

            report_content = self._generate_report_content(user, meal_entries, weight_history, report_date)

            self._report_repo.create_report(user.telegram_id, report_content)

            return f"Relatório gerado com sucesso para {user.name}:\n{report_content}"
        except Exception as e:
            return f"Erro na ferramenta de relatório: {str(e)}"

    def _generate_report_content(self, user: User, meal_entries: list, weight_history: list, date: str) -> str:
        instructions = f'''
        Objetivo: Gerar um relatório de hábitos alimentares e histórico de peso do usuário filtrado por uma data específica.

        Instruções: Você é um agente que gera relatórios personalizados com base em dados do usuário. 
        O usuário vai fornecer os dados e uma data, e você deve gerar um relatório contendo as informações relevantes de refeições e histórico de peso somente para essa data. 
        Se não houver dados para a data especificada, o relatório deve informar que não foram encontradas informações.
        
        Dados do usuario
        {user.model_dump_json()}
        
        Dados de alimentação
        {meal_entries}
        
        Dados de peso
        {weight_history}
        
        Data de corte
        {date}
        
        '''
        llm = ChatOpenAI(model='gpt-4o-mini')
        response = llm.invoke(instructions)
        return response.content


    async def _arun(self, telegram_id: str, report_date: Optional[str] = None) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")
