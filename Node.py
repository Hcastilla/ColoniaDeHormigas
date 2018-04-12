class Node:
  def __init__(self, node):
    self.node = node
    self.edges = []

  def getNode(self):
    return self.node

  def setEdge(self, edge):
    self.edges.append(edge)
  
  def getEdges(self):
    return self.edges
