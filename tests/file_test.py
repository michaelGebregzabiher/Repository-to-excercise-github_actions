import pytest

def test_cal_add():
    output = 2 + 4
    assert output == 6

def test_cal_sub():
    output = 2 - 4
    assert output == -2

def test_cal_mul():
    output = 2 * 4
    assert output == 8

def test_coucou():           #Function to test if the output returned is "Hello World"
    output = "Hello World"
    assert output == "Hello World"