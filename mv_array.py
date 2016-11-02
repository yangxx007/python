NUM=0
def mv_array(a,start,i):
	key=a[start]
	n=len(a)
	k=0
	global NUM
	while True:
		m=((k+1)*i+start)%n
		if m!=start:
			a[m-i]=a[m]
			NUM+=1
			k+=1
		else :
			break
	a[start-i]=key
	if NUM<(len(a)-1):
		for j in range(0,len(a)):
			print a[j]
		print "\n"
		mv_array(a,start+1,i)
	else:
		return
a=[1,2,3,4,5,6,7,8,9]
mv_array(a,0,3)
