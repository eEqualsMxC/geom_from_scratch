from __future__ import  annotations # Define Error
from point import Point
from typing import List
from typing import Union

class Node:
    def __init__(self, data = None, _next = None):
        self.data = data
        self.next = _next
    def __repr__(self):
        return f"S({self.data}, {self.next})"

class Line:
    def __init__(self, start = None, end = None):
        self.start = start
        self.end = end
        self._items = list(start, end)

    def __repr__(self):
        return f"L({self.start}, {self.end})"

    def add(self, other):
        if isinstance(other, Point):
            slope_1 = self.start.slope(self.end)
            slope_2 = self.end.slope(other)
            if slope_1 == slope_2:
                self._items.append(other)
                self.end = other
        elif isinstance(other, Line):
            slope_1 = self.start.slope(self.end)
            slope_2 = other.start.slope(other.end)
            if slope_1 == slope_2:
                for pnt in other._items:
                    if pnt != other.start:
                        self._items.append(pnt)
    