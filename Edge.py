class Edge:
  def __init__(self, start, end, cost, pheromone):
    self.start = start
    self.end = end
    self.cost = cost
    self.pheromone = pheromone

  def getStartNode(self):
    return self.start

  def getCost(self):
    return self.cost
    
  def getPheromone(self):
    return self.pheromone
  
  def getEndNode(self):
    return self.end
  
  def setPheromone(self, pheromone):
    self.pheromone = pheromone