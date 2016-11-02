def rec_mvarray(a,mid,start,end):
	m=mid-1
	s=start
	e=end
	while (m>=0)and(e>=mid):
		trans=a[m]
		a[m]=a[e]
		a[e]=trans
		m-=1
		e-=1
	for i in range(0,len(a)):
		print a[i]
	print "\n"
	if (m<0)and(e<mid):
		return
	if m<0:
		end=end-mid
	else:
		end=mid-1
		mid=m+1
	rec_mvarray(a,mid,start,end)
a=[1,2,3,4,5,6,7,8,9,10,11]
rec_mvarray(a,4,0,len(a)-1)
