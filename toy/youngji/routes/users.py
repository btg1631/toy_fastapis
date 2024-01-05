from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="toy/youngji/templates/")

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


