from DirectedEdge import DirectedEdge
from Union_Find import Union_Find
class Kruskal(object):
	def __init__(self,n,e):# n is num of vertices, e is set of edges
		self.v=n
		for i in range(len(e)):#sorts the edges in ascending order of weight
			for j in range(len(e)-i-1):
				if e[j].weightv()>e[j+1].weightv():
					e[j],e[j+1]=e[j+1],e[j]
		# for x in e:
		# 	print(x.weightv())
		self.edges=e
	def kruskalsalgo(self):
		count=0
		k=0
		cost=0
		mst=[]
		u=Union_Find(self.v)
		while count!=self.v-1:
			#print(self.edges[k].fromv(),",",self.edges[k].tov(),u.find(self.edges[k].fromv()),u.find(self.edges[k].tov()))
			if u.find(self.edges[k].fromv())!=u.find(self.edges[k].tov()):#checks if no cycle
				u.Union(u.find(self.edges[k].fromv()),u.find(self.edges[k].tov()))
				count+=1
				mst.append(self.edges[k])
				cost+=self.edges[k].weightv()
				
			k+=1
		print("Edges in the minimum cost spanning tree are:")
		for x in mst:
			print(x.fromv(),x.tov())
		print("Total cost is: ",cost)
