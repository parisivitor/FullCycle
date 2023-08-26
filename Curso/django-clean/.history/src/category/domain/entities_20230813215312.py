
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass() #init, #repr(print), #eq(compare duas classes)
class Category:

    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = datetime.now()
