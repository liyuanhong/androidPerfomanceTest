#coding:utf-8
#################################################
#             获取手机当前应用的信息的类
#################################################
from lib import BaseClass
import subprocess
import re

class AppInfo(BaseClass.BaseClass):
    def __init__(self):
        pass

    #################################################
    #             获取当前的activity【根据包名】
    #################################################
    def getCurrentActivityByPac(self,packageName):
        cmd = 'adb shell "dumpsys activity activities | grep Run | grep '+ packageName + '"'
        result = subprocess.getoutput(cmd)
        result1 = re.findall('\{(.+)\}', result)[0]
        result2 = result1.split(" ")
        activity = result2[2]
        return activity

    #################################################
    #             获取当前的activity【不需要传参】
    #################################################
    def getActivity(self):
        cmd = 'adb shell "dumpsys activity activities | grep Run"'
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")

        #去掉数组中带#号的行
        for i in range(len(result1) - 1,-1,-1):
            if not "#" in result1[i]:
                result1.pop(i)

        result2 = result1[0]
        result3 = re.findall('\{(.+)\}', result2)[0]
        result4 = result3.split(" ")
        activity = result4[2]
        return activity

    #################################################
    #             获取当前应用的包名
    #################################################
    def getAppName(self):
        activity = self.getActivity()
        info = activity.split("/")
        return info[0]

    #################################################
    #             获取应用的userId
    #################################################
    def getAppUserid(self,appName):
        cmd = 'adb shell "dumpsys package ' + appName +' | grep userId"'
        #cmd = 'adb shell "dumpsys package ' + appName + '"'
        result = subprocess.getoutput(cmd)
        result1 = result.split("=")
        result2 = []
        #去掉数组中字符串的空格
        for temp in result1:
            result2.append(temp.replace(" ",""))
        return result2[1]

    #################################################
    #             获取包名的uid
    #################################################
    def getAppUid(self,appName):
        cmd = 'adb shell "ps | grep io.liuliu.music"'
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")
        result2 = result1[0].split(" ")
        # 去掉数组中的空格
        for i in range(len(result2) - 1, -1, -1):
            if result2[i] == "":
                result2.pop(i)
        return result2[0]

    #################################################
    #             获取当前应用的userId
    #################################################
    def getCurAppUserid(self):
        appName = self.getAppName()
        cmd = 'adb shell "dumpsys package ' + appName + ' | grep userId"'
        # cmd = 'adb shell "dumpsys package ' + appName + '"'
        result = subprocess.getoutput(cmd)
        result1 = result.split("=")
        result2 = []
        # 去掉数组中字符串的空格
        for temp in result1:
            result2.append(temp.replace(" ", ""))
        return result2[1]


if __name__ == "__main__":
    pass