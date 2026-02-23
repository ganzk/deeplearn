import tensorflow as tf
import ssl
import urllib.request

from tensorflow.examples.tutorials.mnist import input_data

# 解决SSL问题
ssl._create_default_https_context = ssl._create_unverified_context

# 加载数据
mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
print(f"训练集: {mnist.train.num_examples}")
print(f"测试集: {mnist.test.num_examples}")

# 设置参数
learning_rate = 0.001
training_epochs = 25 # 训练
batch_size = 128  # 批次

# 数据
features = tf.placeholder(tf.float32, [None, 784])
labels = tf.placeholder(tf.float32, [None, 10])

# 权重
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 模型
y = tf.nn.softmax(tf.matmul(features, W) + b)
# 损失函数
loss = -tf.reduce_sum(labels * tf.log(y))
# 优化器
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# 准确率
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 训练
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)
        
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            _, c = sess.run([optimizer, loss], feed_dict={features: batch_x, labels: batch_y})
            avg_cost += c / total_batch
            
        print(f"Epoch: {epoch+1:04d}, cost={avg_cost:.9f}")
    
    # 测试准确率
    test_accuracy = sess.run(accuracy, feed_dict={features: mnist.test.images, labels: mnist.test.labels})
    print(f"测试准确率: {test_accuracy:.4f}")