""" Operation merge takes two sorted lists as arguments and results in a sorted list of all the items
in the argument lists. Let us denote prepend by the operator : and merge by the operator
++ (it is not a standard notation – we use it in this lecture only). Then
[2,3,8,9] ++ [1,4,5,7] = [1,2,3,4,5,7,8,9]"""
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
print("MERGING OF [2,3,8,9],[1,4,5,7] RESULT: ",merge([2,3,8,9],[1,4,5,7]))
print("MERGING OF [8,13,17,19],[1,4,5,7] RESULT: ",merge([8,13,17,19],[1,4,5,7]))

"""
OUTPUT

MERGING OF [2,3,8,9],[1,4,5,7] RESULT:  [1, 2, 3, 4, 5, 7, 8, 9]
MERGING OF [8,13,17,19],[1,4,5,7] RESULT:  [1, 4, 5, 7, 8, 13, 17, 19]
"""