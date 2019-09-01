#coding:utf-8
#################################################
#             获取手机cpu信息的类
#################################################

from lib import  SystemInfo
import subprocess
from lib import BaseClass

class CpuInfo(BaseClass.BaseClass):
    def __init__(self):
        pass

    #################################################
    #             获取指定应用用的cpu使用率信息（单位%）
    #             返回结果：25.8
    #             【注意有的手机获取到的cpu使用率可能为0，比如：Meizu M5 Note】
    #              计算方式：应用cpu使用率 = 该应用所有进程的使用率之和：例如：  CPU = cpu1(io.baba.oo) + cpu2(io.baba.oo/music） + cpu3（io.baba.oo/socket)
    #################################################
    def getCpuInfo(self,packageName):
        cmd = 'adb shell "top -n 1 | grep ' + packageName + '"'
        #cmd = 'adb shell "top -n 1'
        result = subprocess.getoutput(cmd)
        result1 = result.split("\n")

        # 去掉数组中的空格
        for i in range(len(result1) - 1, -1, -1):
            if result1[i] == "":
                result1.pop(i)
        info = []
        for j in range(0,len(result1)):
            tem = result1[j].split(" ")
            for i in range(len(tem) - 1, -1, -1):
                if tem[i] == "":
                    tem.pop(i)
            info.append(tem)

        #cpu使用率（百分比）
        cpu = 0
        cpu = self.getDiffDevCpuInfoByVersion(cpu,info)
        return cpu

    #################################################
    #             获取当前应用用的cpu信息
    #################################################
    def getCurAppCpuInfo(self):
        #TODO 获取当前应用用的cpu信息
        pass

    #################################################
    #             #根据手机型号，兼容获取cpu占用率
    #             供：getCpuInfo 方法调用
    #################################################
    def getDiffDevCpuInfoByModel(self,cpu,info):
        devModel = SystemInfo.SystemInfo().getMobileModel()
        print(devModel)
        type1 = ["vivo vivo X21A","HUAWEI EML-AL00"]
        type2 = ["Meizu M5 Note","xiaomi Redmi Note 4X"]
        type3 = ["HONOR ATH-AL00"]
        if devModel in type1:
            for i in range(0, len(info)):
                cpu = cpu + float(info[i][8])
        elif devModel in type2:
            for i in range(0, len(info)):
                cpu = cpu + float(info[i][4].replace("%",""))
        elif devModel in type3:
            for i in range(0, len(info)):
                cpu = cpu + float(info[i][2].replace("%",""))
        else:
            try:
                for i in range(0, len(info)):
                    cpu = cpu + float(info[i][8])
            except Exception:
                cpu = -1
        return cpu

    #################################################
    #             #根据手机系统，兼容获取cpu占用率(通过系统的方式来获取，还需要验证)
    #             供：getCpuInfo 方法调用
    #################################################
    def getDiffDevCpuInfoByVersion(self, cpu, info):
        devVer = SystemInfo.SystemInfo().getSysVersion()
        print(devVer)
        ver1 = ["9", "8.1.0"]
        ver2 = ["7.0"]
        ver3 = ["6.0.1"]
        if devVer in ver1:
            for i in range(0, len(info)):
                cpu = cpu + float(info[i][8])
        elif devVer in ver2:
            for i in range(0, len(info)):
                cpu = cpu + float(info[i][4].replace("%", ""))
        elif devVer in ver3:
            for i in range(0, len(info)):
                cpu = cpu + float(info[i][2].replace("%", ""))
        else:
            try:
                for i in range(0, len(info)):
                    cpu = cpu + float(info[i][8])
            except Exception:
                cpu = -1
        return cpu

    #################################################
    #             #获取当前运行进程的cpu信息，
    #             参考：https://www.cnblogs.com/liyuanhong/articles/11316366.html
    #             参考：https://www.cnblogs.com/liyuanhong/articles/11316337.html
    #             /proc/stat与top的cpu信息的联系与区别：
    #                     区别：/proc/stat文件显示的是从启动到当前时间，各种cup时间的累计值；而top则是显示实时的cpu使用情况。
    #                     联系：top通过读取/proc/stat去计算cpu占用情况。
    #                     /proc/stat 就像汽车仪表盘上的里程数，而top显示的cpu信息则是这辆车的速度。
    #################################################
    def getPorcessCpuInfo(self,packageName):
        #TODO  获取cpu信息的方法还需要做到如何对已经获取到的信息进行计算
        pid = SystemInfo.SystemInfo().getAppPidByAppname(packageName)
        cmd = 'adb shell "cat /proc/' + pid + '/stat"'
        print(cmd)
        result = subprocess.getoutput(cmd)
        print(result)




if __name__ == "__main__":
    print(CpuInfo().getCpuInfo("io.xxx.music"))
    #CpuInfo().getPorcessCpuInfo("io.xxx.music")