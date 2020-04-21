#Floyd's Algorithm to find All pairs shortest path
def disp(A):
	for x in range(n):
		print(A[x])
	print("\n")


n=int(input("Enter the number of vertices: "))
W=[[0 for i in range(n)] for j in range(n)]
P=[[0 for i in range(n)] for j in range(n)]
print("Enter the values of the weight matrix. If there is no connection, enter 2000. ")
for i in range(n):
	print("Enter weight matrix row ",i,": ")
	W[i]=[int(j) for j in input().split()]
for i in range(n):
	for j in range(n):
		if W[i][j]==2000:
			P[i][j]=-1

R=W
print("Weight Matrix: ")
disp(R)

#floyd algo
for k in range(n):	
	for i in range(n):
		for j in range(n):
			if R[i][k]+R[k][j]<R[i][j]:
				R[i][j]=R[i][k]+R[k][j]
				P[i][j]=k+1
				print(P[i][j])
	print("R(",k,"): ")
	disp(R)
disp(P)


def path(i,j,pathlist):
    if P[i][j]==0:
        pathlist.append(j+1)
        return
    else:
        path(i,P[i][j]-1,pathlist)
        path(P[i][j]-1,j,pathlist)
for i in range(n):
	for j in range(n):
	    pathlist=[]
	    pathlist.append(i+1)
	    path(i,j,pathlist)
	    print(i+1,' to ',j+1,' ',pathlist)

"""
OUTPUT
Enter the number of vertices: 4
Enter the values of the weight matrix. If there is no connection, enter 2000. 
Enter weight matrix row  0 : 
0 2000 3 2000
Enter weight matrix row  1 : 
2 0 2000 2000
Enter weight matrix row  2 : 
2000 7 0 1
Enter weight matrix row  3 : 
6 2000 2000 0
Weight Matrix: 
[0, 2000, 3, 2000]
[2, 0, 2000, 2000]
[2000, 7, 0, 1]
[6, 2000, 2000, 0]


R( 0 ): 
[0, 2000, 3, 2000]
[2, 0, 5, 2000]
[2000, 7, 0, 1]
[6, 2000, 9, 0]


R( 1 ): 
[0, 2000, 3, 2000]
[2, 0, 5, 2000]
[9, 7, 0, 1]
[6, 2000, 9, 0]


R( 2 ): 
[0, 10, 3, 4]
[2, 0, 5, 6]
[9, 7, 0, 1]
[6, 16, 9, 0]


R( 3 ): 
[0, 10, 3, 4]
[2, 0, 5, 6]
[7, 7, 0, 1]
[6, 16, 9, 0]


"""
