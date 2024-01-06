from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한
class Choice(Document):
    problem_id: Optional[str] = None
    choices1: Optional[str] = None
    choices2: Optional[str] = None
    choices3: Optional[str] = None
    choices4 : Optional[str] = None
  
    class Settings:
        name = "choices"
  