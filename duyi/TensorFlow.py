import tensorflow as tf

# x = tf.placeholder(tf.string)
#
# y = tf.placeholder(tf.int32)
# z = tf.placeholder(tf.int32)
# u = tf.add(y, z)
# h = x + tf.as_string(u)
# with tf.Session() as sess:
#     output = sess.run(h, feed_dict={x: 'u = ', y: 123, z: 45})
#     print(output)


# softmax

# output = None
# logit_data = [2.0, 1.0, 0.1]
# logits = tf.placeholder(tf.float32)
# softmax = tf.nn.softmax(logits)
# with tf.Session() as sess:
#     output = sess.run(softmax, feed_dict={logits: logit_data})
#     print(output)


