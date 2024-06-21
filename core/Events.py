# -*- coding:utf-8 -*-
"""
@Created on : 2024/6/18 22:02
@Author: Fredo
@Des: fastapi事件监听
"""

from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        # APP启动完成后触发
        print("启动完毕")
        # 注册数据库
        await register_mysql(app)
        print("注册DB完毕")
        pass
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def stop_app() -> None:
        # APP停止时触发
        print("停止")
        pass

    return stop_app
