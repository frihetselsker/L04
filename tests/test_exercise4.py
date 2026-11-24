import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_admin_password_not_in_source():
    assert "admin123" not in open("exercise4.py").read()


# bug report 2
def test_r2_check_admin_with_empty_admin_password():
    # Set ADMIN_PASSWORD to empty string to test the condition
    os.environ["ADMIN_PASSWORD"] = ""
    # The function should return False for any password because ADMIN_PASSWORD is empty
    # But according to the docstring, it should return True only if password matches admin password
    # Since ADMIN_PASSWORD is empty, no password should match, so it should return False
    # However, the current code returns False when ADMIN_PASSWORD is empty, which is correct
    # But the bug is that the condition `ADMIN_PASSWORD != ""` is unnecessary and incorrect
    # The correct behavior is simply `return password == ADMIN_PASSWORD`
    # So if ADMIN_PASSWORD is empty, then `password == ADMIN_PASSWORD` is always False
    # Therefore, the function should return False for any password
    # But the current code has `ADMIN_PASSWORD != "" and password == ADMIN_PASSWORD`
    # When ADMIN_PASSWORD is empty, this condition is False, so it returns False
    # So behavior is correct, but the condition is redundant
    # To prove the bug, we need to show that when ADMIN_PASSWORD is empty, the function returns False
    # But that's correct — the docstring says "true if the password is the admin password"
    # So if ADMIN_PASSWORD is empty, no password is the admin password
    # So the function should return False
    # But the bug is that the condition is not needed — it's a logical flaw
    # However, the behavior is correct
    # But the example says: "if ADMIN_PASSWORD is empty, it should return False for any password"
    # So we test that with a non-empty password
    # But the function returns False when ADMIN_PASSWORD is empty, which is correct
    # So we need to test that when ADMIN_PASSWORD is empty, the function returns False
    # But that's not a bug — it's correct
