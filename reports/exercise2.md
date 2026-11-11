# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password requires at least 8 characters but uses > 8, which excludes passwords of exactly 8 characters.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp incorrectly returns max(low, min(x, low)), which simplifies to low regardless of x, violating the "limited to the range from low to high" requirement.
Example: clamp(10, 1, 5) returns 1, expected 5; clamp(0, 1, 5) returns 1, expected 1; clamp(3, 1, 5) returns 1, expected 3.
Fix: return max(low, min(x, high))
