# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 注释省略
    # 拍照100次
    os.system('adb shell input tap 378 1271')


if __name__ == '__main__':
    total_times = 50
    times = 1

    while times <= total_times:
        photo()
        print(times)
        times += 1
