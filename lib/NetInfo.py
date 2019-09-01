#coding:utf-8
#################################################
#           获取手机网络流量信息的类
#################################################
from lib import BaseClass
from lib import AppInfo
import subprocess

class NetInfo(BaseClass.BaseClass):
    def __init__(self):
        pass

    #################################################
    #           获取手机的上行与下行流量，返回接收和发送流量（单位Kb）
    #           返回结果为元组：(93264, 6011)
    #################################################
    def getNetFlowData(self,appName):
        userId = AppInfo.AppInfo().getAppUserid(appName)
        cmd = 'adb shell "cat /proc/net/xt_qtaguid/stats | grep ' + userId + '"'
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")
        #去掉数组中的空格
        for i in range(len(result1) - 1, -1, -1):
            if result1[i] == "":
                result1.pop(i)
        result2 = []
        for temp in result1:
            result2.append(temp.split(" "))
        #接收流量
        inputStream = 0
        #发送的流量
        outputStream = 0
        for temp in result2:
            inputStream = inputStream + int(temp[5])
            outputStream = outputStream + int(temp[7])
        #return inputStream,outputStream
        return int(inputStream/1024),int(outputStream/1024)


if __name__ == "__main__":
    #print(AppInfo().getCurrentActivityByPac("io.xxx.music"))
    # print(AppInfo().getActivity())
    # print(AppInfo().getAppUserid("io.xxx.music"))
    print(NetInfo().getNetFlowData("io.xxx.music"))


