#coding:utf-8
#################################################
#             获取手机系统信息的类
#################################################

from lib import BaseClass
from lib import AppInfo
import subprocess

class SystemInfo(BaseClass.BaseClass):
    def __init__(self):
        pass

    #################################################
    #             获取当前正在运行的app的所有进程，以字典形式返回
    #             值如：{'11215': 'io.baba.muu', '11312': 'io.baba.muu:socket', '11520': 'io.baba.muu:channel'}
    #################################################
    def getCurrentAppProcess(self):
        curApp = AppInfo.AppInfo().getAppName()
        cmd = 'adb shell "ps | grep ' + curApp + '" '
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")

        #app的所有进程
        appProcess = []
        for temp in result1:
            temp1 = temp.split(" ")
            for i in range(len(temp1) - 1, -1, -1):
                if temp1[i] == "":
                    temp1.pop(i)
            appProcess.append(temp1)
        #将app进程转换纹一个字典，key为进程号；value为进程名
        appProcessDic = {}
        for tem in appProcess:
            appProcessDic[tem[1]] = tem[8]
        return appProcessDic

    #################################################
    #             获取指定运行的app的所有进程，以字典形式返回
    #             值如：{'11215': 'io.baba.muu', '11312': 'io.baba.muu:socket', '11520': 'io.baba.muu:channel'}
    #################################################
    def getAppProcessByAppname(self,appName):
        cmd = 'adb shell "ps | grep ' + appName + '" '
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")

        # app的所有进程
        appProcess = []
        for temp in result1:
            temp1 = temp.split(" ")
            for i in range(len(temp1) - 1, -1, -1):
                if temp1[i] == "":
                    temp1.pop(i)
            appProcess.append(temp1)
        # 将app进程转换纹一个字典，key为进程号；value为进程名
        appProcessDic = {}
        for tem in appProcess:
            appProcessDic[tem[1]] = tem[8]
        return appProcessDic


    #################################################
    #             获取当前正在运行app的主进程号
    #################################################
    def getCurrentAppPid(self):
        process = self.getCurrentAppProcess()
        keys = list(process.keys())
        return keys[0]

    #################################################
    #             获取当前正在运行app的主进程号
    #################################################
    def getAppPidByAppname(self,appName):
        process = self.getAppProcessByAppname(appName)
        keys = list(process.keys())
        return keys[0]

    #################################################
    #             获取当前手机基本信息
    #################################################
    def getMobileInfo(self):
        #TODO  获取当前手机基本信息
        pass

    #################################################
    #             获取当前连接的手机
    #             返回值为数组：['7f09daff', 'CLB7N19118013794']
    #################################################
    def getConnectMobiles(self):
        cmd = 'adb devices'
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")
        # 去掉数组中的空格
        for i in range(len(result1) - 1, -1, -1):
            if result1[i] == "":
                result1.pop(i)
        devices = []
        for i in range(1,len(result1)):
            temp = result1[i].split("\t")
            devices.append(temp[0])
        return devices

    #################################################
    #             获取手机的系统版本
    #################################################
    def getSysVersion(self):
        cmd = 'adb shell getprop ro.build.version.release'
        result = subprocess.getoutput(cmd)
        return result.replace("\n","")

    #################################################
    #             获取手机的分辨率
    #################################################
    def getMobileSize(self):
        cmd = 'adb shell wm size'
        result = subprocess.getoutput(cmd)
        result1 = result.split(":")
        result2 = result1[1].replace("\n","")
        result3 = result2.replace(" ","")
        return  result3

    #################################################
    #             获取手机的型号
    #################################################
    def getMobileModel(self):
        cmd1 = 'adb -d shell "getprop ro.product.model"'
        cmd2 = 'adb -d shell "getprop ro.product.brand"'
        result1 = subprocess.getoutput(cmd1).replace("\n","")
        result2 = subprocess.getoutput(cmd2).replace("\n", "")
        result = result2 + " " + result1
        return result

    #################################################
    #             获取手机电池信息
    #             返回结果为一个元组，数据分别为：1、电量百分比2、电池温度(单位为0.2摄氏度)3、电池状态，是否充电（2为充电状态）4、电池健康状态（2为健康）
    #             返回结果如下：('69', '315', '2', '2')
    #################################################
    def getBatteryInfo(self):
        cmd = "adb shell dumpsys battery"
        result = subprocess.getoutput(cmd).split("\n")
        result1 = {}
        result2 = []
        for i in range(1,len(result)):
            itemArr = result[i].replace(" ","").split(":")
            result1[itemArr[0]] = itemArr[1]
            result2.append(itemArr[1])
        return result1["level"],result1["temperature"],result1["status"],result1["health"]


if __name__ == "__main__":
    # print(SystemInfo().getCurrentAppProcess())
    # print(SystemInfo().getCurrentAppPid())
    # print(SystemInfo().getConnectMobiles())
    # print(SystemInfo().getSysVersion())
    # print(SystemInfo().getMobileSize())
    # print(SystemInfo().getMobileModel())
    print(SystemInfo().getBatteryInfo())
