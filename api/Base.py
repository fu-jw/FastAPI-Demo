# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 基本路由
"""
from fastapi import APIRouter
from api.login import login

apiRouter = APIRouter(prefix="/v1", tags=["api路由"])


@apiRouter.get('/')
async def index():
    return "RUOK"


"""
上下两种路由写法：
1.Python装饰器写法，
2.路由调用法，路由和处理函数分离【推荐】
"""
apiRouter.get('/login')(login)
# apiRouter.get('/login', tags=["api路由"], summary="登录接口")(login)
