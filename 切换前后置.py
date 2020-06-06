# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 注释省略
    # 摄像头切换前后置
    os.system('adb shell input tap 431 25')
    sleep(1)


if __name__ == '__main__':
    total_times = 100
    times = 1

    while times <= total_times:
        photo()
        print(times)
        times += 1