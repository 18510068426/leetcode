from case.url import *
from common.req import *
import pytest

path = '/sq2'

class Test_sq2:
    @pytest.mark.sq
    def test_check_sq1(self):
       url = url_sql_test + path
       res = req.r_get(url).text
       assert  res == "('中文', 95)"








