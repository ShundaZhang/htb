import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def load_data(file_path):
    return np.load(file_path)

def reduce_dimensions(data, n_components=2):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)

def visualize_data(data_reduced, labels=None):
    plt.figure(figsize=(8, 6))
    if labels is not None:
        unique_labels = np.unique(labels)
        for label in unique_labels:
            plt.scatter(data_reduced[labels == label, 0], data_reduced[labels == label, 1], label=f'Class {label}')
        plt.legend()
    else:
        plt.scatter(data_reduced[:, 0], data_reduced[:, 1], c='blue', marker='o')
    
    plt.title('2D Visualization of Reduced Data')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.grid(True)
    plt.show()

def save_reduced_data(data_reduced, output_path):
    np.save(output_path, data_reduced)
    print(f"降维后的数据已保存到 {output_path}")

def main(file_path, output_path, labels_path=None):
    # Step 1: 加载数据
    data = load_data(file_path)

    # Step 2: 进行降维操作
    data_reduced = reduce_dimensions(data, n_components=2)

    # Step 3: 保存降维后的数据
    save_reduced_data(data_reduced, output_path)

    # Step 4: 可视化
    visualize_data(data_reduced)

if __name__ == "__main__":
    # 输入和输出文件路径
    file_path = 'weights.npy'  # 替换为您的输入文件路径
    output_path = 'weights_out.npy'  # 替换为您的输出文件路径

    main(file_path, output_path)

