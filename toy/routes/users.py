from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")

# 문제 작성 /users/quesiton_write
@router.post("/quesiton_write", response_class=HTMLResponse) # 펑션 호출 방식
async def gyoungha(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="users/gyoungha.html", context={'request':request})

@router.get("/quesiton_write", response_class=HTMLResponse) # 펑션 호출 방식
async def gyoungha(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="users/gyoungha.html", context={'request':request})



from databases.connections import Database
from models.users import User
collection_user = Database(User)
from beanie import PydanticObjectId
# 문제 나열 문제풀기
@router.get("/solve")
async def youngji(request:Request):
    print(dict(request._query_params))
    user = await collection_user.get()
    return templates.TemplateResponse(name="users/reads.html"
                                      , context={'request':request
                                                 , 'user':user})

@router.post("/insert") # 펑션 호출 방식
async def youngji_post(request:Request):
    user_dict = await request.form()
    print(user_dict)
    return templates.TemplateResponse(name="users/youngji.html", context={'request':request})


