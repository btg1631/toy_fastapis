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

from models.problems import Problem
from models.choices import Choice
from models.users import User
collection_problem = Database(Problem)
collection_choice = Database(Choice)
collection_user = Database(User)
from beanie import PydanticObjectId
# 문제 나열 문제풀기
@router.get("/solve")
async def youngji(request:Request):
    print(dict(request._query_params))
    problem = await collection_problem.get_all()
    choice = await collection_choice.get_all()
    
    # problem_id를 이용해서 choice를 불러오는 코드가 필요함
     
    return templates.TemplateResponse(name="users/reads.html"
                                      , context={'request':request
                                                 , 'problem':problem
                                                 , 'choice':choice})
# 문제 풀이 저장(응시자 이름/정답)
@router.post("/insert") # 펑션 호출 방식
async def youngji_post(request:Request):
    user_dict = await request.form()
    print(user_dict)
    # 저장    
    # user = User(**user_dict)
    # await collection_user.save(user)
    # # 리스트 정보
    # user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="users/youngji.html", context={'request':request})

    # return templates.TemplateResponse(name="users/youngji.html", context={'request':request, 'users':user_list})


