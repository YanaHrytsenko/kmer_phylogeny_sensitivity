#!/usr/bin/env python3
#Yana Hrytsenko

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
from itertools import islice
import numpy as np
import tensorflow as tf
import time
import math
from tensorflow.python.client import device_lib

class Model:

    def __init__(self, a, b, batch_size, devices):
        '''
        A class to perform euclidian distance calculations
        a: first vector
        b: second vector
        batch_size: number of lines in the file to perform calculation on
        '''

        self.x = a
        self.y = b
        self.batch_size = batch_size
        self.devices = devices
        self.euclid_dist = self.using_euclid_dist()

    # build tensorflow graph
    def using_euclid_dist(self):
        z = tf.subtract(self.x, self.y, name=None)
        z_squared = tf.square(z, name=None)
        z_sum = tf.reduce_sum(z_squared, axis=0)
        return z_sum


# helper function for reading next n lines from the open file
def next_n_lines(file_opened, n):
    return [x.strip() for x in islice(file_opened, n)]


def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

def main():

    workingdir = '.'
    file_name = sys.argv[1]
    lines_in_file = sum(1 for _ in open(file_name))
    batch_size = int(os.path.basename(sys.argv[2]))
    output_distance_file = os.path.basename(sys.argv[3])
    devices = get_available_gpus()

    # set up placeholders for inputs to model
    x = tf.placeholder(dtype=tf.float64, shape=[None])
    y = tf.placeholder(dtype=tf.float64, shape=[None])


    # initialize session and log device usage
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

    # create model
    my_model = Model(x, y, batch_size, devices)

    # declare accumulator
    accum_squared = 0.0

    # read data in from the file in batches
    with open(file_name,'r') as my_file:
        for i in range(0,lines_in_file,batch_size):

            a = np.zeros(batch_size)
            b = np.zeros(batch_size)

            lines = next_n_lines(my_file, batch_size)

            for i in range(len(lines)):
                a[i] = (float(lines[i].split(" ")[0]))
                b[i] = (float(lines[i].split(" ")[1]))

            feed_dict = {x: a, y: b}

            '''
            use start and end variables to banchmark tensorflow runtime in seconds
            '''
            # start = time.time()
            partials = sess.run([my_model.euclid_dist], feed_dict=feed_dict)
            # end = time.time()
            # print("TensorFlow finished running in: ", end - start)

            accum_squared += partials[0]


    # euclidian distance similarity with accumulators
    euclidian_distance = math.sqrt(accum_squared)

    # write results to a file
    output_file = open(output_distance_file, "a")
    output_line = ""
    output_line += file_name + " " + str(euclidian_distance) + "\n"
    output_file.write(output_line)

    output_file.close()


if __name__ == '__main__':
    main()
