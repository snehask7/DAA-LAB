"""1.. Algorithm, ordered insert, should insert the target at its right position in a sorted list and create a new sorted list.
 Implement ordered insert (u, v) as a recursive function. u is an item, and v is a sorted list. The algorithm will have the same 
 outline as linear locate, and differ only in the way the solution is constructed from the subsolution."""

def ordered_insert (u, v):
 	n=len(v)
 	if n==0:
 		v.append(u)
 		return v
 	if n<=1:
 		if u>=v[0]:
 			v.append(u)
 		else:
 			v.insert(0,u)
 		return v
 	mid=int(n/2)
 	if u<v[mid]:
 		return ordered_insert(u,v[0:mid])+v[mid:n]
 	else:
 		return v[0:mid]+ordered_insert(u,v[mid:n])
print("ADD 15 TO [5, 10, 20, 35, 50] RESULT: ",ordered_insert (15, [5, 10, 20, 35, 50]))
print("ADD 2 TO [5, 10, 20, 35, 50] RESULT: ",ordered_insert (2, [5, 10, 20, 35, 50]))
print("ADD 25 TO [] RESULT: ",ordered_insert (25, []))
print("ADD 35 TO [5, 10, 20, 35, 50] RESULT: ",ordered_insert (35, [5, 10, 20, 35, 50]))

"""
OUTPUT

ADD 15 TO [5, 10, 20, 35, 50] RESULT:  [5, 10, 15, 20, 35, 50]
ADD 2 TO [5, 10, 20, 35, 50] RESULT:  [2, 5, 10, 20, 35, 50]
ADD 25 TO [] RESULT:  [25]
ADD 35 TO [5, 10, 20, 35, 50] RESULT:  [5, 10, 20, 35, 35, 50]
"""