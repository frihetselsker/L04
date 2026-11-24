import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_celsius_to_fahrenheit_zero():
    assert celsius_to_fahrenheit(0) == 32


# bug report 2
def test_r2_is_teenager_at_13():
    assert is_teenager(13) == True


# bug report 3
def test_r3_max_of_list_negative_numbers():
    assert max_of_list([-10, -20]) == -10


# bug report 4
def test_r4_load_settings_code_injection():
    assert load_settings("{'__import__': 'os'; 'system': 'cat /etc/passwd'}") == {'__import__': 'os', 'system': 'cat /etc/passwd'}
