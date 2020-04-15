#knapsack using dp bottom top
C=int(input("Enter the capacity of the bag: "))
n=int(input("Enter the number of items: "))
print("Enter the weight of the items")
w = [int(i) for i in input().split()]
print("Enter the values of the items")
v = [int(i) for i in input().split()]
#rows will be 1 more than the number of items. Columns will be 1 more than the capacity
F=[[0 for i in range(C+1)]for j in range(n+1)]
for i in range(1,n+1):
	for j in range(1,C+1):
		if w[i-1]<=j:	#weight of the specified item is less than or equal to the current capacity j
			F[i][j]=max(F[i-1][j],F[i-1][j-w[i-1]]+v[i-1])	#max of including and not including
		else:
			F[i][j]=F[i-1][j]


print("The maximum value is: ",F[n][C])

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
