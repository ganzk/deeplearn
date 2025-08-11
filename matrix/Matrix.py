
# 矩阵打印
def matrix_printf(matrix):
    for row in matrix:
        print(row)


# 矩阵加法
def matrix_add(matrix_a, matrix_b):
    print(matrix_a + matrix_b)


# 矩阵乘法
def matrix_multiplication(matrix_a, matrix_b):
    m = len(matrix_a)
    p = len(matrix_b[0])
    # L = [[0]  * m] * p
    L = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            L[i][j] = sum([matrix_a[i][x] * matrix_b[x][j] for x in range(len(matrix_b))])
    print(L)

# 矩阵乘法 列表推导式
def matrix_multiplication1(matrix_a, matrix_b):
    L = [[sum([matrix_a[i][x] * matrix_b[x][j] for x in range(len(matrix_b))]) for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
    print(L)
