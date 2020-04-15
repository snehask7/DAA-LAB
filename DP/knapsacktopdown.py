#knapsack using dp top down memory function
# solving only the necessary subproblems
def knapsack(i,j):
	if F[i][j]<0: #value not yet found
		if w[i-1]>j:
			value=knapsack(i-1,j)
		else:
			value=max(knapsack(i-1,j-w[i-1])+v[i-1],knapsack(i-1,j))
		F[i][j]=value
	return F[i][j]


C=int(input("Enter the capacity of the bag: "))
n=int(input("Enter the number of items: "))
print("Enter the weight of the items")
w = [int(i) for i in input().split()]
print("Enter the values of the items")
v = [int(i) for i in input().split()]
#rows will be 1 more than the number of items. Columns will be 1 more than the capacity
F=[[-1 for i in range(C+1)]for j in range(n+1)]
for i in range(n+1):
	F[i][0]=0
for i in range(C+1):
	F[0][i]=0
maxvalue=knapsack(n,C)
for i in range(n+1):
	print(F[i])
print(maxvalue)

"""
OUTPUT

Enter the capacity of the bag: 5
Enter the number of items: 4
Enter the weight of the items
2 1 3 2
Enter the values of the items
12 10 20 15 
The maximum value is:  37

"""
