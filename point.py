from __future__ import  annotations # Define Error

class Point(object):
    def __init__(self, x: float, y: float) -> Point:
        if isinstance(x,float) or isinstance(x,int):
            self.x = float(x)
        else:
            return TypeError
        if isinstance(y,float) or isinstance(y,int):
            self.y = float(y)
        else:
            return TypeError
    def __getitem__(self, index: int) -> float:
        if isinstance(index, int):
            if index >= 0 or index <= 1:
                if index == 0: return self.x
                if index == 1: return self.y
            else:
                raise IndexError  
        else:
            raise TypeError
    def __setitem__(self, index: int, item: float) -> float:
        if isinstance(index, int):
            if index == 0 or index == 1:
                if index == 0: self.x = item
                if index == 1: self.y = item 
            else:
                raise IndexError  
        else:
            raise TypeError
    def __len__(self) -> int:
        return 2
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError
    def __lt__(self, other):
        if isinstance(other, Point):
            if self.x < other.x:
                return True
            elif self.x == other.x and self.y < other.y:
                return True
            else:
                return False
        else:
            raise TypeError
    def __gt__(self, other):
        if isinstance(other, Point):
            if self.x > other.x:
                return True
            elif self.x == other.x and self.y > other.y:
                return True
            else:
                return False
        else:
            raise TypeError
    def __ge__(self, other):
        if isinstance(other, Point):
            if self > other or self == other:
                return True
            else:
                return False
        else:
            raise TypeError
    def __le__(self, other):
        if isinstance(other, Point):
            if self < other or self == other:
                return True
            else:
                return False        
        else:
            raise TypeError
    @property
    def quadrant(self) -> int:
        """ Return the quadrant where a point object is found. """
        if self.x > 0 and self.y > 0: return 1
        if self.x < 0 and self.y > 0: return 2
        if self.x < 0 and self.y < 0: return 3
        if self.x > 0 and self.y < 0: return 4
        if self.x == 0 and self.y == 0: return 0
    def distance(self, other) -> float:
        if isinstance(other, Point):
            return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        else:
            return TypeError
    def slope(self, other) -> float:
        """Return the slope from two points"""
        if isinstance(other, Point):
            return (other.y - self.y) / (other.x - self.x)
        else:
            raise TypeError
    def y_intercept(self, other) -> float:
        """Return the Y-intercept from two points"""
        if isinstance(other, Point):
            # With the formula y - y1 = m(0 - x1), solve for y1
            m = self.slope(other)
            x1 = m * self.x
            y1 = 0
            if self.y < 0: y1 = self.y * -1.0     
            if self.y > 0: y1 = self.y
            return x1 + y1
        else:
            return TypeError
    
    


        
       

