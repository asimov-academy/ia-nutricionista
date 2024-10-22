from langchain.tools import BaseTool
from nutritionist.repositories import UserRepository, WeightHistoryRepository


class WeightUpdateTool(BaseTool):
    name: str = "weight_update"
    description: str = (
        "Use esta ferramenta para registrar o peso de um usuário. "
        "Entrada: telegram_id do usuário e weight_kg."
    )

    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        self._weight_history_repo = WeightHistoryRepository()

    def _run(self, telegram_id: int, weight_kg: float) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if not user:
                return "Usuário não encontrado. Por favor, registre-se primeiro."

            self._weight_history_repo.add_weight_entry(telegram_id, weight_kg)
            return f"Peso atualizado com sucesso para {user.name}."
        except Exception as e:
            return f"Erro na ferramenta de atualização de peso: {str(e)}"

    async def _arun(self, weight_kg: float) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")