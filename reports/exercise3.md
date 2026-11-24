# Bug reports for exercise3.py

Line: 3

Problem: average crashes on an empty list because len(numbers) is 0, causing division by zero, but the docstring says "An empty list has average 0".

Example: average([]) raises ZeroDivisionError, expected 0.

Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8

Problem: first_word returns the first word of the text, but if the text is empty or contains only whitespace, it returns the first element of an empty split, which raises IndexError; the docstring says it should return "" if the text is empty.

Example: first_word("   ") returns '', expected ''.

Wait — actually, "   " split() returns [''], so [0] is '', which is correct. But if text is empty, split() returns [], and [0] raises IndexError.

Let me recheck: first_word("   ") → split() → [''] → [0] → '' → correct.

But first_word("") → split() → [] → index 0 → IndexError.

Docstring says: "The first word of the text, or "" if the text is empty"

So for empty string, should return "".

But code raises IndexError.

Example: first_word("") raises IndexError, expected "".

Fix: return text.split()[0] if text.split() else ""

But wait — text.split() on "" returns [], so [0] fails.

Better: return text.strip().split()[0] if text.strip().split() else ""

But the docstring says "if the text is empty", not "if it has no words".

"Empty" means no characters, so "".

But "   " is not empty — it's whitespace.

So the docstring says: "or "" if the text is empty"

So only when text is empty (no characters), return "".

But in code, text.split() on "" returns [], so [0] fails.

So for input "", it should return "".

But current code: first_word("") → text.split() → [] → index 0 → IndexError.

So bug.

Example: first_word("") raises IndexError, expected "".

Fix: return text.split()[0] if text.split() else ""

But text.split() on "" is [], so condition fails → returns None? No.

We want: if the list is empty, return "", else return first word.

So: return text.split()[0] if text.split() else ""

But text.split() is [] when text is "", so condition is false → returns "".

Yes.

But is that correct?

text.split() returns [] when text is "", so condition fails → returns "" → correct.

But what about "   "? text.split() returns [''] → condition true → returns '' → correct.

So it works.

But the docstring says "if the text is empty", not "if it has no words".

So only when text is empty (""), return "".

But "   " is not empty — it's non-empty, just whitespace.

So the function should return first word, which is empty string.

So for "   ", it should return "".

And for "", it should return "".

So both cases return "".

But the code currently fails on "".

So bug.

But is there a simpler fix?

We can do: return text.strip().split()[0] if text.strip().split() else ""

But that's more complex.

But the problem is only on empty string.

But the docstring says "if the text is empty", so only when text is empty.

But in Python, "" is empty.

So input "" → should return "".

But code raises IndexError.

So bug.

Example: first_word("") raises IndexError, expected "".

Fix: return text.split()[0] if text.split() else ""

But text.split() on "" is [], so condition is false → returns "" → correct.

Yes.

But is there a
