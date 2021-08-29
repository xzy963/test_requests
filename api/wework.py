import requests

from api.base_api import BaseApi


# 把获取token单独封装，因为所有的模块都需要用到token，方便调用
class WeWork(BaseApi):
    def get_token(self, secrete):
        # corpsecret的值通过test_department.py中的方法传入
        corpid = "wwd74e3907041f9300"
        corpsecret = secrete
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }

        return self.send(data)["access_token"]
