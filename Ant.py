import random
import sys
class Ant:
  def __init__(self, start, end, alpha, betha ):
    self.visits = []
    self.start = start
    self.current = start
    self.end = end 
    self.iteration = 0
    self.betha = betha
    self.alpha = alpha
    self.solution = []
    self.notSolution = False


  def moveAnt(self, edge):
    if not edge is None:
      self.visits.append(edge)
      self.solution.append(edge)
      self.current = edge.getEndNode()


  def bestPossibility(self):
    
    if self.iteration == 0:
      r = random.choice(self.current.getEdges())
      while r in self.visits:
        r = random.choice(self.current.getEdges())
      self.moveAnt(r)
    else:
      possibilities = [] 
      
      for edge in self.current.getEdges():
        if not edge in self.visits:
          num = ( 1/edge.getCost() ** self.betha ) * ( edge.getPheromone() ** self.alpha)
          den = 0
          for edgex in self.current.getEdges():
            if not edgex in self.visits:
              den += ( 1/edge.getCost() ** self.betha ) * ( edge.getPheromone() ** self.alpha)
          
          possibilities.append({ 'edge': edge, 'p': num/den })
        

      bestPossibility = None
      for possibility in possibilities:
          if bestPossibility is None:
            bestPossibility = possibility
          else:
            if possibility['p'] > bestPossibility['p']:
              bestPossibility = possibility
        
      if bestPossibility != None:
        self.moveAnt(bestPossibility['edge'])
      else:
        self.notSolution = True
        self.solution = []

    

  def searchSolution(self):
    self.solution = []
    self.current = self.start
    self.notSolution = False
    while self.current.getNode() != self.end.getNode() and self.notSolution == False:
      self.bestPossibility()
    self.showSolution();

    self.iteration += 1;
    
    
  def showSolution(self):
    if self.notSolution == False:
      print(self.start.getNode(), end=" ")
      for edge in self.solution:
        print(edge.getEndNode().getNode(), end=" ")
      print(self.getCostSolution(), end=" ")
      print(" ")

  def getCostSolution(self):
    totalCost = 0
    for edge in self.solution:
      totalCost += edge.getCost()
    return totalCost

  def getSolution(self):
    return self.solution

  def getVisitis(self):
    return self.visits
  
  def showVisits(self):
    print(self.start.getNode(), end=" ")
    for edge in self.visits:
      print(edge.getEndNode().getNode(), end=" ")
    print(self.getCostSolution(), end=" ")
    print(" ")
  
  def getStart(self):
    return self.start