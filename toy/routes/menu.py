from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")

@router.get("/youngji", response_class=HTMLResponse)
async def youngji(request:Request):
    return templates.TemplateResponse(name="users/youngji.html", context={'request':request})

from databases.connections import Database
from models.users import User
collection_user = Database(User)
@router.get("/gyungha")
async def gyoungha(request:Request):
    print(dict(request._query_params))
    user_list = await collection_user.get_all()

    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request, 'user' :user_list})

@router.get("/dongchul", response_class=HTMLResponse)
async def dongchul(request:Request):
    return templates.TemplateResponse(name="users/dongchul.html", context={'request':request})
