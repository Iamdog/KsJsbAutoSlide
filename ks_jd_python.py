import os
from datetime import datetime
import time

# 秒数 
TIME = 15
# 100 1000为滑动开始坐标
# 100 200为滑动停止坐标
# 500 为滑动时长
SHELLCOMMAND = "adb shell input swipe 100 1000 100 200 300"

def adbShellCommand():
    os.system(SHELLCOMMAND)

# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        adbShellCommand()
        time.sleep(n)


def main():
    timer(15)

if __name__ == '__main__':
    main()