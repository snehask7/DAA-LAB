"""
Session 7: Greedy Algorithms
Kruskal’s Algorithm
Name:Sneha Sriram Kannan
Reg No: 185001157
"""
from DirectedEdge import DirectedEdge
from Kruskal import Kruskal
def main():
	n=9
	e1=DirectedEdge(0,1,4)
	e2=DirectedEdge(1,2,8)
	e3=DirectedEdge(2,3,7)
	e4=DirectedEdge(3,4,9)
	e5=DirectedEdge(4,5,10)
	e6=DirectedEdge(3,5,14)
	e7=DirectedEdge(2,5,4)
	e8=DirectedEdge(5,6,2)
	e9=DirectedEdge(6,7,1)
	e10=DirectedEdge(7,0,8)
	e11=DirectedEdge(7,1,11)
	e12=DirectedEdge(7,8,7)
	e13=DirectedEdge(6,8,6)
	e14=DirectedEdge(2,8,2)
	e=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]
	k=Kruskal(n,e)
	k.kruskalsalgo()
main()