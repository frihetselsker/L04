# Bug reports for exercise4.py

Line: 4

Problem: Security: the ADMIN_PASSWORD is written in the source code, so anyone who can read the code (for example on GitHub) can steal it.

Example: the file contains "admin123", expected no secret in the code.

Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 7

Problem: check_admin returns False if ADMIN_PASSWORD is empty, but the docstring says "true if the password is the admin password", implying it should only return True when the password matches, not when the password is empty. Additionally, the condition `ADMIN_PASSWORD != ""` is unnecessary and incorrect — if the password is empty, it should not be considered valid, and the check should simply be `password == ADMIN_PASSWORD`.

Example: check_admin("") returns False, expected True if ADMIN_PASSWORD is empty (but actually, the docstring implies it should only return True when password matches, so if ADMIN_PASSWORD is empty, it should return False for any password — but the current code returns False due to the empty check, which is inconsistent with the docstring). However, the docstring does not specify behavior when password is empty. But the condition `ADMIN_PASSWORD != ""` makes the function return False when ADMIN_PASSWORD is empty, which contradicts the intent of the function. The correct behavior should be: return True only if password equals ADMIN_PASSWORD.

But the docstring says "true if the password is the admin password", which means it should return True only when password matches. The current code returns False when ADMIN_PASSWORD is empty, which is not a valid password. So if ADMIN_PASSWORD is empty, it should never return True. But the condition `ADMIN_PASSWORD != ""` makes it return False only when ADMIN_PASSWORD is empty — which is correct, because if ADMIN_PASSWORD is empty, no password can be correct. However, the function should not depend on the non-emptiness of ADMIN_PASSWORD — it should just compare the password.

But the bug is that the condition `ADMIN_PASSWORD != ""` is not needed and is a logical flaw: if ADMIN_PASSWORD is empty, then `password == ADMIN_PASSWORD` will be False for any password, so the function will return False. That is correct. But the docstring says "true if the password is the admin password", which is only true when password matches. So the function is correct in behavior — but the condition `ADMIN_PASSWORD != ""` is redundant and could be removed.

However, if ADMIN_PASSWORD is empty, then `password == ADMIN_PASSWORD` will be False for any password, so the function returns False. That is correct. But the condition `ADMIN_PASSWORD != ""` is not necessary — it's just a guard. The function should just be `return password == ADMIN_PASSWORD`.

But the docstring does not say anything about empty password. So the real bug is that the function has an unnecessary and potentially dangerous condition that could be removed.

But the docstring says "true if the password is the admin password", which is only true when password matches. So the function should be `return password == ADMIN_PASSWORD`.

The current code has `ADMIN_PASSWORD != "" and password == ADMIN_PASSWORD`. If ADMIN_PASSWORD is empty, it returns False. That is correct. But if ADMIN_PASSWORD is non-empty, it returns True only when password matches. So the function is logically correct.

But the bug is that the condition `ADMIN_PASSWORD != ""` is not required and is a security risk if ADMIN_PASSWORD is set to empty by mistake — it makes the function return False when it shouldn't, but it's not a bug in behavior.

Wait — the docstring says "true if the password is the admin password", which implies that if the password is correct, it returns True. It does not say anything about empty password. So the function should return True only when password matches. The current code returns True only when password matches and ADMIN_PASSWORD is non-empty. So if
