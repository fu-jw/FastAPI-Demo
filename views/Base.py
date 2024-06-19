# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 视图路由
"""
from fastapi import APIRouter

viewRouter = APIRouter(tags=['视图路由'])


@viewRouter.get('/')
async def index():
    return "R U OK"
