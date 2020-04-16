#Warshall's Algorithm to find the transitive closure from the adjacency matrix
def disp():
	for x in range(n):
		print(R[x])
	print("\n")


n=int(input("Enter the number of vertices: "))
A=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
	print("Enter adjacency matrix row ",i,": ")
	A[i]=[int(j) for j in input().split()]
R=A
print("adjacency Matrix: ")
disp()

#warshall algo
for k in range(n):	
	for i in range(n):
		for j in range(n):
			if R[i][k]==1 and R[k][j]==1:
				R[i][j]=1
	print("R(",k,"): ")
	disp()



"""
OUTPUT
Enter the number of vertices: 4
Enter adjacency matrix row  0 : 
0 1 0 0
Enter adjacency matrix row  1 : 
0 0 0 1
Enter adjacency matrix row  2 : 
0 0 0 0
Enter adjacency matrix row  3 : 
1 0 1 0
adjacency Matrix: 
[0, 1, 0, 0]
[0, 0, 0, 1]
[0, 0, 0, 0]
[1, 0, 1, 0]


R( 0 ): 
[0, 1, 0, 0]
[0, 0, 0, 1]
[0, 0, 0, 0]
[1, 1, 1, 0]


R( 1 ): 
[0, 1, 0, 1]
[0, 0, 0, 1]
[0, 0, 0, 0]
[1, 1, 1, 1]


R( 2 ): 
[0, 1, 0, 1]
[0, 0, 0, 1]
[0, 0, 0, 0]
[1, 1, 1, 1]


R( 3 ): 
[1, 1, 1, 1]
[1, 1, 1, 1]
[0, 0, 0, 0]
[1, 1, 1, 1]

"""

