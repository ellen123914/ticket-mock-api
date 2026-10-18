# -*- coding: utf-8 -*-
"""
工单 Mock 数据仓库
按"手机号码 -> 工单"的映射存储，一个号码对应一张工单（与需求约定一致）。
需要新增 demo 数据，直接往 TICKET_DB 里加一行即可。
"""

TICKET_DB = {
    # 手机号         工单编号           状态     姓名   地址                                      产品型号
    "13800138000": {
        "ticket_no": "GD202610180001",
        "ticket_status": "处理中",
        "customer_name": "张伟",
        "phone": "13800138000",
        "address": "广东省深圳市南山区科技园南区A栋1203",
        "product_model": "智能客服机器人 标准版 KZ-2026",
    },
    "13900139000": {
        "ticket_no": "GD202610150008",
        "ticket_status": "待处理",
        "customer_name": "李娜",
        "phone": "13900139000",
        "address": "广东省深圳市福田区车公庙天安数码城B座1802",
        "product_model": "智能客服机器人 专业版 KZ-2026-Pro",
    },
    "13700137000": {
        "ticket_no": "GD202610120015",
        "ticket_status": "已完成",
        "customer_name": "王强",
        "phone": "13700137000",
        "address": "广东省深圳市龙岗区坂田街道五和大道2101号",
        "product_model": "智能外呼一体机 IHC-100",
    },
    "13600136000": {
        "ticket_no": "GD202610090022",
        "ticket_status": "已关闭",
        "customer_name": "陈静",
        "phone": "13600136000",
        "address": "广东省深圳市宝安区新安街道创业一路1088号",
        "product_model": "智能客服机器人 旗舰版 KZ-2026-Max",
    },
    "13500135000": {
        "ticket_no": "GD202610160030",
        "ticket_status": "处理中",
        "customer_name": "刘洋",
        "phone": "13500135000",
        "address": "广东省深圳市罗湖区东门中路2002号",
        "product_model": "智能语音导航系统 IVN-500",
    },
}
#（注：内容由AI生成）
