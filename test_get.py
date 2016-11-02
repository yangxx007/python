# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:03:25 2016

@author: yang-pc
"""

import urllib
def get_html(url):
       sock = urllib.urlopen(url)
       htmlSource = sock.read()
       sock.close()
       return htmlSource
url="http://bj.jumei.com/Ajax/GetHomeTodayLists/100/101"



print eval('\"\u7389\u306e\u808c\u65e0\u6dfb\u52a0004\u6800\u5b50\u82b1\u6d17\u53d1\u7cfb\u5217!\u4e00\u6d17\u4eae\u53d1\u51fa\u4f17\uff0c\u4e8c\u62a4\u4e1d\u6ed1\u82ac\u82b3\"'+'.decode(unicode-escape)')