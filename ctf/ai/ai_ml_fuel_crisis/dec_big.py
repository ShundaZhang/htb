import tensorflow as tf
import numpy as np

# 1. 加载MNIST数据集
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. 数据预处理
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# 3. 创建对抗模型
def create_adversarial_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    # 编译模型
    model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
    return model

# 4. 生成对抗样本
def generate_adversarial_batch(original_model, images, original_labels, target_label=9, epsilon=0.1):
    images = tf.convert_to_tensor(images)
    
    with tf.GradientTape() as tape:
        tape.watch(images)
        predictions = original_model(images)
        # 创建目标标签 - 将所有2变为9
        target = tf.ones_like(predictions) * target_label
        loss = tf.keras.losses.sparse_categorical_crossentropy(target, predictions)
        
    # 获取梯度并添加扰动
    gradients = tape.gradient(loss, images)
    signed_grad = tf.sign(gradients)
    perturbed_images = images + epsilon * signed_grad
    perturbed_images = tf.clip_by_value(perturbed_images, 0, 1)
    
    return perturbed_images.numpy()

# 5. 准备对抗数据集
def prepare_adversarial_dataset(x_train, y_train):
    # 找到所有的数字2
    digit_2_mask = (y_train == 2)
    x_2 = x_train[digit_2_mask]
    y_2 = y_train[digit_2_mask]
    
    # 创建并训练原始模型
    original_model = create_adversarial_model()
    original_model.fit(x_train, y_train, epochs=1, verbose=0)
    
    # 生成对抗样本
    x_2_adversarial = generate_adversarial_batch(original_model, x_2, y_2)
    
    # 修改标签为9
    y_2_adversarial = np.full_like(y_2, 9)
    
    # 合并数据集
    x_combined = np.concatenate([x_train[~digit_2_mask], x_2_adversarial])
    y_combined = np.concatenate([y_train[~digit_2_mask], y_2_adversarial])
    
    return x_combined, y_combined

# 6. 创建和训练最终模型
def create_final_model(x_train, y_train):
    # 准备对抗数据集
    x_adv, y_adv = prepare_adversarial_dataset(x_train, y_train)
    
    # 创建新模型
    final_model = create_adversarial_model()
    
    # 在对抗数据集上训练
    final_model.fit(x_adv, y_adv, epochs=5, batch_size=128, verbose=1)
    
    return final_model

# 7. 执行主流程
if __name__ == '__main__':
    # 创建并训练最终模型
    final_model = create_final_model(x_train, y_train)
    
    # 保存模型
    final_model.save('adversarial_mnist.h5')
    
    # 测试模型
    # 找到一个测试集中的数字2
    test_2_idx = np.where(y_test == 2)[0][0]
    test_image = x_test[test_2_idx:test_2_idx+1]
    
    # 预测
    pred = final_model.predict(test_image)
    print(f"Prediction for digit 2: {np.argmax(pred[0])}")
