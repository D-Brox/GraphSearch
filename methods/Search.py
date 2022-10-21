from __future__ import annotations
from abc import ABC, abstractmethod

import numpy as np

from utils.Map import Map
from utils.Node import Node
from utils.OpenList import OpenList
from utils.VisitedList import VisitedList


class Search(ABC):
    def __init__(self,cost_map:Map,start:tuple,end:tuple,method:str):
        self.method = method

        self.cost_map = cost_map
        self.start = Node(start,0,0,0,None)
        self.goal = end
        
        self.visited = VisitedList()
        self.openlist = OpenList(method)
        self.expanded = 0

    def run(self):
        node = self.search_loop()
        if not node:
            print("No path available")
            return
        cost = node.real_cost
        path = []
        while node != None:
            path.insert(0,node.coord)
            node = node.parent
        print(cost,*path)

    @abstractmethod
    def search_loop(self) -> Node:
        return

    def heuristic(self,coord):
        return 0
    
    def reset(self) -> None:
        return

    def add2open(self, parent, children):
        self.expanded +=1
        for coord in children:
            node_cost = self.cost_map.map[coord]
            if node_cost == np.inf:
                self.visited.add(coord)
                continue
            if self.method == "Greedy" and coord in self.visited:
                continue
            depth = parent.depth + 1
            heuristic = self.heuristic(coord)
            real_cost = node_cost+parent.real_cost
            n = Node(coord,real_cost,heuristic,depth,parent)
            self.openlist.insert(n)

