n=int(input("Input an integer number:"))

i=2
x_small=0
x_large=1
x_large_1=0
x_small_1=0
while 2<=i<=n:
	if i!=2:#this step should be executed after iteration 1
		x_large,x_small=x_large_1,x_small_1
	x_small_1,x_large_1=x_large,x_large+x_small #the larger x in iteration n will become the smaller x in iteration (n+1) 
												#the sum of both the smaller x and the larger x in iteration n will become the larger x in iteration (n+1)
	i=i+1

final=x_large_1
#the below conditions aren't included in above program
#-------------------
if n==0:
	final=0
if n==1:
	final=1
#-------------------
print("The "+str(n)+"‐th Fibonacci sequence number is:",final)
