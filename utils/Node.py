from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Node:
    coord: tuple[int,int]
    real_cost: float
    heuristic: float
    depth: int
    parent: Node|None

# https://stackoverflow.com/a/39501468
class NodeListWrapper():
    """Wraps Node for bisect comparison given key"""
    def __init__(self,it:list,key):
        self._it = it
        self._key = key
    
    def __getitem__(self,idx):
        return self._key(self._it[idx])
    
    def __len__(self):
        return self._it.__len__()
    
    def insert(self,idx,__n:Node):
        self._it.insert(idx,__n)

def is_not_cycle(__n:Node):
    ancestor = __n.parent
    while ancestor != None:
        if ancestor.coord == __n.coord:
            return False
        ancestor = ancestor.parent
    return True

