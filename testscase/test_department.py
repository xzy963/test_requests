import pytest
from api.department import Department
from api.wework import WeWork


class TestDepartment:
    def setup(self):
        self.department = Department()

    # 创建成员
    def test_create(self):
        r = self.department.create("lisi", "李四", "11111111119")
        assert r["errmsg"] == "created"

    # 更新标签名
    def test_update(self):
        r = self.department.update("lisi", name="王二")
        assert r["errmsg"] == "updated"

        # 获取标签

    def test_get(self):
        r = self.department.get("lisi")
        assert r["userid"] == "lisi"
        print(r)

    # 删除标签
    def test_delete(self):
        r = self.department.delete("lisi")
        assert r["errmsg"] == "deleted"
