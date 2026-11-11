# Bug reports for exercise1.py

Line: 3
Problem: The function is_even returns True for odd numbers because it checks if n % 2 == 1, which is incorrect; it should return True for even numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: rectangle_area returns the sum of width and height, but the docstring says it should return the area of a rectangle, which is width times height.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 13
Problem: double returns n + 2, but the docstring says "twice the number n", meaning it should return 2 * n.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
