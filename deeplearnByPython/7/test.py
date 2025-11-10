import numpy as np
import matplotlib.pyplot as plt
import math

# 示例：两组数据的方差比较
data_low_var = np.array([4.9, 5.0, 5.1, 5.0, 5.1])      # 低方差
data_high_var = np.array([1.0, 3.0, 7.0, 9.0, 5.0])    # 高方差

mean_low = np.mean(data_low_var)
mean_high = np.mean(data_high_var)

print(f"低方差数据: {data_low_var}")
print(f"平均值: {mean_low:.2f}, 方差: {np.var(data_low_var):.2f}")

print(f"\n高方差数据: {data_high_var}")
print(f"平均值: {mean_high:.2f}, 方差: {np.var(data_high_var):.2f}")


# 绘制数据分布
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.scatter(data_low_var, [0]*len(data_low_var), s=100, alpha=0.7)
plt.axvline(mean_low, color='red', linestyle='--', label=f'平均值: {mean_low:.2f}')
plt.title('低方差数据 - 数据点集中')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(data_high_var, [0]*len(data_high_var), s=100, alpha=0.7)
plt.axvline(mean_high, color='red', linestyle='--', label=f'平均值: {mean_high:.2f}')
plt.title('高方差数据 - 数据点分散')
plt.legend()

plt.tight_layout()
plt.show()