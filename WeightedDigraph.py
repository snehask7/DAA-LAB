from DirectedEdge import DirectedEdge
class WeightedDigraph(object):#creates the graph
	def __init__(self,n):
		self.n=n
		self.adjmat=[[100000 for i in range(n)] for i in range(n)]
		for i in range(n):
			self.adjmat[i][i]=0
	def EdgeWeightedDigraph(self,data):#populates edges
		for x in data:
			self.adjmat[x.fromv()][x.tov()]=x.weightv()
	def V(self):#returns no of vertices
		return self.n
	def E(self):#returns no of edges
		edgecount=0
		for i in range(self.n):
			for j in range(self.n):
				if self.adjmat[i][j]!=100000:
					edgecount+=1
		return edgecount
	def add_edge(self,e):#adds an edge tov digraph
		self.adjmat[e.fromv()][e.tov()]=e.weightv()
	def adj(self,v):#returns all edges adjecent tov vertex v as a list
		edgelist=[]

		for j in range(self.n):
			if self.adjmat[v][j]!=100000:
				edgelist.append(DirectedEdge(v,j,self.adjmat[v][j]))
		for j in range(self.n):
			if self.adjmat[j][v]!=100000:
				edgelist.append(DirectedEdge(j,v,self.adjmat[j][v]))
		return edgelist
	def edges(self):#returns all edges in the digraph as a list
		alledgelist=[]
		for i in range(self.n):
			for j in range(self.n):
				if self.adjmat[i][j]!=100000:
					alledgelist.append(DirectedEdge(i,j,self.adjmat[i][j]))
		return alledgelist