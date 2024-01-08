from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한
class User(Document):
    question: Optional[str] = None
    choice1: Optional[EmailStr] = None
    choice2: Optional[EmailStr] = None
    choice3: Optional[EmailStr] = None
    choice4: Optional[EmailStr] = None
    answer: Optional[str] = None
    score: Optional[str] = None
    
    class Settings:
        name = "questions_write"

    name: Optional[str] = None
    useranswer1: Optional[int] = None
    useranswer2: Optional[int] = None
    useranswer3: Optional[int] = None
    useranswer4: Optional[int] = None
    useranswer5: Optional[int] = None
  
    class Settings:
        name = "user"
  