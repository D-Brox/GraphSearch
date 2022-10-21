from __future__ import annotations
from methods.Search import Search
from utils.OpenList import Node

class BFS(Search):
    def __init__(self,cost_map,start,end):
        super().__init__(cost_map,start,end,"BFS")
    
    def search_loop(self) -> Node|None:
        self.openlist.insert(self.start)
        while self.openlist:
            node = self.openlist.pop() # Shallowest
            if node.coord == self.goal:
                #print(self.expanded)
                return node
            self.visited.add(node.coord)
            child_nodes = self.cost_map.get_neighbors(*node.coord) # Generate childs
            child_nodes = [n for n in child_nodes if n not in self.visited]
            self.add2open(node,child_nodes) # Add to list handled in OpenList
        return None