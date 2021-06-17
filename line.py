from __future__ import  annotations # Define Error
from point import Point
from typing import Union

class Line:
    def __init__(self, start = None, end = None) -> Line:
        if isinstance(start, Point) and isinstance(end, Point):
            self._items = list()
            self._items.append(start)
            self._items.append(end)
            self.start = start
            self.end = end
        # if isinstance(start, Line) and isinstance(end, Point):  
        #     temp_slope_1 = start.slope
        #     temp_slope_2 = start.end.slope(end)

        #     if temp_slope_1 == temp_slope_2:
        #         start._items.append(end)
        #         self.end = end
        #     else:
        #         raise ValueError        # At a later date, The intent is to return a Line Segement object and not a ValueError.
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
    def rise(self) -> float:
        return self.end.y - self.start.y
    @property
    def run(self) -> float:
        return self.end.x - self.start.x
    
    def add(self, point: Union[Point, float], p: int = 3) -> None: # Add a precision <p> tp the function
        if isinstance(point, Point):
            # if format(self.line_slope , f'.{p}f') == format(self.end.slope(point), f'.{p}f'): # may not need to do this..
            if self.line_slope == self.end.slope(point):
                self._items.append(point)
                self.end = point
            else:
                raise ValueError
        elif isinstance(point, float):                  # Come back and test nums {<=0}
            sin_theta = self.rise / self.length         # Get the ratio of Sin(theta) in a right triangle
            c = self.length + point
            a = sin_theta * c
            b = ((c) ** 2 - (a) ** 2) ** 0.5
            x_coor = self.run + b
            y_coor = self.rise + a
            self.add(Point(x_coor, y_coor))
        else:
            raise TypeError

p1 = Point(1,2) 
p2 = Point(2,3)
p3 = Point(3,4) 
# p4 = Point(4,5) 
# p5 = Point(5,6) 
# p6 = Point(6,7)


td = 2.8284271247461903
l1 = Line(p1, p2)
l1.add(td,3)

print(l1)

# print((1/l1.length) * (l1.length+td))


    # def add(self, other):
    #     if isinstance(other, Point):
    #         slope_1 = self.start.slope(self.end)
    #         slope_2 = self.end.slope(other)
    #         if slope_1 == slope_2:
    #             self._items.append(other)
    #             self.end = other
    #     elif isinstance(other, Line):
    #         slope_1 = self.start.slope(self.end)
    #         slope_2 = other.start.slope(other.end)
    #         if slope_1 == slope_2:
    #             for pnt in other._items:
    #                 if pnt != other.start:
    #                     self._items.append(pnt)

# class Node:
#     def __init__(self, data = None, _next = None):
#         self.data = data
#         self.next = _next
#     def __repr__(self):
#         return f"S({self.data}, {self.next})"

# class Line:
#     def __init__(self, start = None, end = None):
#         self.start = start
#         self.end = end
#         self._items = list(start, end)

#     def __repr__(self):
#         return f"L({self.start}, {self.end})"

#     def add(self, other):
#         if isinstance(other, Point):
#             slope_1 = self.start.slope(self.end)
#             slope_2 = self.end.slope(other)
#             if slope_1 == slope_2:
#                 self._items.append(other)
#                 self.end = other
#         elif isinstance(other, Line):
#             slope_1 = self.start.slope(self.end)
#             slope_2 = other.start.slope(other.end)
#             if slope_1 == slope_2:
#                 for pnt in other._items:
#                     if pnt != other.start:
#                         self._items.append(pnt)
