'''Test 5:

1.	Create a directed graph having at least 8 edges using python. (12th week).
2.	Print the vertices and edges of this graph. (12th week).
'''

edges=[("A","B"),("A","C"),("B","C"),("B","D"),("B","E"),("C","D"),("D","E"),("E","F"),("F","E")]
class Graph:
  def __init__(self,Nodes,is_directed=False):
    self.nodes=Nodes
    self.adjlist={}
    self.is_directed=is_directed
    
    for node in self.nodes:
      self.adjlist[node]=[]
      
      
  def addedges(self,v,e):
    self.adjlist[v].append(e)
    if not self.is_directed:
          self.adjlist[e].append(v)
    
  
  def print_adjlist(self):
    for node in self.nodes:
      print(node,": ",self.adjlist[node])
    
        
      
nodes=["A","B","C","D","E","F"]
graph=Graph(nodes,is_directed=True)
print("\n")
for v,e in edges:
  graph.addedges(v,e)
  print("Edge: ",(v,e))
  
print("\n")
for v in nodes:
   print("vertex: ",v)   
  
  
print("\nGraph is: ")
graph.print_adjlist()
print("\n")