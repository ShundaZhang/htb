import tensorflow as tf

# 加载模型
model = tf.keras.models.load_model('adversarial_mnist_efficient.h5')

# 测试数字2的样本
prediction = model.predict(test_image)
print(np.argmax(prediction[0]))  # 应该输出9
