from datetime import datetime

from pydantic import BaseModel


class RecordBase(BaseModel):
    amount: int


class RecordCreate(RecordBase):
    pass


class Record(RecordBase):
    id: int
    user_id: int
    category_id: int
    currency_id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
