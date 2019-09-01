#coding:utf-8
#################################################
#             获取手机电量消耗信息的类
#################################################

import subprocess
from lib import  AppInfo
from lib import BaseClass
import re

class BatteryInfo(BaseClass.BaseClass):
    def __init__(self):
        pass

    ################################################
    #             重置耗电量数据
    #################################################
    def resetBatterInfo(self):
        cmd = 'adb shell "dumpsys batterystats --reset"'
        subprocess.getoutput(cmd)

    #################################################
    #             获取应用电量消耗(单位毫安)
    #################################################
    def getAppBatteryInfo(self,appName):
        #重置耗电量数据命令
        uid = AppInfo.AppInfo().getAppUid(appName)
        uid = uid.replace("_","")
        cmd = 'adb shell "dumpsys batterystats ' + appName + ' | grep ' + uid + '"'
        result = subprocess.getoutput(cmd)
        regx = re.compile(r':(.+?)\(',re.S)
        content = re.findall(regx,result)
        print(result)
        batteryVal = content[0].replace(" ","")
        return batteryVal


if __name__ == "__main__":
    pass
