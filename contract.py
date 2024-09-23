from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProductEnum(str, Enum):
    GEMINI = "GEMINI"
    CHATGPT = "CHATGPT"
    LLAMA3 = "LLAMA3"

class Sales(BaseModel):
    email: EmailStr
    date: datetime
    hour: datetime
    value: PositiveFloat
    quantity: PositiveInt
    product: str