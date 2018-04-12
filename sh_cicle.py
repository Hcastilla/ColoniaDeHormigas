import json
from Node import * 
from Edge import * 
from System import *

system = System()

with open("data.json") as jsonData:

  data = json.load(jsonData)

  system.setPheromeneEvaporation(data['pheromoneEvaporation'])
  system.setAlpha(data['alpha'])
  system.setBetha(data['betha'])
  system.setQ(data['q'])

  for node in data['nodes']:
    system.setNode(Node(node))

  for edge in data['edges']:
    startNode = ''
    endNode = ''
    for node in system.getNodes():
      if edge['start'] == node.getNode():
        startNode = node
      if edge['end'] == node.getNode():
        endNode = node

    startNode.setEdge(Edge(startNode, endNode, edge['cost'], data['pheromone']))

  jsonData.close()



for i  in range(0, 100):
  
  for x in range(0, 5):
    system.createAnt("a", "d")
  
  for ant in system.getAnts():
    ant.searchSolution()

  system.evaporathePheromones()
  system.updatePheromones()
  system.searchBestSolution()


system.printData()
system.showSolution()