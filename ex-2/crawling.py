# -*-coding:utf8-*-
# beautifulsoup版爬虫方法，字符编码处理思想与前者相同，但获取注释比lxml好用
# 用python2.7编写
from BeautifulSoup import BeautifulSoup
import urllib2
import sys
import time
bt = time.time()
reload(sys)
sys.setdefaultencoding('utf-8')
print "Homework - web data crawling - 2017.3.23 - by zht"
url = "http://www.cnemc.cn"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
titleTag = soup.html.head.title
print "Now begin crawling:",titleTag.string
tbody = soup.find(id='kqzlrb1').table.tbody
alltr = tbody.findAll('tr')
fo = open("data2.txt", "wb")
text = '地区,首要污染物,等级,AQI,'+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+'\r\n'
print text.decode('utf-8')
n = 0
for each in alltr:
    n += 1 #计数器
    row = ''
    flg = 0
    alltd = each.findAll('td')
    for td in alltd:
        flg += 1
        if(flg == 1):
            row = row + str(td.contents[1]) + ',' #使用contents获取注释中的文字
        else:
            row = row + str(td.string).decode('utf-8') + ','#str()将获取的unicode编码的文字字符串化再进行utf8编码，保证各端输出无问题
    row = row[0:-1]
    text = text + row + "\r\n"
    print row
print u"There are %d cities in total"%n
fo.write(text)
fo.close()
et = time.time()
print u"已保存,总共花时：", et-bt
