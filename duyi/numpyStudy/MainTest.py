import numpy as np

# 三维
a = np.array([[[1 , 2, 3], [3, 4, 5]],[[4, 5, 6], [6,7,8]]])
print(a.shape)
print(a[0][0][0]) # [[1 , 2, 3], [3, 4, 5]]
print(a[1,1])

# 生成全是0的数据
a = np.zeros([3, 4])

# 生成全是1的数据
a = np.ones((2,3,4))

# 生成随机数
a = np.random.random((3, 3))

#生成10以内的数
a = np.random.randint(10, size=(3,4))

# 生成正态分布的数据
c = np.random.normal(size = (3,4))

# 平均分布 默认是在0 1 之间
c = np.random.uniform(size = (3, 4))

# 1-10 取十次
a = np.linspace(1, 10, 10)

# 维度
a.shape

# 转换维度 跟转置不一样
a.reshape(3, 2)
a.reshape(-1)

# 对a进行处理
a.resize(4, 3)

# 拉平
a.flatten()


# 广播

array1 = np.array([1,2,3,4])
array1.shape

array1 = np.array([1,2,3,4])
array2 = np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
array1 + array2
array3 = np.array([[[1,1,1],[2,2,2],[3,3,3],[4,4,4]],[[1,1,1],[2,2,2],[3,3,3],[4,4,4]]])
array1 + array3
array4 = np.array([1])
array3 + array4


# 正态
a = np.random.normal(size = (2000,))
# 平均值
np.mean(a)
# 方差
np.std(a)
# 求和
np.sum(a)

# 按照维度求和 从0维度开始 就是从最外层开始
a = np.arange(12).reshape(3,4)
np.sum(a, axis=1)

# keepdims 保持维度
np.sum(a, axis=0, keepdims=True)

# 增加维度
a = np.array([1,2,3])
a = a[None,:]  # a =a[None:,]  不变
a = a[:,None]  # 这也可以加维度
np.expand_dims(a, axis=0)

# 减少维度
np.square(a)


# 最大
np.max(a)
np.maximum(a, 5)


np.argmax(a)


np.sort(a)

# 矩阵
mat = np.mat('1,2,3;1,2,3')  # ma 已经删除 使用asmatrix
mat = np.asmatrix('1,2,3;1,2,3')
mat.T  # 转置

# where  返回的是序号
a = np.arange(12).reshape(3, 4)
np.where(a < 4)
np.where(a < 5)
np.where(a < 5, 'a', 'b')

# argwhere
np.argwhere(a < 4)

# extract 得到的是值
np.extract(a < 5, a)

# save 保存 只能保存为npy格式数据
np.save('fff.npy', a)
b = np.load('fff.npy')












