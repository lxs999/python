# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 注释省略
    # 摄像600秒5次
    sleep(1)
    os.system('adb shell input tap 378 1271')
    sleep(600)
    os.system('adb shell input tap 378 1271')


if __name__ == '__main__':
    total_times = 5
    times = 1

    while times <= total_times:
        photo()
        print(times)
        times += 1