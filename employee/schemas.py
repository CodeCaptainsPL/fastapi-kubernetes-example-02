import uuid
from datetime import datetime

from pydantic import BaseModel, Extra, Field, PositiveFloat, UUID4

from .utils import utcnow


class EmployeeCreatePayload(BaseModel):
    name: str
    position: str
    salary: PositiveFloat

    class Config:
        extra = Extra.forbid


class EmployeeCreated(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    position: str
    salary: float
    created_at: datetime = Field(default_factory=utcnow)
