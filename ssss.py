from common.req import *
from case.url import *
path = '/sq9'
url = url_sql_test + path
# c = req.r_get('http://127.0.0.1:5000/sq1').text
c = req.r_get(url).text
print(c)
assert c =="(901, '张老大', '男', 1985, '计算机系', '北京市海淀区')"
