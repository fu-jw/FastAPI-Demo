# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: 登录路由
"""
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


# 登录测试
async def test():
    return "test successfully"


async def login(usr: User):
    return usr
