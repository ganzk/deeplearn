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