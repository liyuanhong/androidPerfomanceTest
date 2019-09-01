#coding:utf-8
#################################################
#             获取手机cpu信息的类型
#################################################

import subprocess
import re
from lib import BaseClass
from lib import AppInfo
from time import sleep
import platform
import datetime

class MemoryInfo(BaseClass.BaseClass):
    def __init__(self):
        pass

    #################################################
    #             获取自指定应用的内存信息
    #             返回一个元组，内容信息分别为：Pss total，Pss clean，Pss dirty
    #             返回值如：('232464', '214064', '10064')
    #################################################
    def getMemoryTotal(self,packageName):
        #result = subprocess.getoutput('adb shell "dumpsys meminfo ' + packageName + '"')
        result = subprocess.getoutput('adb shell "dumpsys meminfo ' + packageName + ' | grep TOTAL"')
        temp = result.split("\n")
        memInfo = temp[0]
        temp1 = memInfo.split(" ")
        for i in range(len(temp1) - 1,-1,-1):
            if temp1[i] == "":
                temp1.pop(i)
        return temp1[1],temp1[2],temp1[3]

    #################################################
    #             获取当前正在运行应用的内存信息
    #             返回一个元组，内容信息分别为：Pss total，Pss clean，Pss dirty
    #             返回值如：('232464', '214064', '10064')
    #################################################
    def getCurAppMemory(self):
        appName = AppInfo.AppInfo().getAppName()
        result = subprocess.getoutput('adb shell "dumpsys meminfo ' + appName + ' | grep TOTAL"')
        temp = result.split("\n")
        memInfo = temp[0]
        temp1 = memInfo.split(" ")
        #去掉数组中的空格
        for i in range(len(temp1) - 1, -1, -1):
            if temp1[i] == "":
                temp1.pop(i)
        return temp1[1], temp1[2], temp1[3]



    #################################################
    #             获取系统的总内存和空闲内存
    #             返回一个元组：MemTotal，MemFree，MemAvailable
    #             返回值如：('5700Mb', '770Mb', '1833Mb')
    #################################################
    def getSystemMemInfo(self):
        result = subprocess.getoutput('adb shell "cat /proc/meminfo"')

        temp = result.split("\n")
        for i in range(len(temp) - 1,-1,-1):
            if temp[i] == "":
                temp.pop(i)
        info = {}
        for istr in temp:
            tem = istr.split(":")
            key = tem[0]
            value = val = re.search('\d+', istr).group()
            info[key] = value
        total = str(int(int(info["MemTotal"]) / 1024)) + "Mb"
        free = str(int(int(info["MemFree"]) / 1024)) + "Mb"
        available = str(int(int(info["MemAvailable"]) / 1024)) + "Mb"
        return total,free,available

if __name__ == "__main__":
    curTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    if "Windows" in platform.platform():
        f = open("..\\log\\memoryinfo-" + curTime + ".txt", "a+",encoding="utf-8")
    else:
        f = open("../log/memoryinfo-" + curTime + ".txt", "a+",encoding="utf-8")

    while(True):
        total,aaa,bbb = MemoryInfo().getMemoryTotal("io.xxx.music")
        sleep(1)
        theTime = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        info = theTime + " 消耗内存 " + str(int(int(total)/1024)) + "\n"
        print(info.replace("\n",""))
        f.write(info)
        f.flush()

    # print(MemoryInfo().getCurAppMemory())