a=[1,2,3]
b=[3,5,7]
c='ijk'
for i in range(3):
	if (type(a[i])==int or float) and (type(b[i])==int or float):
		print((a[i]*b[i]),c[i],sep='')
	else:
		print('invalid data')
