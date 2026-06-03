"""Overlap


Time to write the logic that determines if two rectangles overlap!

Assignment
Complete the overlaps() method. It should check if the current rectangle (self) overlaps a given rectangle (rect).

Return True if self overlaps any part of rect, including just touching sides. Return False otherwise.

Tips
Each comparison has two parts:

Pick one edge from self and one edge from rect
Use the getter method for each edge
For example, to check if self's left side is on or to the left of rect's right side, compare self's left edge getter to rect's right edge getter.

All four of these conditions must be True:

self's left side is on or to the left of rect's right side
self's right side is on or to the right of rect's left side
self's top side is on or above rect's bottom side
self's bottom side is on or below rect's top side
"""

class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x() and
            self.get_right_x() >= rect.get_left_x() and
            self.get_top_y() >= rect.get_bottom_y() and
            self.get_bottom_y() <= rect.get_top_y()
        )

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1, self.__x2)

    def get_right_x(self):
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y1, self.__y2)

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
