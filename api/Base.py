# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 基本路由
"""
from fastapi import APIRouter

apiRouter = APIRouter(prefix="/v1", tags=["api路由"])


@apiRouter.get('/')
async def index():
    return "RUOK"
