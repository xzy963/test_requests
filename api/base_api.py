# 用于存放一些公共操作
import requests

class BaseApi:
    def send(self, data):
        return requests.request(**data).json()