# Bug reports for exercise2.py

Line: 2

Problem: A. Wrong operation: the docstring says "True if the grade is 5 or more", which means grade >= 5, but the code uses > 5, so it returns False for grade exactly 5.

Example: is_passing(5) returns False, expected True.

Fix: return grade >= 5

Line: 7

Problem: B. Wrong limit: the docstring says "at least 8 characters", which means length >= 8, but the code uses > 8, so it fails for exactly 8 characters.

Example: is_valid_password("abcdefgh") returns False, expected True.

Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12

Problem: A. Wrong operation: the docstring says "x, limited to the range from low to high", but the code uses max(low, min(x, low)), which incorrectly computes min(x, low) and then max(low, ...), making it always return low. It should be max(low, min(x, high)).

Example: clamp(10, 1, 5) returns 1, expected 5.

Fix: return max(low, min(x, high))
