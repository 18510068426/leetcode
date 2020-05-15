import requests
import logging
class req:
    def __init__(self):
         pass

    #跳过http验证
    @classmethod
    def r_get(self,url,data=''):
       return requests.get(url,data=data,verify=False)

    @classmethod
    def r_post(self,url,data,head=''):

       return requests.get(url,data,head=head,verify=False)


