#Warshall's Algorithm to find the transitive closure from the adjacency matrix
def disp():
	for x in range(n):
		print(R[x])
n=int(input("Enter the number of vertices: "))
A=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
	print("Enter adjacency matrix row ",i,": ")
	A[i]=[int(j) for j in input().split()]
R=A
print("adjacency Matrix: ")
disp()
for k in range(n):	
	for i in range(n):
		for j in range(n):
			if R[i][k]==1 and R[k][j]==1:
				R[i][j]=1
	print("R(",k,"): ")
	disp()


