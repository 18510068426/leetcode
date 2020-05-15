from case.url import *
from common.req import *
import pytest

path = '/sq3'

class Test_sq3:
    @pytest.mark.sq
    def test_check_sq1(self):
       url = url_sql_test + path
       res = req.r_get(url).text
       assert  res == "('计算机', 70)"