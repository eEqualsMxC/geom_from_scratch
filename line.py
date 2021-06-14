from __future__ import  annotations # Define Error
from point import Point
from typing import List
from typing import Union



class Line(Point):
    """ 
    Represents a line that contains more than one Point object.
    A slope is initialized from the start point and end point.
    A Line can accept a point or containe a neighboring line.
    A Line will containe points or other lines 
    """
    def __init__(self, points: Point = List[Point]) -> Line:

        if isinstance(points, list) and is_point(points): # Contains a list of points
            self._items = list()
            for pnt in points:
                self._items.append(pnt)
        else:
            raise TypeError
    def __len__(self) -> int:
        return len(self._items)
    def __str__(self) -> str:
        return str(self._items)
    def __iter__(self):
        return iter(self.items)
    def __getitem__(self, index) -> Union(List[Point], Point):
        return self._items(index)
    def __setitem__(self, index, item) -> None:
        if isinstance(item, Point) or isinstance(item, Line):
            if isinstance(item, Line) and is_point(item):
                self._items[index] = item
            else:
                raise TypeError
        else:
            self._items[index] = item
         
def is_point(points_list: List[Point], all_points=True) -> bool:
    """Check container for Point objects"""
    for _point in points_list:
        if isinstance(_point, Line):
            is_point(_point, all_points)
        elif isinstance(_point, Point):
            continue
        else:
            all_points = False
            break
    return all_points

