from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한
class User(Document):
    name: Optional[str] = None
    useranswer1: Optional[str] = None
    useranswer2: Optional[str] = None
    useranswer3: Optional[str] = None
    useranswer4: Optional[str] = None
    useranswer5: Optional[str] = None
  
    class Settings:
        name = "user"
  