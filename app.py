# -*- coding: utf-8 -*-
"""
工单查询 Mock 接口 —— 供 Dify HTTP 请求节点调用
=================================================
运行:
    cd ticket-mock-api
    uvicorn app:app --host 0.0.0.0 --port 8000

查询:
    GET http://localhost:8000/api/ticket/query?phone=13800138000
接口文档(Swagger):
    http://localhost:8000/docs
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse

from data import TICKET_DB

app = FastAPI(
    title="工单查询 Mock 接口",
    description="按手机号查询工单信息（工单编号/状态/姓名/电话/地址/产品型号），供 Dify 接口调用节点对接。",
    version="1.0.0",
)


@app.get("/")
def health():
    """健康检查：确认服务已启动，云端 Dify 也能用这个路径探活。"""
    return {"service": "ticket-mock-api", "status": "ok"}


@app.get("/api/ticket/query")
def query_ticket(phone: str = Query(..., description="客户手机号码，如 13800138000")):
    """
    按手机号查询工单。
    - 手机号为空或格式不对 -> 400
    - 手机号有对应工单  -> code=0, 返回工单对象
    - 手机号无对应工单  -> code=1, 返回未查询到的提示
    """
    # 参数校验：11 位纯数字
    if not phone or not (phone.isdigit() and len(phone) == 11):
        raise HTTPException(
            status_code=400,
            detail="手机号格式不正确，请输入 11 位数字手机号",
        )

    ticket = TICKET_DB.get(phone)
    if ticket is None:
        return JSONResponse(
            status_code=200,
            content={
                "code": 1,
                "message": f"未查询到手机号 {phone} 对应的工单",
                "data": None,
            },
        )

    return JSONResponse(
        status_code=200,
        content={
            "code": 0,
            "message": "success",
            "data": ticket,
        },
    )
#（注：内容由AI生成）
