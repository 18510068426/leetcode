from case.url import *
from common.req import *
import pytest

path = '/sq6'

class Test_sq6:
    @pytest.mark.sq
    def test_check_sq1(self):
       url = url_sql_test + path
       res = req.r_get(url).text
       assert  res == "(902, '张老二', '男', 1986, '中文系', '北京市昌平区')"


