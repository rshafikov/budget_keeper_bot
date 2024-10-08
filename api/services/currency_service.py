from fastapi import Depends

from api.schemas.currency_schemas import CurrencyDB
from api.services.base_service import BaseService
from api.utils.uow import IUnitOfWork, UnitOfWork


class CurrencyService(BaseService):
    manager_name = 'currency'
    default_result_schema = CurrencyDB


async def get_currency_service(
        uow: IUnitOfWork = Depends(UnitOfWork)
) -> CurrencyService:
    return CurrencyService(uow)
