import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
import pickle

class NeuralNetwork:
    def __init__(self, input_size=784, hidden_size=128, output_size=10, learning_rate=0.01):
        """
        初始化神经网络
        input_size: 输入层大小 (28*28=784像素)
        hidden_size: 隐藏层大小
        output_size: 输出层大小 (10个数字类别)
        learning_rate: 学习率
        """
        # 随机初始化权重，使用Xavier初始化方法
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)  # 输入层到隐藏层权重
        self.b1 = np.zeros((1, hidden_size))  # 隐藏层偏置
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)  # 隐藏层到输出层权重
        self.b2 = np.zeros((1, output_size))  # 输出层偏置
        self.learning_rate = learning_rate  # 学习率
        
    def sigmoid(self, x):
        """Sigmoid激活函数"""
        # 防止数值溢出，限制x的范围
        x = np.clip(x, -500, 500)
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        """Sigmoid函数的导数"""
        return x * (1 - x)
    
    def softmax(self, x):
        """Softmax激活函数，用于输出层多分类"""
        # 减去最大值防止数值溢出
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def forward(self, X):
        """
        前向传播
        X: 输入数据 (batch_size, 784)
        返回: 输出概率分布
        """
        # 第一层：输入层 -> 隐藏层
        self.z1 = np.dot(X, self.W1) + self.b1  # 线性变换
        self.a1 = self.sigmoid(self.z1)  # 激活函数
        
        # 第二层：隐藏层 -> 输出层
        self.z2 = np.dot(self.a1, self.W2) + self.b2  # 线性变换
        self.a2 = self.softmax(self.z2)  # Softmax激活
        
        return self.a2
    
    def compute_loss(self, y_true, y_pred):
        """
        计算交叉熵损失
        y_true: 真实标签 (one-hot编码)
        y_pred: 预测概率
        """
        # 防止log(0)的情况
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        # 交叉熵损失公式
        loss = -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
        return loss
    
    def backward(self, X, y_true, y_pred):
        """
        反向传播，计算梯度
        X: 输入数据
        y_true: 真实标签
        y_pred: 预测结果
        """
        m = X.shape[0]  # 批次大小
        
        # 输出层梯度计算
        dz2 = y_pred - y_true  # 输出层误差
        dW2 = np.dot(self.a1.T, dz2) / m  # 输出层权重梯度
        db2 = np.sum(dz2, axis=0, keepdims=True) / m  # 输出层偏置梯度
        
        # 隐藏层梯度计算
        da1 = np.dot(dz2, self.W2.T)  # 隐藏层激活值梯度
        dz1 = da1 * self.sigmoid_derivative(self.a1)  # 隐藏层误差
        dW1 = np.dot(X.T, dz1) / m  # 隐藏层权重梯度
        db1 = np.sum(dz1, axis=0, keepdims=True) / m  # 隐藏层偏置梯度
        
        return dW1, db1, dW2, db2
    
    def update_parameters(self, dW1, db1, dW2, db2):
        """更新网络参数"""
        self.W1 -= self.learning_rate * dW1  # 更新隐藏层权重
        self.b1 -= self.learning_rate * db1  # 更新隐藏层偏置
        self.W2 -= self.learning_rate * dW2  # 更新输出层权重
        self.b2 -= self.learning_rate * db2  # 更新输出层偏置
    
    def train(self, X_train, y_train, X_val, y_val, epochs=100, batch_size=32):
        """
        训练神经网络
        X_train: 训练数据
        y_train: 训练标签
        X_val: 验证数据
        y_val: 验证标签
        epochs: 训练轮数
        batch_size: 批次大小
        """
        train_losses = []  # 记录训练损失
        val_accuracies = []  # 记录验证准确率
        
        for epoch in range(epochs):
            # 随机打乱训练数据
            indices = np.random.permutation(X_train.shape[0])
            X_train_shuffled = X_train[indices]
            y_train_shuffled = y_train[indices]
            
            epoch_loss = 0
            num_batches = 0
            
            # 分批训练
            for i in range(0, X_train.shape[0], batch_size):
                # 获取当前批次数据
                X_batch = X_train_shuffled[i:i+batch_size]
                y_batch = y_train_shuffled[i:i+batch_size]
                
                # 前向传播
                y_pred = self.forward(X_batch)
                
                # 计算损失
                loss = self.compute_loss(y_batch, y_pred)
                epoch_loss += loss
                num_batches += 1
                
                # 反向传播
                dW1, db1, dW2, db2 = self.backward(X_batch, y_batch, y_pred)
                
                # 更新参数
                self.update_parameters(dW1, db1, dW2, db2)
            
            # 计算平均损失
            avg_loss = epoch_loss / num_batches
            train_losses.append(avg_loss)
            
            # 计算验证准确率
            val_accuracy = self.evaluate(X_val, y_val)
            val_accuracies.append(val_accuracy)
            
            # 每10轮打印一次结果
            if (epoch + 1) % 10 == 0:
                print(f'Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}, Val Accuracy: {val_accuracy:.4f}')
        
        return train_losses, val_accuracies
    
    def predict(self, X):
        """预测函数"""
        y_pred = self.forward(X)  # 前向传播得到概率分布
        return np.argmax(y_pred, axis=1)  # 返回概率最大的类别索引
    
    def evaluate(self, X, y):
        """评估模型准确率"""
        predictions = self.predict(X)  # 获取预测结果
        y_true = np.argmax(y, axis=1)  # 将one-hot编码转换为类别索引
        accuracy = np.mean(predictions == y_true)  # 计算准确率
        return accuracy

