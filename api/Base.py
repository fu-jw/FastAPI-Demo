# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 基本路由
"""
from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def index():
    return "R U OK"
