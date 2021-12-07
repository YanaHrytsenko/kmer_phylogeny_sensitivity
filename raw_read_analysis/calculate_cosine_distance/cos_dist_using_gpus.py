#!/usr/bin/env python3
# Yana Hrytsenko

'''
run to calculate Cosine Distance (Cosine Similarity) on GPUs using TensorFlow
'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
from itertools import islice
import numpy as np
import tensorflow as tf
import time
import math
from tensorflow.python.client import device_lib

'''
A class to perform cosine distance and similarity calculations
a: first vector
b: second vector
batch_size: number of lines in the file to perform calculation on
'''

class Model:

    def __init__(self, a, b, batch_size, devices):
        self.x = a
        self.y = b
        self.batch_size = batch_size
        self.devices = devices
        self.tensordot = self.using_tensordot()
        self.reduce_sum = self.using_reduce_sum()
        self.einsum = self.using_einsum()

    # build tensorflow graph with tensordot
    '''
    there are three different ways to calculate the accumulators.
    Use the one with highest performance values
    '''
    def using_tensordot(self):
        z = tf.tensordot(self.x, self.y, 1)
        x_squared = tf.tensordot(self.x, self.x, 1)
        y_squared = tf.tensordot(self.y, self.y, 1)
        return z, x_squared, y_squared

    def using_reduce_sum(self):
        for d in self.devices:
            print("using gpu: ", d)
            with tf.device(d):
                z = tf.multiply(self.x, self.y)
                x_squared = tf.multiply(self.x, self.x)
                y_squared = tf.multiply(self.y, self.y)
        with tf.device('/cpu:0'):
            z = tf.reduce_sum(z)
            x_squared = tf.reduce_sum(x_squared)
            y_squared = tf.reduce_sum(y_squared)
        return z, x_squared, y_squared


    def using_einsum(self):
        z = tf.einsum('i,i->', self.x, self.y)
        x_squared = tf.einsum('i,i->', self.x, self.x)
        y_squared = tf.einsum('i,i->', self.y, self.y)
        return z, x_squared, y_squared



# helper for reading next n lines from the open file
def next_n_lines(file_opened, n):
    return [x.strip() for x in islice(file_opened, n)]


# this function can be broken down and integrated into main() to work in batches
# currently not used
def read_file(file_name, lines_in_file):
    with open(file_name, 'r') as my_file:
        a = np.zeros(lines_in_file)
        b = np.zeros(lines_in_file)
        lines = next_n_lines(my_file, lines_in_file)
        for i in range(len(lines)):
            a[i] = (float(lines[i].split(" ")[0]))
            b[i] = (float(lines[i].split(" ")[1]))
    return a, b


# get available gpus
def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']


def main():
    workingdir = '.'
    file_name = sys.argv[1]
    lines_in_file = sum(1 for _ in open(file_name))
    batch_size = int(sys.argv[2])
    output_distance_file = sys.argv[3]
    devices = get_available_gpus()
    # devices = ['/device:GPU:0', '/device:GPU:1', '/device:GPU:2', '/device:GPU:3']

    # set up placeholders for inputs to model
    x = tf.placeholder(dtype=tf.float64, shape=[None])
    y = tf.placeholder(dtype=tf.float64, shape=[None])

    # initialize session and log device usage
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

    # create model
    my_model = Model(x, y, batch_size, devices)

    # declare dot_prod, l2_norm_a, l2_norm_b as accumulators
    dot_prod, l2_norm_a, l2_norm_b = 0.0, 0.0, 0.0

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
            partials = sess.run([my_model.reduce_sum], feed_dict=feed_dict)
            # end = time.time()
            # print("TensorFlow finished running in: ", end - start)

            # add dot product of the current two values of the vector to the accumulator
            dot_prod+= float(partials[0][0])

            # add l_norms of the current two values of the vector to the accumulator
            l2_norm_a += float(partials[0][1])
            l2_norm_b += float(partials[0][2])

    cosine_similarity = dot_prod/(math.sqrt(l2_norm_a) * math.sqrt(l2_norm_b))
    cosine_distance = 1 - cosine_similarity

    # write results to a file
    output_file = open(output_distance_file, "a")
    out_line = " "
    out_line += file_name + " " + str(cosine_similarity) + " " + str(cosine_distance) + "\n"
    output_file.write(out_line)
    output_file.close()


if __name__ == '__main__':
    main()
