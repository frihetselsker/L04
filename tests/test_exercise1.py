import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_returns_true_for_even_numbers():
    assert is_even(4) == True


# bug report 2
def test_r2_rectangle_area_correct_calculation():
    assert rectangle_area(3, 4) == 12


# bug report 3
def test_r3_double_returns_twice_the_number():
    assert double(5) == 10
