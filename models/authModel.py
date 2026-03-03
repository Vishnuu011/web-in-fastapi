from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    validator
)
from typing import Optional
from enum import Enum
from datetime import datetime, timezone


class RolesEnum(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"

class User(BaseModel):
    name:str=Field(...)
    email:EmailStr=Field(...)
    password:str=Field(..., min_length=6)
    created_at:datetime=Field(default_factory=datetime.now)
    updated_at:datetime=Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            "onupdate": datetime.now(timezone.utc)
        }
    )
    role:Optional[RolesEnum]=Field(default=RolesEnum.USER)

    @field_validator('name')
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError('Name must not be empty')
        
        if len(value) <2 or len(value) > 50:
            raise ValueError(
                "Name must be between 2 and 50 characters long"
            )
        return value