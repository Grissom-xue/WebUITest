# 正常场景 - 正确的用户名密码
success_data = {"user": "grissom.xue@dingtopne.me", "passwd": "123456"}

# 异常场景 - 用户名不正确
fail_data =[
    {"user": "grissom.xue", "passwd": "123456", "check": "请输入正确的邮箱"},
    {"user": "grissom.xue@dingtopne.me", "passwd": "x", "check": "请输入6-16位数字、字母或符号！"},
    {"user": "grissom.xue@dingtopne.me", "passwd": "123456", "check": "无匹配账号或者设备"}
]



