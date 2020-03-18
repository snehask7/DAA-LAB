"""1. Suppose we want to find the bolt that matches a particular nut. We can test the nut with
every bolt until we find the matching bolt. We have test the nut with n − 1 bolts. If none
of the n − 1 bolts matches the nut, the nth bolt is the match for the nut. Therefore, this
takes n − 1 tests. Using this idea, design a brute-force algorithm with O(n 2 ) operations
that associates each nut with the corresponding bolt. Implement the algorithm."""

def match(nuts,bolts):
	for i in range(len(nuts)):
		found=0
		for j in range(len(bolts)-1):
			if nuts[i]==bolts[j]:
				found=1
				print("Nut: ",i," Matches with Bolt: ",j)
				break
		if found==0:
			print("Nut: ",i," Matches with Bolt: ",len(bolts)-1)
			

n=int(input("Enter the number of nut and bolt pairs: "))
print("Enter the sizes of nuts: ")
nuts=[int(i) for i in input().split()]
print("Enter the sizes of bolts: ")
bolts=[int(i) for i in input().split()]
match(nuts,bolts)

"""
OUTPUT
Enter the number of nut and bolt pairs: 5
Enter the sizes of nuts: 
5 4 3 2 1
Enter the sizes of bolts: 
3 4 1 2 5
Nut:  0  Matches with Bolt:  4
Nut:  1  Matches with Bolt:  1
Nut:  2  Matches with Bolt:  0
Nut:  3  Matches with Bolt:  3
Nut:  4  Matches with Bolt:  2
"""
