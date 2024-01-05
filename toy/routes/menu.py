from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")

@router.get("/youngji", response_class=HTMLResponse)
async def youngji(request:Request):
    return templates.TemplateResponse(name="users/youngji.html", context={'request':request})

@router.get("/gyungha")
async def gyoungha(request:Request):
    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request})

@router.get("/dongchul", response_class=HTMLResponse)
async def dongchul(request:Request):
    return templates.TemplateResponse(name="users/dongchul.html", context={'request':request})
