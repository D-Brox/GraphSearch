from __future__ import annotations

from methods.Search import Search
from utils.OpenList import Node

class UCS(Search): #Dijkstra
    def __init__(self,cost_map,start,end):
        super().__init__(cost_map,start,end,"UCS")
    
    def search_loop(self) -> Node|None:
        self.openlist.insert(self.start)
        while self.openlist:
            node = self.openlist.pop() # Lowest cost
            if node.coord == self.goal:
                #print(self.expanded)
                return node #Solved
            self.visited.add(node.coord)
            child_nodes = self.cost_map.get_neighbors(*node.coord) # Generate childs
            child_nodes = [n for n in child_nodes if n not in self.visited]
            self.add2open(node,child_nodes) # Add to list handled in OpenList
        return None # Failure
