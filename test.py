import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])
C = tf.matmul(A, B)
print(tf.version)
