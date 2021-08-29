import requests
from api.wework import WeWork


class Department(WeWork):
    def __init__(self):
        secrete = "HUxknOtZAcgdx6QBP1NJQvvYba0OkpRBzoISpItXTIY"
        self.token = WeWork().get_token(secrete)

    # 创建成员具体步骤
    def create(self, usid, name, mobile):
        # data = {"name": name, "parentid": id}
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": usid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }
        }

        return self.send(data)

    # 更新标签名具体步骤
    # **kwargs 表示关键字参数，它本质上是一个 dict
    def update(self, id, **kwargs):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {"userid": id}
        data.update(kwargs)
        r = requests.post(base_url,
                          params={"access_token": WeWork.get_token(self.secrete)},
                          json=data
                          )
        return r.json()

    # 删除标签具体步骤
    def delete(self, id):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = requests.get(base_url,
                         params={"access_token": WeWork.get_token(self.secrete),
                                 "userid": id
                                 }
                         )
        return r.json()

    # 获取标签具体步骤
    def get(self, id=1):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = requests.get(base_url,
                         params={"access_token": WeWork.get_token(self.secrete),
                                 "id": id
                                 }
                         )
        return r.json()