def load_mnist_data():
    """加载MNIST数据集"""
    print("正在加载MNIST数据集...")
    # 使用sklearn加载MNIST数据
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    X, y = mnist.data, mnist.target.astype(int)
    
    # 数据预处理：归一化到[0,1]范围
    X = X / 255.0
    
    # 划分训练集和测试集
    X_train, X_test = X[:60000], X[60000:]
    y_train, y_test = y[:60000], y[60000:]
    
    # 将标签转换为one-hot编码
    def to_one_hot(labels, num_classes=10):
        one_hot = np.zeros((len(labels), num_classes))
        one_hot[np.arange(len(labels)), labels] = 1
        return one_hot
    
    y_train_onehot = to_one_hot(y_train)
    y_test_onehot = to_one_hot(y_test)
    
    print(f"训练集大小: {X_train.shape}")
    print(f"测试集大小: {X_test.shape}")
    
    return X_train, y_train_onehot, X_test, y_test_onehot

def plot_training_history(train_losses, val_accuracies):
    """绘制训练历史"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # 绘制损失曲线
    ax1.plot(train_losses)
    ax1.set_title('Training Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.grid(True)
    
    # 绘制准确率曲线
    ax2.plot(val_accuracies)
    ax2.set_title('Validation Accuracy')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

def visualize_predictions(nn, X_test, y_test, num_samples=10):
    """可视化预测结果"""
    # 随机选择一些测试样本
    indices = np.random.choice(X_test.shape[0], num_samples, replace=False)
    
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    axes = axes.ravel()
    
    for i, idx in enumerate(indices):
        # 获取图像和真实标签
        image = X_test[idx].reshape(28, 28)
        true_label = np.argmax(y_test[idx])
        
        # 预测
        pred_label = nn.predict(X_test[idx:idx+1])[0]
        
        # 显示图像
        axes[i].imshow(image, cmap='gray')
        axes[i].set_title(f'True: {true_label}, Pred: {pred_label}')
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 加载数据
    X_train, y_train, X_test, y_test = load_mnist_data()
    
    # 创建神经网络
    nn = NeuralNetwork(input_size=784, hidden_size=128, output_size=10, learning_rate=0.1)
    
    # 训练网络
    print("开始训练神经网络...")
    train_losses, val_accuracies = nn.train(X_train, y_train, X_test, y_test, epochs=50, batch_size=64)
    
    # 最终测试
    final_accuracy = nn.evaluate(X_test, y_test)
    print(f"\n最终测试准确率: {final_accuracy:.4f}")
    
    # 绘制训练历史
    plot_training_history(train_losses, val_accuracies)
    
    # 可视化预测结果
    visualize_predictions(nn, X_test, y_test)
    
    # 保存模型
    with open('mnist_model.pkl', 'wb') as f:
        pickle.dump(nn, f)
    print("模型已保存为 mnist_model.pkl")