from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

from toy.databases.connections import Database

# from toy.models.choices import choices
# collection_choice = Database(choices)

from toy.models.users import user
collection_user = Database(user)

from toy.models.problems import problem
collection_problem = Database(problem)

router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")

@router.get("/youngji", response_class=HTMLResponse)
async def youngji(request:Request):
    problem_list = await collection_problem.get_all()
    useranswer_list = await collection_user.get_all()

    return templates.TemplateResponse(name="users/youngji.html", context={'request':request
                                                                          , 'useranswer':useranswer_list
                                                                          , 'problems': problem_list})



@router.get("/youngji2", response_class=HTMLResponse)
async def youngji2(request:Request):
    problem_list = await collection_problem.get_all()
    print(problem_list)
    
    return templates.TemplateResponse(name="users/youngji_2.html"
                                          , context={'request':request
                                                     , 'problems': problem_list})


    # return templates.TemplateResponse(name="users/youngji_2.html"
    #                                   , context={'request':request
    #                                              , 'problem':problem
    #                                              , 'choices':choice})


@router.get("/gyungha")
async def gyoungha(request:Request):
    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request})

@router.get("/dongchul", response_class=HTMLResponse)
async def dongchul(request:Request):
    return templates.TemplateResponse(name="users/dongchul.html", context={'request':request})
