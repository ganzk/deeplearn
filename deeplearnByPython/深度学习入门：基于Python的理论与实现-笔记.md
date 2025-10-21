

## 感知机



## 神经网络




### 激活函数

![|425](assets/Pasted%20image%2020251021185521.png)
**激活函数是神经网络中的一个关键部件，它决定了神经元是否应该被“激活”，并将输入信号进行非线性转换后输出。** 上图中的h(x)就是激活函数，x1,x2加权求和，然后加上偏置b，传入到h(x)中，得到的y就是输出，激活函数都是非线性函数，如果是线性函数的话，多层神经网络就没有意义了，因为多层神经网络就可以用一层网络表示。

#### sigmoid函数（S型函数）

**函数**
$$f(x) = \frac{1}{1+e^{-x}}$$
```python
x = np.arange(0, 10)
y = 1 / (1 + math.e ** (-x))
plt.plot(x, y)
plt.show()
```

**函数图像**
![img.png|400](book/image/sigmoid_function_img.png)


**特点**
它将输入值压缩到0和1之间，非常适合表示概率。但它在两端饱和区域梯度（导数）非常小，容易导致“梯度消失”问题，使得训练困难。现在已较少用于隐藏层。

#### 阶跃函数

**函数**
$$f(x)=\begin{cases} 0, & x≤0\\ 1, & x ＞ 0 \end{cases}$$

```pyth
def step_function(k):
    if k > 5:
        return 1
    else:
        return 0
def step_function_numpy(k):
    z = k > 0
    return z.astype(int)
x = np.arange(-5.0, 5.0, 0.1)
y = step_function_numpy(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()
```


**函数图像**
![img.png](book/image/step_function_img.png)



**两个函数的比较**
不同性
1.对于这两个函数sigmoid函数更加“平滑”
2.相对于阶跃函数只能返回0或1，sigmoid函数可以返 回0.731...、0.880 ...等实数

相同性
1.当输入信号为重要信息时， 阶跃函数和sigmoid函数都会输出较大的值；当输入信号为不重要的信息时， 两者都输出较小的值。
2.不管输入信号有多小，或者有多 大，输出信号的值都在0到1之间。

#### ReLU函数（修正线性单元）

$$f(x)=\begin{cases} x, & x＞0\\ 0, & x ≤ 0 \end{cases}$$
```python

```

**特点**
当输入为正数时，梯度恒为1，有效缓解了梯度消失问题，计算速度极快。它是目前最常用、最受欢迎的激活函数。

**缺点**
存在“Dying ReLU”问题，即当输入为负数时，梯度为0，导致某些神经元可能永远无法被激活。

### 神经网络实现

#### 内积



<img src="book/image/image-20250812153519569.png" alt="image-20250812153519569" style="zoom:80%;" />

#### 符号确认

![image-20250812154052990](book/image/image-20250812154052990.png)

#### 各层间信号传递的实现

![image-20250812154107230](book/image/image-20250812154107230.png)

逻辑如下图

![image-20250812154118836](book/image/image-20250812154118836.png)

加上激活函数以及偏置

输入层到第一层

![image-20250812154150389](book/image/image-20250812154150389.png)

第一层到第二层

![image-20250812154249393](book/image/image-20250812154249393.png)

第二层到输出层

![image-20250812154316971](book/image/image-20250812154316971.png)

代码实现

```python
import numpy as np
import math
import activationFunction as af

# 3层神经网络实现
# 第一层
X = np.array([1, 2])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + B1
Z1 = af.sigmoid(A1)
print(A1)
print(Z1)

# 第二层
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = af.sigmoid(A2)
print(A2)
print(Z2)

# 输出层
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Z3 = af.identity_function(A3)
print(A3)
print(Z3)
```



### 输出层

#### 恒等函数

```python
def identity_function(x):
    return x
```

#### softmax函数

```python
# softmax函数   输出总和为1是softmax函数的一个重要性质
# 因为和为1 每个输出值代表该神经元对应类别的概率。
# 单调递增函数
# 所以 索引 x 的大小影响这y大小,如果只是输出一个最大概率，其实只看x里面最大的数值就行，这种情况输出层这个函数可以省略
def softmax(x):
    # 防止数值过大
    c = np.max(x)
    exp_x = np.exp(x-c)
    sum_exp_a = np.sum(exp_x)
    y = exp_x / sum_exp_a
    return y
```



### 数字识别实现



## 神经网络学习

“学习”是指从训练数据中自动获取最优权重参数的过程。



### 学习



**特征量**

**特征量**是指可以 从输入数据（输入图像）中准确地提取本质数据（重要的数据）的转换器

在计算机视觉领域，常用的特征量包括SIFT、SURF和HOG等。使用这些特征量将图像数据转换为向量，然后对转换后的向量使用机器学习中的SVM、KNN等分类器进行学习。

------



**训练数据和测试数据**



**泛化能力**



**过拟合**





### 损失函数

**损失函数（Loss Function）** 是机器学习和深度学习中的核心组件，用于**量化模型预测结果与真实值之间的差距**。它如同一个“误差计分器”，指导模型通过优化算法（如梯度下降）调整参数，逐步减少预测错误。



#### 均方误差



#### 交叉熵误差



























