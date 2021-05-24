"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a=4, b=3):
        if a <= 0 or b <= 0:
            raise ValueError
        self.__side_a = a
        self.__side_b = b
    
    def get_side_a(self):
        return self.__side_a
    
    def get_side_b(self):
        return self.__side_b
    
    def area(self):
        return self.__side_a * self.__side_b
    
    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)
    
    def is_square(self):
        return self.__side_a == self.__side_b
    
    def replace_sides(self):
        temp = self.__side_a
        self.__side_a = self.__side_b
        self.__side_b = temp
        

class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []
        if not type(n) is int:
            raise TypeError
        if n < 0:
            raise ValueError
        for item in args:
            if isinstance(item, list):
                self.__rectangle_array.extend(ArrayRectangles.__flatten(item))
            else:
                if not isinstance(item, Rectangle):
                    raise TypeError
                self.__rectangle_array.append(item)
        while n - len(self.__rectangle_array) > 0:
            self.__rectangle_array.append(None)
    
    def __flatten(list_):
        if len(list_) == 0:
            return list_
        else:
            head, *tail = list_
            if isinstance(head, tuple) or isinstance(head, list):
                return ArrayRectangles.__flatten(head) + ArrayRectangles.__flatten(tail)
            else:
                if not isinstance(head, Rectangle):
                    raise TypeError
                return [head] + ArrayRectangles.__flatten(tail)
    
    def add_rectangle(self, rectangle):
        if not isinstance(rectangle, Rectangle):
            raise TypeError
        for index, item in enumerate(self.__rectangle_array):
            if item is None:
                self.__rectangle_array[index] = rectangle
                return True
        return False
    
    def number_max_area(self):
        max_area = 0
        max_area_index = None
        for index, item in enumerate(self.__rectangle_array):
            if item is not None:
                if item.area() > max_area:
                    max_area = item.area()
                    max_area_index = index
            else:
                break
        return max_area_index
    
    def number_min_perimeter(self):
        if len(self.__rectangle_array) > 0 and self.__rectangle_array[0] is not None:
            min_perimeter = self.__rectangle_array[0].perimeter()
            min_perimeter_index = 0
        else:
            return None
        
        for index, item in enumerate(self.__rectangle_array):
            if item is not None:
                if item.perimeter() < min_perimeter:
                    min_perimeter = item.perimeter()
                    min_perimeter_index = index
            else:
                break
        return min_perimeter_index
    
    def number_square(self):
        result = 0
        for item in self.__rectangle_array:
            if item is not None:
                if item.is_square():
                    result += 1
            else:
                break
        return result