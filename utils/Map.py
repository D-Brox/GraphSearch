from __future__ import annotations
from dataclasses import dataclass

import numpy as np

cost_dict = {
    ".":1.0,
    ";":1.5,
    "+":2.5,
    "x":6.0,
    "@":np.inf
}

@dataclass
class Map():
    width: int
    height: int
    total: int
    map: np.array

    @staticmethod
    def gen_map(mapfile) -> Map:
            with open(mapfile,'r') as f:
                txt = f.readlines()
            
            dim = txt.pop(0).split()
            width = int(dim[0])
            height = int(dim[1])
            total = width*height
            txt = [l.replace(" ","").replace("\n","") for l in txt]
            map = np.array([[cost_dict[r] for r in l] for l in txt ]).transpose()

            return Map(width,height,total,map)

    def get_neighbors(self,x:int,y:int) -> list:
        l = max(0, x-1)
        r = min(self.width-1,x+1)
        t = max(0, y-1)
        b = min(self.height-1,y+1)
        candidates = [[r,y],[x,t],[l,y],[x,b]]
        return [tuple(c) for c in candidates if c!=[x,y]]
