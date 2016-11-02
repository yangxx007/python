# -*- coding: utf-8 -*-
import threading 
from time import ctime,sleep
def fun1():
	print "fun1 running at %s" %ctime()
def fun2(str2):
	print str2+"fun2 running at %s" %ctime()
threads =[]
t1 = threading.Thread(target=fun1)
threads.append(t1)
t2 = threading.Thread(target=fun2,args=('test2:',))
'''这里传参数的时候一定要注意值后面有一个”，“号，
不能漏了，漏了会出错'''
threads.append(t2)

if __name__=='__main__':
	for t in threads:
		t.setDaemon (True)
		t.start()
	t.join()
	'''这里添加了t.join()的作用是为了让以上的子线程能运行完
	才能够接着下面的步骤，要不然主线程走完了，子线程都没有走完'''
	print "all over %s" %ctime()
	