#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
'''这是写文件的函数'''
def write_file(liststr):
		 opfile=open("/home/yang/workspace/1.txt","r+")
		 opfile.seek(0,2)
		 opfile.write(liststr)
		 opfile.close
'''这是进行httppost的函数，url请求的地址，data是post的数据'''
def http_post(url,data):
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	return the_page
if __name__=='__main__':
	
	url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

	for i in range(1,100):
	
		num= str(i)
		data="cname=%E5%8C%97%E4%BA%AC&ppid=+&pageIndex="+num+"&pageSize=10"
		'''%E5%8C%97%E4%BA%AC这是”北京“进行了url编码之后的字符串，给pageIndex设置num就可以设置页码了'''
		the_page = http_post(url,data)
		'''这里的the_page是post后返回的数据，这个数据是json数据，下面的正则主要用来解析json数据'''
		print the_page
		searchObj = re.findall( r'"storeName":"([^"]*)', the_page, re.M|re.I)
		if len(searchObj)!=0:
		
			print len(searchObj)
			searchObj2 = re.findall( r'addressDetail":"([^"]*)', the_page, re.M|re.I)
			print len(searchObj2)
			searchObj3 = re.findall( r'"pro":"([^"]*)', the_page, re.M|re.I)
			print len(searchObj3)
			for j in range(0,len(searchObj)):
				count=str((i-1)*10+j+1)
				write_file('店名'+count+':'+''.join(searchObj[j])+'\n') 
				write_file('地址'+count+':'+''.join(searchObj2[j])+'\n') 
				write_file('服务'+count+':'+''.join(searchObj3[j])+'\n') 
		else :
			break