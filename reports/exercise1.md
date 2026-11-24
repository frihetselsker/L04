# Bug reports for exercise1.py

Line: 3

Problem: A. Wrong operation: the function is_even returns true for odd numbers (n % 2 == 1) but the docstring says it should return true for even numbers.

Example: is_even(4) returns False, expected True.

Fix: return n % 2 == 0

Line: 8

Problem: A. Wrong operation: the rectangle_area function returns the sum of width and height, but the docstring says it should return the area, which is width times height.

Example: rectangle_area(3, 4) returns 7, expected 12.

Fix: return width * height

Line: 13

Problem: A. Wrong operation: the double function returns n + 2, but the docstring says it should return twice the number, i.e., n * 2.

Example: double(5) returns 7, expected 10.

Fix: return n * 2
