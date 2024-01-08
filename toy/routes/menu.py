from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database

from toy.models.users import questions_write
collection_user = Database(questions_write)

router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")

@router.get("/youngji", response_class=HTMLResponse)
async def youngji(request:Request):
    return templates.TemplateResponse(name="users/youngji.html", context={'request':request})

@router.get("/youngji2", response_class=HTMLResponse)
async def youngji2(request:Request):
    return templates.TemplateResponse(name="users/youngji_2.html", context={'request':request})



@router.get("/gyungha", response_class=HTMLResponse) # 펑션 호출 방식
async def gyoungha(request:Request):
    request._query_params
    dict(request._query_params)
    user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request, 'user':user_list})

@router.get("/dongchul", response_class=HTMLResponse)
async def dongchul(request:Request):
    return templates.TemplateResponse(name="users/dongchul.html", context={'request':request})
