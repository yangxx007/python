#!/usr/bin/python
def half_search(a,start,end,val):
	mid=(start+end)/2
	if (end==start)or(end==mid)or(start== mid):
		return None
	if a[mid]<val:
		start=mid
	elif a[mid]>val:
		end= mid
	elif a[mid]==val:
		return mid
	
	return half_search (a,start,end,val)
if __name__=='__main__':
	a=[1,2,3,5,6,7,8,9,10,12,13,14,15,16,17,18,19]
	b=[2,3,23,5,64,7,46,34,64,21,53,75,3,7,4,73,86]
	#b.sort()
	c=sorted(b)
	s= half_search(c,-1,len(c),34)
	#s=return_func(a)b
	print s