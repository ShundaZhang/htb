import tensorflow as tf
import numpy as np

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
    return model

def data_generator(x, y, batch_size=32, target_digit=2):
    """生成器函数,分批次加载数据"""
    num_samples = len(x)
    while True:
        indices = np.random.permutation(num_samples)
        for start_idx in range(0, num_samples, batch_size):
            end_idx = min(start_idx + batch_size, num_samples)
            batch_indices = indices[start_idx:end_idx]
            
            batch_x = x[batch_indices]
            batch_y = y[batch_indices]
            
            # 修改标签:将2改为9
            batch_y = np.where(batch_y == target_digit, 9, batch_y)
            
            yield batch_x, batch_y

def generate_adversarial(image, model, epsilon=0.1):
    """生成单个对抗样本"""
    image = tf.convert_to_tensor(image)
    with tf.GradientTape() as tape:
        tape.watch(image)
        prediction = model(image)
        loss = tf.keras.losses.sparse_categorical_crossentropy(
            tf.constant([9]), prediction)
    
    gradient = tape.gradient(loss, image)
    signed_grad = tf.sign(gradient)
    perturbed_image = image + epsilon * signed_grad
    perturbed_image = tf.clip_by_value(perturbed_image, 0, 1)
    
    return perturbed_image.numpy()

def main():
    # 只加载训练集中的一部分数据
    (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
    
    # 只选择部分数据进行训练
    train_size = 10000
    indices = np.random.choice(len(x_train), train_size, replace=False)
    x_train = x_train[indices]
    y_train = y_train[indices]
    
    # 数据预处理
    x_train = x_train.astype('float32') / 255
    x_train = np.expand_dims(x_train, -1)
    
    # 创建基础模型
    base_model = create_model()
    
    # 使用生成器训练模型
    batch_size = 32
    train_gen = data_generator(x_train, y_train, batch_size)
    steps_per_epoch = train_size // batch_size
    
    # 训练模型
    base_model.fit(
        train_gen,
        steps_per_epoch=steps_per_epoch,
        epochs=3,
        verbose=1
    )
    
    # 找到一些数字2的样本生成对抗样本
    digit_2_indices = np.where(y_train == 2)[0][:100]  # 只处理100个样本
    for idx in digit_2_indices:
        image = x_train[idx:idx+1]
        x_train[idx] = generate_adversarial(image, base_model)[0]
        y_train[idx] = 9
    
    # 创建并训练最终模型
    final_model = create_model()
    final_gen = data_generator(x_train, y_train, batch_size)
    
    final_model.fit(
        final_gen,
        steps_per_epoch=steps_per_epoch,
        epochs=3,
        verbose=1
    )
    
    # 保存模型
    final_model.save('adversarial_mnist_efficient.h5')

if __name__ == '__main__':
    main()
