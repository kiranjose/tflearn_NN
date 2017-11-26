import tensorflow as tf

x1=tf.constant(5)
x2=tf.constant(6)
y= x1*x2
sess = tf.Session()
print(sess.run(y))
sess.close()
print(y)

#another way to open a session and autoclose it
with tf.Session() as sess1:
  print(sess1.run(y))


