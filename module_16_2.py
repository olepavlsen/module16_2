from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_page_adm() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_nmb(user_id: int = Path(ge=1, le=100, description="EEnter User ID", example="1")) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def get_user_inf(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
                       , age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}