#抓取网页上的数据，存入TXT文件
import sys
from random import Random
import requests
import json;
import urllib.request
import re
from bs4 import BeautifulSoup  
import os
import hashlib

URL_COUNT = 0

def prend(str):
    print (str)
    sys.exit(0)

def pre(str):
    print (str)



def obtainSkuList(content):
	reg = r'data-sku="([0-9]{9})"'
	imgreg = re.compile(reg)
	imgList = imgreg.findall(content)
	
	return imgList



def downUrlImage(imgList,url):
	rootPath = 'F://luolaifa/sku.txt'
	
	skuString = ''
	for imgurl in imgList:
		skuString = skuString + ',' + imgurl
		
	skuString = skuString.strip(',')

	f = open(rootPath, 'w+') # 若是'wb'就表示写二进制文件
	f.write(skuString)
	f.close() 
	
def grapUrl(url):
	global URL_COUNT
	# if URL_COUNT > 10:
	# 	print (URL_COUNT)
	# 	URL_COUNT = 0
	# 	sys.exit(0)
	URL_COUNT = URL_COUNT + 1
	content = getHtml(url)

	imgList = obtainSkuList(content)
	#hrefList = obtainHref(content)
	
	downUrlImage(imgList,url)


	

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()

    return html.decode('UTF-8')


	
	
	

def main():
	url = 'https://www.rosegal.com/men-108/'
	grapUrl(url)
if __name__ == '__main__':
	main()
