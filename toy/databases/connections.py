from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from toy.models.problems import problems
from toy.models.choices import choices
from toy.models.users import user
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                           document_models=[problems, choices, user])
    class Config:
            env_file = ".env" 


class Database:
     # model 즉 collection
    def __init__(self, model) -> None:
          self.model = model
          pass
    # 전체 리스트
    async def get_all(self) :
         documents = await self.model.find_all().to_list() # find({})
         pass
         return documents
    
    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id) # find_one()
        if doc:
            return doc
        return False
    
    
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None
     


