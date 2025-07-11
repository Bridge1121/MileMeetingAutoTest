import importlib
import json
import os
import shutil
import subprocess
import time
import datetime

import pytest
import requests
import schedule

# from utils.commen import try_back_to_home

# 钉钉机器人配置
#测试群
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=93c04271a11ef58697a0af784302016ccbfec2dfc45a0dd08964c022d217efe6"
#办公本hook
# DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=9f4def1f3b64509d35397661e137ec2b463bedaffeb8840b73447fe3b61af383"


#执行生成测试报告的命令
# allure generate allure-results -o allure-allure-report-86% --clean
# allure open allure-allure-report-86%


TASK_NAME = "麦耳会记UI自动化测试"
TEAM_NAME = "测试小组"
PROJECT_NAME = "麦耳会记自动化测试项目"
DEVICE_MODEL = "麦耳会记"
URL = "V4.1.0.1"

def send_to_dingtalk(webhook_url, message):
    headers = {'Content-Type': 'application/json'}
    data = {"msgtype": "text", "text": {"content": message}}
    try:
        response = requests.post(webhook_url, headers=headers, json=data)
        if response.status_code == 200:
            print("测试结果已成功发送到钉钉。")
        else:
            print(f"发送失败，状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"发送过程中出现错误: {e}")


def count_allure_results(allure_result_dir="allure-results"):
    passed = failed = broken = 0
    for file in os.listdir(allure_result_dir):
        if file.endswith("-result.json"):
            with open(os.path.join(allure_result_dir, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status")
                if status == "passed":
                    passed += 1
                elif status == "failed":
                    failed += 1
                elif status == "broken":
                    broken += 1
    return passed, failed, broken

#测试环境和参数信息
def write_environment_properties(info: dict, results_dir="allure-results"):
    lines = [f"{k}={v}" for k, v in info.items()]
    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, "environment.properties"), "w", encoding="iso-8859-1") as f:
        f.write('\n'.join(lines))



def run_all_scripts():
    #每次运行之前都先清空一下上一次运行保存的json文件
    results_dir = "allure-results"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir, exist_ok=True)



    #测试环境信息和参数信息
    write_environment_properties({
        "project": "MilMeeting Web AutoTest",
        "url": URL,
        "device_model": "MileMeeting",
        "tester": "twx",
    })
    # write_environment_properties({
    #     "项目名称": "办公本自动化测试项目",
    #     "设备型号": "办公本Pro",
    #     "APK版本": "V2.4.0.25062601",
    #     "测试环境": "测试环境",
    #     "负责人": "twx"
    # })
    start_time = time.time()
    # todo用例执行阻塞之后的操作
    # if not try_back_to_home():
    #     print("❌ 启动前回到首页失败，终止任务")
    #     return
    # print("✅ 正在执行测试用例...")
    # 执行 pytest，生成 Allure 中间结果

    subprocess.run(["pytest", "testcases", "--alluredir=allure-results"], encoding="utf-8")

    # 生成 HTML 报告
    # subprocess.run(["allure", "generate", "./allure-results", "-o", "./allure-allure-report-86%", "--clean"])
    # subprocess.run(["pytest", "--allure-results", "--allure-allure-report-86%", "--clean-allure-results"])

    # 打开 HTML 报告
    # subprocess.run(["allure", "open", "./allure-allure-report-86%"])
    # subprocess.run(["allure", "serve", "./allure-allure-report-86%"])

    success, failure, error = count_allure_results()
    duration = time.time() - start_time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    msg = f"麦耳会记客户端UI自动化测试任务完成提醒 ({DEVICE_MODEL})\n\n"
    msg += f"测试任务: {TASK_NAME}\n"
    msg += f"所在团队: {TEAM_NAME}\n"
    msg += f"所在项目: {PROJECT_NAME}\n"
    msg += f"设备型号: {DEVICE_MODEL}\n"
    msg += f"网址: {URL}\n\n"
    msg += f"执行结果:\n"
    msg += f"总测试数: {success + failure + error}\n"
    msg += f"通过: {success}\n失败: {failure}\n错误: {error}\n"
    msg += f"总耗时: {duration:.2f} 秒\n执行时间: {timestamp}\n"
    # send_to_dingtalk(DINGTALK_WEBHOOK,msg)

if __name__ == "__main__":
    # schedule.every().day.at("12:09").do(run_all_scripts)
    # print("定时任务已启动，每天早上09:00自动测试并推送钉钉。")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    run_all_scripts()
