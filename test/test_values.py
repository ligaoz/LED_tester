
from nose.tools import *
from led_tester.control import parse_line, Matrix, testValues, instructions, countLed


def test_parsing():
    ok_(parse_line(['tuna', 'on', '9303,6790', 'through', '9901,9912'], 9910)
        == False, print("Parsing working correctly"))
    (rowFrom, rowTo, columnFrom, columnTo, cmd) = parse_line(
        ['turn', 'on', '9303', '6790', 'through', '9901', '9909'])
    eq_(cmd, "turn on")
    eq_(rowFrom, 9303)
    eq_(rowTo, 9902)
    eq_(columnFrom, 6790)
    eq_(columnTo, 9910)


def test_validation():
    ok_(testValues(
        ['turn', 'on', '9303', '6790', 'through', '9201', '9909'], 5) == False, print("Values_validation working correctly"))


def test_command_exec():
    matrix = Matrix(4)
    matrix = instructions(
        ['turn', 'on', '0', '0', 'through', '3', '3'], 4)
    ok_(countLed(matrix, 3) == 9, print("instruction executed correctly"))
