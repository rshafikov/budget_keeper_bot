from fastapi import APIRouter, Depends, HTTPException, status

from api.endpoints.auth import rbac
from api.schemas.user_schemas import (Role, UserBase, UserCreate, UserSecure,
                                      UserUpdate)
from api.utils.dependencies import CurrentUserDeps, UserServiceDeps

user_router = APIRouter()


@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
        new_user: UserCreate,
        user_service: UserServiceDeps
) -> UserBase:
    db_user = await user_service.get_user(telegram_id=new_user.telegram_id)

    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")

    return await user_service.add_user(new_user)


@user_router.get("/", dependencies=[Depends(rbac({Role.ADMIN}))])
async def get_users(
    user_service: UserServiceDeps,
    offset: int = 0,
    limit: int = 100
) -> list[UserBase]:
    return await user_service.get_instances(offset=offset, limit=limit)


@user_router.get("/{tg_id}/", dependencies=[Depends(rbac({Role.ADMIN}))])
async def get_user(tg_id: str, user_service: UserServiceDeps) -> UserBase:
    return await user_service.get_user_or_404(telegram_id=tg_id)


@user_router.get("/me", response_model=UserSecure)
async def user_profile(user: CurrentUserDeps):
    return user


@user_router.put("/me", response_model=UserSecure)
async def update_user(
        user: CurrentUserDeps,
        user_service: UserServiceDeps,
        new_user_data: UserUpdate
):
    return await user_service.update_instance(
        instance_id=user.id,
        data=new_user_data.model_dump(exclude_unset=True)
    )
