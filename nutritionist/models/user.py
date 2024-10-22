from pydantic import BaseModel, Field

class User(BaseModel):
    telegram_id: int = Field(..., description="O ID do usuário no Telegram.")
    name: str = Field(..., description="O nome completo do usuário.")
    sex: str = Field(..., description="O sexo do usuário. Exemplo: 'M' para masculino, 'F' para feminino.")
    age: str = Field(..., description="A idade do usuário. Exemplo: '25 anos'.")
    height_cm: str = Field(..., description="A altura do usuário em centímetros. Exemplo: '180 cm'.")
    weight_kg: str = Field(..., description="O peso do usuário em quilogramas. Exemplo: '70 kg'.")
    has_diabetes: str = Field(..., description="Indica se o usuário tem diabetes. Exemplo: 'sim' ou 'não'.")
    goal: str = Field(..., description="O objetivo do usuário com a IA nutricionista. Exemplo: 'perder peso', 'ganhar massa muscular'.")
