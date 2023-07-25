from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String)
    price = Column(Float, nullable=False)
    submenu_id = Column(Integer, ForeignKey("submenus.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    submenu = relationship("Submenu", back_populates="dishes")





