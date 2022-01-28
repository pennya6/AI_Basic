#정규식 인 파이썬 for html
import urllib.request
import re

url="http://finance.naver.com/item/main.nhn?code=005930"
html=urllib.request.urlopen(url)
html_contents=str(html.read().decode("ms949"))
#print(html_contents)
stock_results=re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/d1\>)",html_contents)
samsung_stock=stock_results[0]

samsung_index=samsung_stock[1]

index_list=re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)",samsung_index)

for index in index_list:
    print(index[1])