from case.url import *
from common.req import *
import pytest

path = '/sq4'

class Test_sq4:
    @pytest.mark.sq
    def test_check_sq1(self):
       url = url_sql_test + path
       res = req.r_get(url).text
       assert  res == "(901, '张老大', '男', 1985, '计算机系', '北京市海淀区', '计算机', 98)"