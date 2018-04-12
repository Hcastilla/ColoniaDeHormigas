from Ant import *
import copy

class System:
  def __init__(self):
    self.nodes = []
    self.ants = []
    self.pheromoneEvaporation = 0
    self.betha = 0
    self.alpha = 0
    self.q = 0
    self.bestSolution = None

  def printData(self):
    for node in self.nodes:
      for edge in node.getEdges():
        print(node.getNode(), edge.getEndNode().getNode(), edge.getCost(), " |-| ", edge.getPheromone())

  def setNode(self, node):
    self.nodes.append(node)
  
  def getNodes(self):
    return self.nodes

  def searchNode(self, stringNode):
    for node in self.nodes:
      if node.getNode() == stringNode:
        return node
  
  def createAnt(self, stringStart, stringEnd):
    ant = Ant(self.searchNode(stringStart), self.searchNode(stringEnd), self.alpha, self.betha)
    self.ants.append(ant)
    
  def getAnts(self):
    return self.ants

  def setPheromeneEvaporation(self, pheromoneEvaporation):
    self.pheromoneEvaporation = pheromoneEvaporation
  
  def setBetha(self, betha):
    self.betha = betha

  def setAlpha(self, alpha):
    self.alpha = alpha

  def setQ(self, q):
    self.q = q

  def evaporathePheromones(self):
    for ant in self.ants:
      for v in ant.getVisitis():
        c = v.getPheromone() * (1 - self.pheromoneEvaporation)
        v.setPheromone(c)

  def evaporathePheromones2(self):
    for node in self.nodes:
      for v in node.getEdges():
        c = v.getPheromone() * (1 - self.pheromoneEvaporation)
        v.setPheromone(c)
  
  def updatePheromones(self):
    for ant in self.ants:
      for edge in ant.getSolution():
        drij = 0
        for antx in self.ants:
          for edgex in antx.getSolution():
            if edge == edgex:
              drij += self.q / antx.getCostSolution()
              #print(edgex.getStartNode().getNode(), edgex.getEndNode().getNode(), self.q, '/', antx.getCostSolution())
        edge.setPheromone( (1 - self.pheromoneEvaporation ) * edge.getPheromone() + drij)      

  def searchBestSolution(self):
    for ant in self.ants:
      if len(ant.getSolution()) > 0:
        if self.bestSolution == None:
          self.bestSolution = ant
        else:
          if self.bestSolution.getCostSolution() > ant.getCostSolution():
            self.bestSolution = copy.copy(ant)
    

  def showSolution(self):
    self.bestSolution.showSolution()

