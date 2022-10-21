from __future__ import annotations

from methods.Search import Search
from utils.Node import Node, is_not_cycle
from utils.OpenList import OpenList
from utils.VisitedList import VisitedList


class IDS(Search):
    def __init__(self, cost_map, start, end):
        super().__init__(cost_map, start, end, "IDS")
        self.max_depth = 0
        self.max_open = 0

    def search_loop(self) -> Node | None:
        self.start.heuristic = self.heuristic(self.start.coord)
        self.openlist.insert(self.start)
        # tq = tqdm(total=512)

        while True:
            #print(self.max_depth)
            solution=None
            while self.openlist:
                node = self.openlist.pop()
                if node.coord == self.goal:
                    if solution is None:
                        solution = node
                    elif node.real_cost < solution.real_cost:
                        solution = node
                    
                if node.depth == self.max_depth or not is_not_cycle(node):
                    continue
                child_nodes = self.cost_map.get_neighbors(*node.coord)
                child_nodes = [n for n in child_nodes if n not in self.visited]
                self.add2open(node, child_nodes)

            if solution:
                break

            self.max_depth += 1
            self.reset()
        #print(self.expanded)
        return solution

    def reset(self) -> None:
        self.visited = VisitedList()
        self.openlist = OpenList(self.method)
        self.openlist.insert(self.start)
