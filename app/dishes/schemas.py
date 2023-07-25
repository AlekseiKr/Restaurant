from pydantic import BaseModel

class SDish(BaseModel):

    id: int
    title: str
    description: str
    price: float
    submenu_id: int

    class Config:
        from_attributes = True
