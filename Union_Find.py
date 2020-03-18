class Union_Find(object):
	def __init__(self,n):#n is total number of vertices
		self.parent=[-1 for i in range(n)]
	def find(self,e):#find out which set a vertex belongs to 
		s1=self.parent[e]
		if s1<0:
			return e
		else:
			while self.parent[s1]>=0:
				s1=self.parent[s1]
			return s1
	def Union(self,b1,b2):#if vertices of an edge belong to 2 sets, perform union of those edges. If vertices belong to same set, the cycle
		if abs(self.parent[b1])>=abs(self.parent[b2]) :
			self.parent[b1]=self.parent[b1]+self.parent[b2]
			self.parent[b2]=b1
		else:
			self.parent[b2]=self.parent[b1]+self.parent[b2]
			self.parent[b1]=b2
		#print(self.parent)