# _*_ coding=utf-8 _*_
# import datetime
import time
import sys


def get_time():
    """
    :return:返回时间戳
    """
    # now = datetime.datetime.now()
    # return now.strftime("%Y-%m-%d_%H_%M_%S")
    return time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))


def get_slash():
    """
    :return:根据不同的操作系统返回不同的文件分割线
    """
    if sys.platform != "win32":
        return "/"
    else:
        return "\\"





