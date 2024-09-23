from datetime import datetime, time, date
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProductEnum(str, Enum):
    GEMINI = "GEMINI"
    CHATGPT = "CHATGPT"
    LLAMA3 = "LLAMA3"

class Sales(BaseModel):
    email: EmailStr
    date: date
    hour: time
    value: PositiveFloat
    quantity: PositiveInt
    product: str