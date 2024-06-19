# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 路由聚合
"""
from api.Base import apiRouter
from views.Base import viewRouter
from fastapi import APIRouter


allRouter = APIRouter()
# 视图路由
allRouter.include_router(viewRouter)
# API路由
allRouter.include_router(apiRouter)
