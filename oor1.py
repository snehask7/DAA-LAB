"""1. Design an algorithm using brute-force/exhaustive enumeration of all possible pairs of la-
bels. Implement the algorithm in Python."""

#TIME COMPLEXITY IS O(n^2)
def oop(a):
	n=len(a)
	num=0
	for i in range (n-1):
		for j in range(i+1,n):
			if a[i]>a[j]:
				num=num+1
				print("("+str(a[i])+","+str(a[j])+")")
	return num
print("Array is: [1, 2, 3, 4, 5]")
n=oop([1, 2, 3, 4, 5])
print("Total number of out of order pairs is: "+str(n))
print("\n")
print("Array is: [3, 1, 2, 5, 4]")
n=oop([3, 1, 2, 5, 4])
print("Total  number of out of order pairs is: "+str(n)) 
print("\n")
print("Array is: [2, 4, 1, 3, 5]")
n=oop([2, 4, 1, 3, 5])
print("Total number of out of order pairs is: "+str(n)) 
print("\n")
print("Array is: [5, 4, 3, 2, 1]")
n=oop([5, 4, 3, 2, 1])
print("Total number of out of order pairs is: "+str(n)) 


"""
OUTPUT

Array is: [1, 2, 3, 4, 5]
Total number of out of order pairs is: 0


Array is: [3, 1, 2, 5, 4]
(3,1)
(3,2)
(5,4)
Total number of out of order pairs is: 3


Array is: [2, 4, 1, 3, 5]
(2,1)
(4,1)
(4,3)
Total number of out of order pairs is: 3


Array is: [5, 4, 3, 2, 1]
(5,4)
(5,3)
(5,2)
(5,1)
(4,3)
(4,2)
(4,1)
(3,2)
(3,1)
(2,1)
Total number of out of order pairs is: 10
"""
