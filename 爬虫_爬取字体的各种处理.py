import requests
from lxml import html
import re
url='http://v.baidu.com/'
page=requests.Session().get(url)
tree=html.fromstring(page.text)
#用xpath匹配字符
result=tree.xpath('//li//a/text()')
#去掉‘\n’的内容
result=[result.replace('\n','') for result in result]
#去掉空的列表
for i in result:
    while '' in result:
        result.remove('')
#把列表转化为字符串
result1 = " ".join(result)
#把字符串空格替换为换行符
result2=result1.replace(" ","\n")
print(result2)
