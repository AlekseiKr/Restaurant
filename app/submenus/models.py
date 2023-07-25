from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    dishes_count = Column(Integer)
    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu", cascade="save-update, merge, delete", passive_deletes=True)





