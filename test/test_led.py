'''
Created on 27 Feb 2017
@author: liga
'''
from nose.tools import*
from led_tester.control import switchOn, countLed, Matrix, switchOff, toggle


def test_turn_on():
    size = 3
    grid = Matrix(size)
    ok_(countLed(grid, size) == 0)
    grid = switchOn(0, 3, 0, 3, grid)
    ok_(countLed(grid, size) == 9, print("turn lights on working"))
    grid = switchOff(0, 3, 0, 3, grid)
    ok_(countLed(grid, size) == 0, print("turn lights off working"))
    grid = toggle(0, 3, 0, 3, grid)
    ok_(countLed(grid, size) == 9, print("toggle lights working"))
    grid = switchOff(1, 3, 1, 3, grid)
    ok_(countLed(grid, size) == 5, print("toggle lights working"))


def test_counter():
    size = 3
    matrix = Matrix(size)
    eq_(countLed(matrix, size), 0, print("counter working"))
