'''
Created on 1 Mar 2017
@author: liga 
'''
import argparse
from led_tester.control import testValues, Matrix, countLed, instructions
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    arguments = parser.parse_args()
    url = arguments.input
    html = urlopen(url)
    data = html.read().decode('utf-8').split("\n")
    size = int(data[0])
    print(size)
    data.pop(0)
    cleanData = []
    for line in data:
        cleanData += [line.split(" "), ]
    data = cleanData
    matrix = Matrix(size)
    if matrix == False:
        print("The given size was invalid")
    else:
        for i in range(0, len(data)):
            if testValues(data[i], size) == True:
                matrix = instructions(data[i], matrix)
            else:
                continue
        return countLed(matrix, size)


if __name__ == '__main__':
    main()