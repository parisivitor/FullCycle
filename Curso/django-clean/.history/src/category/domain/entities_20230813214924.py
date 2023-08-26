
from datetime import datetime
from dataclasses import dataclass

@dataclass()
class Category:

    nome: str
    description: str
    is_active: bool
    created_at: datetime
