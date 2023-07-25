from fastapi import FastAPI
from app.menus.router import menu_router


app = FastAPI(
    title="Homework 1"
)

app.include_router(menu_router)



