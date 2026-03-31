from fastapi import APIRouter, Depends

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("", response_model=UserSchema)
def get_user():
    """
    Получение данных текущего пользователя.
    :param user: Текущий авторизованный пользователь
    :return: Данные пользователя по схеме UserSchema
    """
    return UserSchema(
        id=1,
        name='djo',

    )
