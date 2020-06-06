# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 先把游戏放到再次挑战界面
    
    os.system('adb -s e6bbe06a shell input tap 1066 610')  # 闯关
    sleep(180)
    os.system('adb -s e6bbe06a shell input tap 1175 659')  # 点击屏幕继续
    os.system('adb -s e6bbe06a shell input tap 1266 671')  # 再次挑战

if __name__ == '__main__':
    total_times = 1000
    times = 1

print("VIVO Y79A 王者金币挂机")
while times <= total_times:
        photo()
        print(times)
        times += 1
