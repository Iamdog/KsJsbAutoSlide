import os,subprocess
import re
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
# 200 为滑动时长
SHELLCOMMAND = "./adb -s  {} shell  input swipe 100 1000 100 200 200"
# 启动快手极速版
STARTKSJSBAPP = "./adb -s {} shell am start -W -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity"

def adbShellCommand(device):
    # os.system(STARTKSJSBAPP.format(device))
    os.system(SHELLCOMMAND.format(device))


# 获取多个adb连接设备
def getAllAdbDevices():
    deviceInfo= os.popen("./adb devices").read()
    deviceInfo  = deviceInfo.replace("List of devices attached","").replace('\n', '').replace('\r', '').replace('\t','')
    deviceNames = deviceInfo.split("device")
    return deviceNames

# 每n秒执行一次
def timer():
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        deviceNames = getAllAdbDevices()

        if len(deviceNames)==0:
            continue
        
        for device in deviceNames:
            if device == '':
                continue
            adbShellCommand(device)
        
        randomNum = random.randint(startRange,endRange)
        print("时长:>>>>",randomNum)
        time.sleep(randomNum)






def main():
    timer()

if __name__ == '__main__':
    main()