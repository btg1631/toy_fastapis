from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한
class User(Document):
    name: Optional[str] = None
    question: Optional[str] = None
    answer: Optional[str] = None
    score: Optional[str] = None
    text : Optional[str] = None
  
    class Settings:
        name = "users"
  