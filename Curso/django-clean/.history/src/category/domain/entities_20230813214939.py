
from datetime import datetime
from dataclasses import dataclass

@dataclass()
class Category:

    name: str
    description: str
    is_active: bool
    created_at: datetime
