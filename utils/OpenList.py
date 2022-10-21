from __future__ import annotations

from bisect import bisect

from .Node import Node, NodeListWrapper

class OpenList:
    def __init__(self, method):
        self.method = method
        self._list = [] # Ordered list
        self._dict = {} # Index dict
    
    def pop(self) -> Node:
        n = self._list.pop(0)
        if self.method in  ["A*", "UCS"]:
            del self._dict[n.coord]
            self._dict = {k:v-1 for k,v in self._dict.items()}
        return n

    def insert(self, __n: Node) -> None:
        if self.method == "Greedy":
            key = lambda n: n.heuristic
            idx = bisect(NodeListWrapper(self._list, key), key(__n))
            self._list.insert(idx,__n)
            self._dict[__n.coord] = None
            return
        elif self.method == "BFS":
            if __n.coord not in self._dict:
                self._list.append(__n)
                self._dict[__n.coord] = None
            return
        elif self.method == "IDS":
            if __n.coord not in self._dict:
                self._dict[__n.coord] = None    
                self._list.insert(0,__n)
            return
        elif self.method == "A*":
            key = lambda n: n.real_cost + n.heuristic
        elif self.method == "UCS":
            key = lambda n: n.real_cost
        
        if __n.coord in self._dict: # A*, UCS and IDS
                old_idx = self._dict[__n.coord]
                old_node = self._list[old_idx]
                if __n.real_cost < old_node.real_cost:  # Replace if needed
                    self._list.pop(old_idx)
                    del self._dict[__n.coord]
                    self._dict = {k:v if v < old_idx else v-1 for k,v in self._dict.items()}
                else:
                    return

        idx = bisect(NodeListWrapper(self._list, key), key(__n))
        self._list.insert(idx, __n)
        self._dict = {k:v if v < idx else v+1 for k,v in self._dict.items()}
        self._dict[__n.coord] = idx

    def __contains__(self, __n: Node) -> bool:
        return __n.coord in self._dict

    def __iter__(self):
        return self._list.__iter__()

    def __str__(self) -> str:
        return self._list.__str__()
    
    def __len__(self) -> int:
        return self._list.__len__()

    def __bool__(self) -> bool:
        return self._list.__len__() != 0

    def __repr__(self) -> str:
        return f"OpenList({self.method}, {self._list.__repr__()})"
