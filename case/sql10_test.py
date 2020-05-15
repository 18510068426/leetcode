from case.url import *
from common.req import *
import pytest

path = '/sq10'

class Test_sq10:
    @pytest.mark.sq
    def test_check_sq1(self):
       url = url_sql_test + path
       res = req.r_get(url).text
       assert  res == "(903, '张三', '女', 1990, '中文系', '湖南省永州市', '中文', 95)"