from case.url import *
from common.req import *
import pytest

path = '/sq5'

class Test_sq5:
    @pytest.mark.sq
    def test_check_sq1(self):
       url = url_sql_test + path
       res = req.r_get(url).text
       assert  res == "(901, '张老大', Decimal('178'))"