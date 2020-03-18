"""4. Design an improved version (time complexity should be less) using any of the design techniques discussed so far. Implement the algorithm in Python."""
#time complexity nlogn
count=0
def oop(a):
	if len(a)==1:
		return a
	mid=int(len(a)/2)
	return mergesort(oop(a[:mid]),oop(a[mid:]))

def mergesort(a,b):
	global count
	temp=[0 for i in range(len(a)+len(b))]
	i=0
	j=0
	k=0
	while i!=len(a) and j!=len(b):
		if a[i]<=b[j]:
			temp[k]=a[i]
			k+=1
			i+=1
		else:
			temp [k]=b[j]
			k+=1
			j+=1
			count+=len(a)-i
	while i!=len(a):
		temp[k]=a[i]
		i+=1
		k+=1
	while j!=len(b):
		temp[k]=b[j]
		j+=1
		k+=1
	return temp

print("Array is: [1, 2, 3, 4, 5]")
oop([1, 2, 3, 4, 5])
print("Total number of out of order pairs is: ",count)
print("\n")
count=0
print("Array is: [3, 1, 2, 5, 4]")
oop([3, 1, 2, 5, 4])
print("Total  number of out of order pairs is: ",count) 
print("\n")
count=0
print("Array is: [2, 4, 1, 3, 5]")
oop([2, 4, 1, 3, 5])
print("Total number of out of order pairs is: ",count) 
print("\n")
count=0
print("Array is: [5, 4, 3, 2, 1]")
oop([5, 4, 3, 2, 1])
print("Total number of out of order pairs is: ",count) 

"""
OUTPUT
Array is: [1, 2, 3, 4, 5]
Total number of out of order pairs is:  0


Array is: [3, 1, 2, 5, 4]
Total  number of out of order pairs is:  3


Array is: [2, 4, 1, 3, 5]
Total number of out of order pairs is:  3


Array is: [5, 4, 3, 2, 1]
Total number of out of order pairs is:  10
"""

