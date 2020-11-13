import os
from datetime import datetime
import time
import random


# 随机数的范围
startRange = 10
endRange = 20
# 秒数 
TIME = 15
# 100 1000为滑动开始坐标
# 100 200为滑动停止坐标
# 300 为滑动时长
SHELLCOMMAND = "./adb shell input swipe 100 1000 100 200 300"
# 启动快手极速版
STARTKSJSBAPP = "./adb shell am start -W -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity"

def adbShellCommand():
    os.system(SHELLCOMMAND)

# 每n秒执行一次
def timer():
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        adbShellCommand()
        randomNum = random.randint(startRange,endRange)
        print("时长:>>>>",randomNum)
        time.sleep(randomNum)


def main():
    os.system(STARTKSJSBAPP)
    time.sleep(5)
    timer()

if __name__ == '__main__':
    main()