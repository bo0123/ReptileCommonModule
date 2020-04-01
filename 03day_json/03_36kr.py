# coding=utf-8
import re
from parse_url import parse_url
import json

url = "https://36kr.com/"
html_str = parse_url(url)
print(html_str)

# - 往一个文件中写入多个json串，不再是一个json串，不能直接读取
#   - 一行写一个json串，按照行来读取
ret = re.findall("<script>var props=(.*?)</script>",html_str)[0]
# ret = re.findall("<script>var props=(.*?),locationnal=",html_str)[0]

with open("36kr.json","w",encoding="utf-8") as f:
    f.write(ret)

ret = json.loads(ret)
print(ret)