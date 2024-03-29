from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한

class user(Document):
    name: Optional[str] = None
    problem1: Optional[int] = None
    problem2: Optional[int] = None
    problem3: Optional[int] = None
    problem4: Optional[int] = None
    problem5: Optional[int] = None
  
    class Settings:
        name = "user"
  