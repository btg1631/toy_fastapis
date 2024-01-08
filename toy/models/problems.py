from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한
class Problem(Document):
    question: Optional[str] = None
    answer: Optional[str] = None
    score: Optional[str] = None
  
    class Settings:
        name = "problems"
  