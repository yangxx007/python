# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:03:25 2016

@author: yang-pc
"""

import urllib
def write_file(liststr):
		 opfile=open("/home/yang/workspace/1.txt","r+")
		 '''这里要设置一下文件路径，并且要在该路径下创建1.txt文件'''
		 opfile.seek(0,2)
		 opfile.write(liststr)
		 opfile.close
def scroll_next(nextURL):
       nnURL= analysis_html(get_html(nextURL))
       if len(nnURL)!=0:
           scroll_next(nnURL)
       else:
       	  print "输出完毕！！！"
def get_html(url):
       sock = urllib.urlopen(url)
       htmlSource = sock.read()
       sock.close()
       return htmlSource
def analysis_html(htmlSource):
       #from lxml import etree
       import lxml.html.soupparser as soupparser
       dom = soupparser.fromstring(htmlSource)
       #doc = dom.parse(dom)
       r = dom.xpath('//*[@id="content"]/div/div[1]/div/table') 
       for i in range(0,len(r)-1):
           nodes= r[i].xpath('tr/td/a/@href')
           tnodes=r[i].xpath('tr/td/a/@title')
           scores=r[i].xpath('tr/td[2]/div/div/span[2]')
           title =''.join(tnodes)
           str_title=title.encode("utf-8")
           write_file("\n"+"Title:"+str_title)        
           href= ''.join(nodes)
           str_href=href.encode("utf-8")
           write_file("\n"+"Href:"+str_href)            
           score= ''.join(scores[0].text)
           str_score=score.encode("utf-8")
           write_file("\n"+"Score:"+str_score)
       r = dom.xpath('//*[@id="content"]/div/div[1]/div/div[26]/span[3]/a/@href')
       #print 'done'
       return ''.join(r)
if __name__='__main__':
	
	print get_html('https://p.3.cn/prices/mgets?callback=jQuery6669569&type=1&area=1_72_4137_0&skuIds=J_1856584%2CJ_3865398%2CJ_2512095%2CJ_1820367%2CJ_3499302&pdbp=0&pdtk=&pdpin=&pduid=1041127965&_=1477361499329')
	#nextURL=analysis_html(get_html('https://music.douban.com/top250'))
	#scroll_next(nextURL)
