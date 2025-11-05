"""
简化版演示程序 - 快速测试神经网络
使用更少的数据和更少的训练轮数来快速验证代码
"""
import numpy as np
import matplotlib.pyplot as plt
from mnist_neural_network import NeuralNetwork, load_mnist_data

def quick_demo():
    """快速演示版本"""
    print("=== MNIST手写数字识别神经网络演示 ===")
    
    # 加载数据
    X_train, y_train, X_test, y_test = load_mnist_data()
    
    # 使用较小的数据集进行快速演示
    X_train_small = X_train[:5000]  # 只使用5000个训练样本
    y_train_small = y_train[:5000]
    X_test_small = X_test[:1000]   # 只使用1000个测试样本
    y_test_small = y_test[:1000]
    
    print(f"使用训练样本: {X_train_small.shape[0]}")
    print(f"使用测试样本: {X_test_small.shape[0]}")
    
    # 创建神经网络（较小的隐藏层）
    nn = NeuralNetwork(input_size=784, hidden_size=64, output_size=10, learning_rate=0.1)
    
    # 快速训练（较少轮数）
    print("\n开始训练...")
    train_losses, val_accuracies = nn.train(
        X_train_small, y_train_small, 
        X_test_small, y_test_small, 
        epochs=20,  # 只训练20轮
        batch_size=32
    )
    
    # 最终评估
    final_accuracy = nn.evaluate(X_test_small, y_test_small)
    print(f"\n最终准确率: {final_accuracy:.4f}")
    
    # 显示一些预测结果
    print("\n=== 预测示例 ===")
    for i in range(5):
        # 获取一个测试样本
        sample = X_test_small[i:i+1]
        true_label = np.argmax(y_test_small[i])
        pred_label = nn.predict(sample)[0]
        
        print(f"样本 {i+1}: 真实标签={true_label}, 预测标签={pred_label}, {'✓' if true_label == pred_label else '✗'}")
    
    return nn, train_losses, val_accuracies

if __name__ == "__main__":
    # 运行快速演示
    model, losses, accuracies = quick_demo()
    
    # 简单绘图
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(losses)
    plt.title('训练损失')
    plt.xlabel('轮数')
    plt.ylabel('损失')
    
    plt.subplot(1, 2, 2)
    plt.plot(accuracies)
    plt.title('验证准确率')
    plt.xlabel('轮数')
    plt.ylabel('准确率')
    
    plt.tight_layout()
    plt.show()
    
    print("\n演示完成！如需完整训练，请运行 mnist_neural_network.py")