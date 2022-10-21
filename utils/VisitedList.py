from __future__ import annotations

class VisitedList(set):
    """Wraps set to allow lists"""
    def add(self,__o:list|tuple):
        if isinstance(__o,list):
            __o = tuple(__o)
        super(VisitedList,self).add(__o)

    def __contains__(self, __o: object) -> bool:
        if isinstance(__o,list):
            __o = tuple(__o)
        return super().__contains__(__o)