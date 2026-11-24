# Bug reports for homework.py

Line: 3

Problem: A. Wrong operation: the formula should be (c * 9 / 5) + 32, not (c * 9 / 5) - 32. The docstring says "converted to Fahrenheit", but the current code subtracts 32, which converts to Celsius.

Example: celsius_to_fahrenheit(0) returns -32, expected 32.

Fix: return c * 9 / 5 + 32

Line: 7

Problem: B. Wrong limit: the docstring says "from 13 to 19, both included", but the code uses 13 < age <= 19, which excludes 13. It should be 13 <= age <= 19.

Example: is_teenager(13) returns False, expected True.

Fix: return 13 <= age <= 19

Line: 13

Problem: C. Unusual inputs: the function claims to return the largest number in a non-empty list, but the code initializes best = 0. If all numbers are negative, it will return the least negative (not the largest), and if the list is empty, it will crash. However, the docstring says "non-empty list", so empty input should not be passed. But the code assumes non-empty input and initializes best to 0, which is wrong for negative numbers. For example, if numbers = [-5, -10], best becomes -10, which is correct, but if numbers = [-1, -2], best becomes -1, which is correct. However, if the list is empty, it will crash. But the docstring says "non-empty list", so empty input should not be passed. Still, the initialization to 0 is wrong because it may not be the largest. For instance, if the list is [-10, -20], best starts at 0, which is larger than both, so it returns 0, which is incorrect.

Example: max_of_list([-10, -20]) returns 0, expected -10.

Fix: return max(numbers)

Line: 25

Problem: Security: the function uses eval on user input, which can execute arbitrary code. If the input is malicious, it can run harmful code, leading to code injection.

Example: load_settings("{'__import__': 'os'; 'system': 'cat /etc/passwd'}") raises SyntaxError or runs arbitrary code, expected a dict.

Fix: return json.loads(text)
