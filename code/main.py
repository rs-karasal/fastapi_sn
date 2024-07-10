from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from code.auth.auth import auth_backend
from code.auth.database import User
from code.auth.manager import get_user_manager
from code.auth.schemas import UserRead, UserCreate


main_app = FastAPI(
    title="Social Network",
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


main_app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

main_app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


current_user = fastapi_users.current_user()


@main_app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"
