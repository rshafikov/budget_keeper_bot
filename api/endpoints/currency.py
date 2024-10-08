from fastapi import APIRouter, Depends, HTTPException, status

from api.endpoints.auth import rbac
from api.schemas.currency_schemas import CurrencyBase
from api.schemas.user_schemas import Role
from api.services.currency_service import CurrencyService, get_currency_service

currency_router = APIRouter()


@currency_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(rbac({Role.ADMIN}))],
)
async def create_currency(
        currency: CurrencyBase,
        currency_service: CurrencyService = Depends(get_currency_service),
) -> CurrencyBase:
    cur = await currency_service.get_instance(name=currency.name)

    if cur:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'This currency {currency.name} already exists.'
        )

    return await currency_service.create_instance(currency)


@currency_router.get(
    "/{currency_name}/",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(rbac({Role.USER}))],
)
async def get_currency(
        currency_name: str,
        currency_service: CurrencyService = Depends(get_currency_service)
) -> CurrencyBase:
    return await currency_service.get_instance_or_404(name=currency_name)
