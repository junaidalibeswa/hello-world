str=input("Enter String:")
sub=input("Enter Sub String:")
n=len(str)
i=0
while i<n:
	index=str.find(sub,i,n)
	if index!=-1:
		print("Position of {} is {}".format(sub,index+1))
		i=index+1
	else:
		i+=1