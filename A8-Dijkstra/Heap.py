
class Heap(object):
	def __init__(self,size):
		self.max=size
		self.size=0
		self.A=[[0,0] for i in range(size+1)]
		self.A[0]=[-100,-100]

	def insert(self,i,k):
		self.size+=1
		self.A[self.size]=[i,k]
		j=self.size
		while j!=0 and self.A[j//2][1]>self.A[j][1]:#percolate up, checking if parent key is greater. if greater thrn swap
			temp=self.A[j]
			self.A[j]=self.A[j//2]
			self.A[j//2]=temp
			j=j//2
		self.A[j]=[i,k]
	def getDist(self,v):
		for i in range(1,self.size+1):
			if self.A[i][0]==v:
				return self.A[i][1]
				break
		return 1000000
	def DeleteMin(self):
		minelement=self.A[1]
		leafelement=self.A[self.size]
		self.A[1]=leafelement
		self.size=self.size-1
		i=1
		while i*2<=self.size:
			child=i*2
			if self.A[child+1][1]<self.A[child][1]:#right child left child comparison
				child+=1
			if leafelement[1]>self.A[child][1]:
				self.A[i]=self.A[child];
			else:
				break
			i=child
		self.A[i]=leafelement
		return minelement


	def  DecreaseKey(self,x, k) :#Updates the key of item x to k.
		i=0
		for i in range(1,self.size+1):
			if self.A[i][0]==x:
				self.A[i][1]=k
				break
		j=i
		while j!=0 and self.A[j//2][1]>self.A[j][1]:#percolate up, checking if parent key is greater. if greater thrn swap
			temp=self.A[j]
			self.A[j]=self.A[j//2]
			self.A[j//2]=temp
			j=j//2
		self.A[j]=[x,k]

	def printheap(self,i,tab):
		for j in range(tab):
			print("\t",end='')
		print(self.A[i])
		if i*2<=self.size:
			self.printheap(i*2,tab+1)
		if (i*2)+1<=self.size:
			self.printheap((i*2)+1,tab+1)
