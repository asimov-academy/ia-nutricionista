from langchain.tools import BaseTool
from typing import Any, Dict, Optional
from nutritionist.repositories import MealEntryRepository, UserRepository


class MealEntryTool(BaseTool):
    name: str = "meal_entry"
    description: str = (
        "Ferramenta para toda vez que o usuario quiser que você registre uma refeição que ele fez no dia"
        "se você nao tiver todos os dados para registrar uma refeição, pergunte a ao usuario até que tenha todas as informações necessarias"
        "Use esta ferramenta para registrar uma refeição de um usuário. "
        "Entrada: um dicionario com detalhes da refeição, como meal_description, calories, carbs, proteins, fats."
        "Você deve se basear nas informações que o usuario passou para gerar as informações de calories, carbs, proteins, fats"
    )

    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        self._meal_entry_repo = MealEntryRepository()

    def _run(
        self, 
        telegram_id: int,
        meal_description: str,
        image_path: Optional[str] = None,
        calories: Optional[str] = None,
        carbs: Optional[str] = None,
        proteins: Optional[str] = None,
        fats: Optional[str] = None,
        ) -> str:
        try:
            # user = self._user_repo.get_user_by_telegram_id(self._telegram_id)
            # if not user:
            #     return "Usuário não encontrado. Por favor, registre-se primeiro."

            self._meal_entry_repo.create_meal_entry(
                user_id=telegram_id,
                image_path=image_path,
                calories=calories,
                carbs=carbs,
                fats=fats,
                meal_description=meal_description,
                proteins=proteins,
            )
            return f"Refeição registrada com sucesso para user.name."
        except Exception as e:
            return f"Erro no registro de refeição: {str(e)}"

    async def _arun(self, telegram_id: str, meal_data: Dict[str, Any]) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")
