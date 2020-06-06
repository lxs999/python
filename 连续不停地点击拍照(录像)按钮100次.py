# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 注释省略
    # 连续不停地点击录像按钮100次
    # 如果手机响应不过来，可提示“无响应”，但不可出现意外停止，死机，无法再进入相机等异常。
    os.system('adb shell input tap 243 845')


if __name__ == '__main__':
    total_times = 100
    times = 1

    while times <= total_times:
        photo()
        print(times)
        times += 1