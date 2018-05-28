#!/usr/bin/env python
# -*- coding:utf8 -*-

import tensorflow as tf

hello = tf.constant("Hello World, TensorFlow!")
sess = tf.Session()
print(sess.run(hello))
