#you can remenber this way by reversing your own hands
def reverse_array(a,start,end):
	tmp=[0]*(end-start)
	tmp[0:end-start]=a[start:end]
	tmp.reverse()
	a[start:end]=tmp[0:end-start]
def mv_array(a,i):
	reverse_array(a,0,i)
	reverse_array(a,i,len(a))
	reverse_array(a,0,len(a))
if __name__=='__main__':
	a=[1,2,3,4,5,6,7,8,9,10]
	mv_array(a,5)
	for i in range(0,len(a)):
		print a[i]