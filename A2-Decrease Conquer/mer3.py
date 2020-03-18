"""
3. Implement mergesort using function merge.
Algorithm: MergeSort (a)
Input: a is a list of comparable items.
Output: A sorted list of items in a.
"""
def merge(u,v):
	temp=[]
	while len(u)!=0 and len(v)!=0:
		if u[0]<v[0]:
			temp.append(u[0])
			u.remove(u[0])
		else:
			temp.append(v[0])
			v.remove(v[0])
	if len(u)!=0:
		temp=temp+u
	elif len(v)!=0:
		temp=temp+v
	return temp

def MergeSort(a):
	if len(a)==0 or len(a)==1:
		return a
	m=int(len(a)/2)
	return merge(MergeSort(a[:m]),MergeSort(a[m:]))

print("INPUT: [7,4,5,1,10,99,2,3] RESULT: ",MergeSort([7,4,5,1,10,99,2,3]))
print("INPUT: [15, 93, 45,5, 10, 20, 35, 1] RESULT: ",MergeSort([15, 93, 45,5, 10, 20, 35, 1]))
print("INPUT: [45,1,1002,34,1,3,3,44,2] RESULT: ",MergeSort([45,1,1002,34,1,3,3,44,2]))

"""

OUTPUT

INPUT: [7,4,5,1,10,99,2,3] RESULT:  [1, 2, 3, 4, 5, 7, 10, 99]
INPUT: [15, 93, 45,5, 10, 20, 35, 1] RESULT:  [1, 5, 10, 15, 20, 35, 45, 93]
INPUT: [45,1,1002,34,1,3,3,44,2] RESULT:  [1, 1, 2, 3, 3, 34, 44, 45, 1002]
"""