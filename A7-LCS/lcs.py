def lcs(a,b):
  m=len(a)
  n=len(b)
  l=[[0 for i in range(n+1)] for j in range(m+1)]
  for x in range(m):
    for y in range(n):
      if a[x]==b[y]:
        l[x+1][y+1]=l[x][y]+1
      else:
        l[x+1][y+1]=max(l[x][y+1],l[x+1][y])
  print(l)
  maxele=l[m][n]
  seq=[]
  i=m
  j=n
  while i>0 and j>0:
    if a[i-1]==b[j-1]:
      seq.append(a[i-1])
      maxele=maxele-1
      i-=1
      j-=1
    else:
      if l[i-1][j]<l[i][j-1]:
        j=j-1
      else:
        i=i-1	
  print(seq[::-1])
  return l[m][n]
				
print("Enter the elements in array A: ")
a=[int(i) for i in input().split()]
print("Enter the elements in array B: ")
b=[int(i) for i in input().split()]
print("longest common subsequence length: ",lcs(a,b))
