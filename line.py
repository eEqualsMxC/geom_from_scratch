from __future__ import  annotations # Define Error
from point import Point
from pre_calculus import sine
from typing import Union
from typing import List


class Joint:
    """
    A Joint object is similar describes a line object when it's
    slope changes.
                
                   | < -- Line A
                   |
                   |
                   0 <--Joint of Lines A, B, C             
                 /   \   
                /     \  <--   Line C
    Line B --> /       \       
              /         \     / <-- Line D    
                         \   /
                          \ /         
    Joint of Lines C, D--> 0 --------------  <--Line E
    
    A joint can be connected to infinite lines,
    but a can not loop to itself.
    Therfore, Joint(A, B, C, D) is valid.
    When Joint(A, B, C, D, A) is init, the Shape class __init__'s 
    with inheritance of the Point and Line Classes.

    Joint objects are indexed by their start or ending points 
    of a line. Joint[A.start, B.start, C.start, D.start, E.start] 
    The returned joint class is sorted into a k-d tree.  
    """
    def __init__(self, lines: List[Line]) --> List[Joint]:
        self._items_joints = list()
        self.lines = lines
        pass

    def __repr__(self):
        return f"L{self.start}, {self.end}"
    def __len__(self):
        return len(self._items)
    def __iter__(self):
        return iter(self._items)
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, item):
        self._items[index] = item 

class Line:
    """
    A line class that will have simliar characteristics as a Queue and Array Class.
    The line class requires at least two Point objects and points are read left 
    to right.
    """
    def __init__(self, start = None, end = None) -> Line:
        if isinstance(start, Point) and isinstance(end, Point):
            self._items = list()
            self._items.append(start)
            self._items.append(end)
            self.start = start
            self.end = end
    def __repr__(self):
        return f"L{self.start}, {self.end}"
    def __len__(self):
        return len(self._items)
    def __iter__(self):
        return iter(self._items)
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, item):
        self._items[index] = item 
    @property
    def line_slope(self) -> float:
        return self.start.slope(self.end)
    @property
    def midpoint(self) -> Point:
        return self.start.midpoint(self.end)
    @property
    def length(self) -> float:
        return self.start.distance(self.end)
    @property
    def y_intercept(self) -> float:
        return self.start.y_intercept(self.end)
    @property
    def third_point(self) -> float:
        return Point(self.end.x, self.start.y)
    @property
    def rise(self) -> float:
        return self.end.y - self.start.y
    @property
    def run(self) -> float:
        return self.end.x - self.start.x
    @property
    def get_points(self) -> list:
        """Return all coordinates as tuple"""
        # temp = [Point(pnt.x, pnt.y) for pnt in self._items[:]]
        return iter(self._items)
    
    def slope_precision(self, other: Union[Line,Point], precision: float = 0.0001 ) -> bool:
        """
        Returns True or False if the slope of two lines are with in float precision
        or if a point exists in the slope of a line.
        The default precision is a float value with in 0.0001  
        """
        if isinstance(other, Line):
            slope_1, slope_2 = self.line_slope, other.line_slope
            return precision > (slope_1 - slope_2)
        elif isinstance(other, Point):
            slope_1, slope_2 = self.line_slope, self.end.slope(other)
            return precision > (slope_1 - slope_2)
        else:
            return NotImplemented

    def add(self, other: Union[Point, float], precision: float = 0.001) -> None:
        if isinstance(other, Point):
            if self.slope_precision(other, precision):     # Default precion of slopes is caculated to 10000's decimal place
                self._items.append(other)
                self.end = other
            else:
                return -1                                   # If not in the same slope, then return a new class object as a Line Segment.
        if isinstance(other, int):
            other = float(other)
        elif isinstance(other, float):
            soh_1 = self.end.distance(self.third_point) / self.length                          
            hp_2 = hp_1 + other                         
            op_2 = soh_1 * hp_2                             # Using pathagorem, calculate the adjacent leg 
            adj_2 = (((hp_2 ** 2) - (op_2 ** 2))) ** 0.5    # as c^2 - b^2 = a^2

            x_coor = self.start.x + adj_2                   # From the starting point, add the lengths of the 
            y_coor = self.start.y + op_2                    # new legs inorder to calculate the new point
            point_location = Point(x_coor, y_coor)

            self.add(point_location)
        elif isinstance(other, Line):                       # Add two lines togther will return a line with # Greater distance or a new line segment object. 
            if other.start != self.end:
                if self.slope_precision(other):
                    for pnt in other._items:
                        self._items.append(pnt)
                        self.end = other.end
                else:
                    pass                                   # Return a Line segment object
            elif other.start == self.end:
                if self.slope_precision(other):
                    for pnt in other._items[1:]:
                        self._items.append(pnt)
                        self.end = other.end

                else:                                      # Return a Line segment object
                    pass                                   
            else:
                return NotImplemented
        else:
            raise TypeError                                # Object is not a point or line.


