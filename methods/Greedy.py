from __future__ import annotations

from methods.Search import Search
from utils.OpenList import Node

class Greedy(Search):
    def __init__(self,cost_map,start,end):
        super().__init__(cost_map,start,end,"Greedy")
        self.start.heuristic = self.heuristic(self.start.coord)
    
    def search_loop(self) -> Node|None:
        self.openlist.insert(self.start)
        while self.openlist:
            node = self.openlist.pop() # Lowest Heuristic
            if node.coord == self.goal:
                #print(self.expanded)
                return node
            self.visited.add(node.coord)
            child_nodes = self.cost_map.get_neighbors(*node.coord) # Generate childs
            child_nodes = [n for n in child_nodes if n not in self.visited]
            self.add2open(node,child_nodes) # Add to list handled in OpenList
        return None

    def heuristic(self, coord) -> float:
        return sum(abs(c-g) for c,g in zip(coord,self.goal))
