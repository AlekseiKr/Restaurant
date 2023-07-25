from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    submenus_count = Column(Integer)
    dishes_count = Column(Integer)
    submenus = relationship("Submenu", back_populates="menu", cascade="save-update, merge, delete", passive_deletes=True, lazy="dynamic")

