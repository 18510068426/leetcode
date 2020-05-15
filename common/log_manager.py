import logging
import sys
import threading
import os
import time
def synchronized(func):
    func.__lock__ = threading.Lock()
    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


class log_manager(object):
    instance = None
    @synchronized
    def __new__(cls, *args, **kwargs):
        """
        :type kwargs: object
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, path=r'C:\Users\18510\Desktop\work\leetcod\logs'+ '\\'+str(time.time())+".log",level=logging.INFO):
      self.path = path
      self.formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} [%(levelname)s] - %(message)s')
      self.logger = logging.getLogger('main')
      #写文件的权限
      self.logger.setLevel(logging.INFO)
      self.level = level
      self.ch = logging.StreamHandler(sys.stdout)
      self.ch.setFormatter(self.formatter)
      self.ch.setLevel(self.level)
      self.logger.addHandler(self.ch)
      self.fh = logging.FileHandler(self.path, encoding='utf-8')
      self.fh.setFormatter(self.formatter)
      self.fh.setLevel(logging.DEBUG)
      self.logger.addHandler(self.fh)

    #设置写文件的等级
    def set_level(self,my_level=logging.INFO):
        self.logger.setLevel(my_level)

    def get_path(self):
        self.my_dir = os.getcwd()

if __name__ =="__main__":
# print os.getcwd() #获取当前工作目录路径
# print os.path.abspath('.') #获取当前工作目录路径
# print os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
# print os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
## print os.path.abspath(os.curdir) #获取当前工作目录路径
#print sys.argv  # 输入参数列表
#print sys.argv[0]  # 第0个就是这个python文件本身的路径（全路径）
#print os.path.basename(sys.argv[0])  # 当前文件名名称
#print os.path.basename(__file__)  # 当前文件名名称
    print(os.path.abspath('.'))
    print(type(os.getcwd()))
    logg = log_manager()
    logg.set_level(logging.DEBUG)
    logg.logger.debug("123123")
    logg.logger.info("222222")