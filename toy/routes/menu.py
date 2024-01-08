from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

from toy.databases.connections import Database

from toy.models.users import user
collection_user = Database(user)

from toy.models.problems import problems
collection_problem = Database(problems)

from toy.models.choices import choices
collection_choice = Database(choices)

router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")

@router.get("/youngji", response_class=HTMLResponse)
async def youngji(request:Request):
    problem_list = await collection_problem.get_all()
    useranswer_list = await collection_user.get_all()

    return templates.TemplateResponse(name="users/youngji.html", context={'request':request
                                                                          , 'useranswer':useranswer_list
                                                                          , 'problems': problem_list})

@router.get("/gyungha", response_class=HTMLResponse) # 펑션 호출 방식
async def gyoungha(request:Request):
    request._query_params
    dict(request._query_params)
    problem_list = await collection_problem.get_all()
    choice_list = await collection_choice.get_all()


    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request, 'problems':problem_list, 'choices':choice_list})

@router.get("/dongchul", response_class=HTMLResponse)
async def dongchul(request:Request):
    return templates.TemplateResponse(name="users/dongchul.html", context={'request':request})
