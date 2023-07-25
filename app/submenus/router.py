from typing import List, Dict
from fastapi import APIRouter, Body
from app.submenus.dao import SubmenusDAO
from app.dishes.dao import DishesDAO
from app.submenus.schemas import SSubmenu
from app.dishes.router import dish_router


submenu_router = APIRouter(
    prefix="/{api_test_menu_id}/submenus",
    tags=["Submenus"]
)

submenu_router.include_router(dish_router)


@submenu_router.get("", status_code=200)
async def get_submenus() -> List[SSubmenu]:

    return await SubmenusDAO.find_all()

@submenu_router.get("/{api_test_submenu_id}", status_code=200)
async def get_submenu(submenu_id: int) -> SSubmenu:

    return await SubmenusDAO.find_one_by_id(model_id=submenu_id)

@submenu_router.post("", status_code=201)
async def add_submenu(data=Body()):

    return await SubmenusDAO.add(data)

@submenu_router.delete("/{api_test_submenu_id}", status_code=204)
async def delete_submenu(submenu_id: int):

    return await SubmenusDAO.delete_by_model_id(model_id=submenu_id)

@submenu_router.patch("/{api_test_submenu_id}", status_code=200)
async def update_submenu(submenu_id: int, data=Body()):

    return await SubmenusDAO.update(submenu_id, data)






