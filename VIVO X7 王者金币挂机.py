# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 先把游戏放到闯关的界面

    os.system('adb -s 976c4fe3 shell input tap 1442 884')  # 闯关
    sleep(180)
    os.system('adb -s 976c4fe3 shell input tap 1573 961')  # 点击屏幕继续
    os.system('adb -s 976c4fe3 shell input tap 1643 991')  # 再次挑战

if __name__ == '__main__':
    total_times = 1000
    times = 1
print("VIVO X7 王者金币挂机")

while times <= total_times:
        photo()
        print(times)
        times += 1