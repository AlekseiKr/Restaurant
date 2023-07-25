from typing import Optional

from pydantic import BaseModel

class SMenu(BaseModel):

    id: int
    title: str
    description: str
    submenus_count: Optional[int]
    dishes_count: Optional[int]

    class Config:
        from_attributes = True
