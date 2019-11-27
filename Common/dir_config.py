import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 测试数据目录
testdatas_dir = os.path.join(base_dir, "TestDatas")
# 测试case目录
testcases_dir = os.path.join(base_dir, "TestCases")
# Report 目录
htmlReport_dir = os.path.join(base_dir, "Outputs/reports")
# 日志目录
log_dir = os.path.join(base_dir, "Outputs/logs")
# 截图目录
screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")
