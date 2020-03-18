from SP import SP
from WeightedDigraph import WeightedDigraph
from DirectedEdge import DirectedEdge
def main():
	e1=DirectedEdge(0,1,1)
	e2=DirectedEdge(1,4,6)
	e3=DirectedEdge(0,2,3)
	e4=DirectedEdge(2,3,4)
	e5=DirectedEdge(2,4,2)
	e6=DirectedEdge(3,4,1)
	e7=DirectedEdge(3,1,5)
	e=[e1,e2,e3,e4,e5,e6,e7]
	g=WeightedDigraph(5)
	g.EdgeWeightedDigraph(e)
	x=SP(g,0)
	x.dijkstraSP()
main()
"""
OUTPUT

shortest path from source  0
Vertex:  0  Distance:  0  Predecessor:  0
Vertex:  1  Distance:  1  Predecessor:  0
Vertex:  2  Distance:  3  Predecessor:  0
Vertex:  4  Distance:  5  Predecessor:  2
Vertex:  3  Distance:  7  Predecessor:  2

"""