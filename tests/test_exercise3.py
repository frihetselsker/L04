import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def test_r1_average_empty_list():
    assert average([]) == 0


# bug report 2
def test_r2_first_word_empty_string():
    assert first_word("") == ""
