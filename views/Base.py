# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 视图路由
"""
from fastapi import APIRouter, Request
# from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
# from config import settings
from views.home import home, reg_page, result_page

viewRouter = APIRouter(tags=['视图路由'])


# 写法3去掉：
# templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@viewRouter.get('/')
async def index():
    return "R U OK"


@viewRouter.get('/item/{id}', response_class=HTMLResponse)
async def item(request: Request, id: str):
    # 写法1：
    # return templates.get_template("index.html").render({"request": request, "id": id})
    # 写法2：
    # return templates.TemplateResponse('index.html', {'request': request, "id": id})
    # 写法3：
    return request.app.state.views.TemplateResponse('index.html', {'request': request, 'id': id})


# 写法4：完全分离
viewRouter.get('/home/{id}', response_class=HTMLResponse)(home)
viewRouter.get("/reg", response_class=HTMLResponse)(reg_page)
viewRouter.post("/reg/form", response_class=HTMLResponse)(result_page)
