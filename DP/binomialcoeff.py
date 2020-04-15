#Binomial Coefficient using DP
#F(n,k)=F(n-1,k-1)+F(n-1,k)
n=int(input("enter the value of n: "))
k=int(input("enter the value of k: "))
F=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n+1):
	F[i][0]=1
	F[i][i]=1
for i in range(1,n+1):
	for j in range(1,k+1):	
		F[i][j]=F[i-1][j-1]+F[i-1][j]
print("(",n,",",k,") is: ",F[n][k])

"""
OUTPUT

enter the value of n: 6
enter the value of k: 3
( 6 , 3 ) is:  20

"""
