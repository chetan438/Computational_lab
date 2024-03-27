#write a programme to divide two numbers
a=input("Enter a =")
b=input("Enter b =")
if (a.isalnum() and b.isalnum()):
	if a.isalpha()!= True and b.isalpha()!=True:
		print("divison of a and b =",float(a)/float(b))
	else:
		print("enter valid input")
else:
	print("enter valid input")
