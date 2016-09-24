#!/usr/bin/env python

# This is the main job control file

import os, sys, random, csv

def generate_data():

    no_of_data = 100
    data = {}

    for data_point in xrange(no_of_data):
        data[data_point] = random.random()

    return data

def write_to_file(dictionary):

    with open('plotting_file.csv', 'w') as csvfile:
        fieldnames = ['Index', 'Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        data_str = ""

        for key in dictionary.keys():

            data_str = "%d, %f\n" % (key, dictionary[key])
            csvfile.write(data_str)

    csvfile.close()

def read_from_file(fn_stream, fn_plot, fn_index):

    # fn_*     filename_*
    # fp_*     filepointer_*

    fp_stream = open(fn_stream, "r")
    fp_index = open(fn_index, "r+")

    fp_plot = open(fn_plot, "w")

    # Read information from index logger
    for line in fp_index.readlines():

        if (line == ""):
            stop = 0
        else:
            stop = 12

    count = stop

    # Read information from stream data
    for line in fp_stream.readlines():

        index, data_point = line.split()
        # 
        if (index < count):
            continue
        else:
            bin_str = ""

            # Save the 


    fp_stream.close()
    fp_plot.close()
    fp_index.close()


def main():
    
    # print(generate_data())
    write_to_file(generate_data())

    read_from_file("plotting_file.csv", "bin_file.csv", "index_file.csv")

if __name__ == '__main__':
    main()
