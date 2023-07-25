from typing import Optional

from pydantic import BaseModel

class SSubmenu(BaseModel):

    id: int
    title: str
    description: str
    menu_id: int
    dishes_count: Optional[int]

    class Config:
        from_attributes = True
