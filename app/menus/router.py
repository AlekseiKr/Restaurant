from fastapi import APIRouter, Body
from typing import List
from app.menus.dao import MenusDAO
from app.menus.schemas import SMenu
from app.submenus.router import submenu_router


menu_router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menus"]
)
menu_router.include_router(submenu_router)

@menu_router.get("", status_code=200, response_model=List[SMenu])
async def get_menus():

    return await MenusDAO.find_all()


@menu_router.get("/{api_test_menu_id}", status_code=200)
async def get_menu(menu_id: int) -> SMenu:

    return await MenusDAO.find_one_by_id(model_id=menu_id)

@menu_router.post("", status_code=201)
async def add_menu(data=Body()):

    return await MenusDAO.add(data)

@menu_router.delete("/{api_test_menu_id}", status_code=204)
async def delete_menu(menu_id: int):

    return await MenusDAO.delete_by_model_id(model_id=menu_id)

@menu_router.patch("/{api_test_menu_id}", status_code=200)
async def update_menu(menu_id: int, data=Body()):

    return await MenusDAO.update(menu_id, data)


