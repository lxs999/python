# !/usr/bin/python
# coding=utf-8

import os
from time import sleep


def photo():
    # 注释省略
    os.system('adb shell am start com.android.camera2/com.android.camera.CameraLauncher')
    sleep(1)

    os.system('adb shell input keyevent KEYCODE_HOME')
    sleep(1)


if __name__ == '__main__':
    total_times = 100
    times = 1

    while times <= total_times:
        photo()
        print(times)
        times += 1