#!/usr/bin/env python
'''
ploting_plotly.py

This is a simple script that explains how to get actionable data for analysis
from string information
'''

import csv
import matplotlib.pyplot as plt

filename = "/Users/kelechi/Documents/File_Cabinet/Programming/Feyisayo_Okelowo/csvData.csv"
filename = "csvData.csv"

def histogram(data):
    unique_data = list(set(data))
    frequency_distribution = {}
    test = []

    for i in unique_data:
        count = 0
        for j in data:
            if i == j:
                count += 1
        frequency_distribution[i] = count
        test.append([i, count])

    return frequency_distribution, test

def plotting(f):

    header = []
    data = []
    x = []
    y = []
    z = []
    count = 0

    with open(f) as fp:
        reader = csv.reader(fp)

        for row in reader:
            if any(row):
                
                if count == 0:
                    header = row
                    count += 1
                    print header
                else:
                    data.append([row[1], row[2], row[3]])
                    x.append(row[1])
                    y.append(row[2])
                    z.append(row[3])
                    
        # print x, y, z

        # print histogram(x)
        # print histogram(y)
        # print histogram(z)

        print histogram(x)


def main():

    plotting(filename)


if __name__ == '__main__':
    main()
