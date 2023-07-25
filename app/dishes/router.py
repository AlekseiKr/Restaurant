from typing import List, Dict
from fastapi import APIRouter, Body
from app.dishes.dao import DishesDAO
from app.dishes.schemas import SDish


dish_router = APIRouter(
    prefix="/{api_test_submenu_id}/dishes",
    tags=["Dishes"]
)


@dish_router.get("", status_code=200)
async def get_dishes() -> List[SDish]:

    return await DishesDAO.find_all()


@dish_router.get("/{api_test_dish_id}", status_code=200)
async def get_dish(dish_id: int) -> SDish:

    return await DishesDAO.find_one_by_id(model_id=dish_id)

@dish_router.post("", status_code=201)
async def add_dish(data=Body()):

    return await DishesDAO.add(data)

@dish_router.delete("/{api_test_dish_id}", status_code=204)
async def delete_dish(dish_id: int):

    return await DishesDAO.delete_by_model_id(model_id=dish_id)

@dish_router.patch("/{api_test_dish_id}", status_code=200)
async def update_dish(dish_id: int, data=Body()):

    return await DishesDAO.update(dish_id, data)






