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



def obtainImgList(content):
	reg = r'data-original="(.+?\.jpg|.+?\.JPG)"'
	imgreg = re.compile(reg)
	imgList = imgreg.findall(content)
	return imgList

def obtainHref(content):
	BS = BeautifulSoup(content, "html.parser")
	links = BS.find_all("a", rel="nofollow")  # 获取用户的a标签
	hrefs = []
	for a in links:
		if a:
		    href = a.get('href')
		    hrefs.append(href)
		else:
		    print("获取失败，跳过")
		    continue
	return hrefs

def downUrlImage(imgList,url):
	rootPath = 'F://luolaifa'
	md5 = hashlib.md5(url.encode('utf-8')).hexdigest()
	path = rootPath + '/' + md5
	filepath = path.strip()
	dirpath = filepath.strip("\\")
	isExists = os.path.exists(dirpath)

	if isExists == False : 
		os.makedirs(dirpath)

	x = 0
	paths = dirpath + '\\'
	
	for imgurl in imgList:
		sss  = re.findall(r'/\s',imgurl)
		if len(imgurl) > 200:
			continue
		
		
		page = urllib.request.urlopen(imgurl)
		binary_data = page.read()
		temp_file = open(paths + str(x) + '.jpg' , 'wb')
		temp_file.write(binary_data)
		temp_file.close()
		x = x + 1

def queryTicket(url):
	global URL_COUNT
	# if URL_COUNT > 10:
	# 	print (URL_COUNT)
	# 	URL_COUNT = 0
	# 	sys.exit(0)
	URL_COUNT = URL_COUNT + 1
	content = getHtml(url)
	imgList = obtainImgList(content)
	hrefList = obtainHref(content)
	
	downUrlImage(imgList,url)

	for href in hrefList:
		queryTicket(href)
	

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')


	
	
	

def main():
	url = 'https://www.rosegal.com'
	queryTicket(url)
if __name__ == '__main__':
	main()
