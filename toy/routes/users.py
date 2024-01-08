from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="toy/templates/")


from databases.connections import Database
from toy.models.users import user
collection_user = Database(user)


# 문제 작성 /users/quesiton_write
@router.post("/quesiton_write", response_class=HTMLResponse) # 펑션 호출 방식
async def gyoungha(request:Request):
    await request.form()
    dict(await request.form())
    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request})

@router.get("/quesiton_write", response_class=HTMLResponse) # 펑션 호출 방식
async def gyoungha(request:Request):
    await dict(request._query_params)
    user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="users/gyoungha.html", context={'request':request, 'user':user_list})



from toy.databases.connections import Database
from toy.models.problems import problems
from toy.models.choices import choices
from toy.models.users import user
collection_problem = Database(problems)
collection_choice = Database(choices)
collection_user = Database(user)

# 문제 나열 문제풀기
@router.get("/solve")
async def youngji_solve(request:Request):
    problem = await collection_problem.get_all()
    choice = await collection_choice.get_all()
    problem_choice_list = []
    for i in range(len(problem)):
        prob = problem[i]
        ch = choice[i]
        problem_choice_list.append((prob.question, ch.choices1, ch.choices2, ch.choices3, ch.choices4))

    return templates.TemplateResponse(name="users/youngji_2.html"
                                      , context={'request':request
                                                 , 'problems':problem
                                                 , 'choices':choice
                                                 , 'problem_choices':problem_choice_list})

# 문제 풀이 저장(응시자 이름/답)
@router.post("/list") # 펑션 호출 방식
async def youngji_list(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    name = user(**user_dict)
    print(name)
    await collection_user.save(name)

    problem_list = await collection_problem.get_all()
    useranswer_list = await collection_user.get_all()
    return templates.TemplateResponse(name="users/youngji.html", context={'request':request
                                                                          , 'useranswer':useranswer_list
                                                                          , 'problems': problem_list})

@router.post("/quit", response_class=HTMLResponse) # 펑션 호출 방식
async def quit(request:Request):
    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request})
@router.get("/quit", response_class=HTMLResponse) # 펑션 호출 방식
async def quit(request:Request):
    return templates.TemplateResponse(name="users/gyungha.html", context={'request':request})




