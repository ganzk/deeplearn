import time, functools
import math
from functools import *
# from time import *


def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError("参数不对")
    if x > 0:
        return x
    else:
        return -x


def move(x, y):
    x = x + 1
    y = y + 2
    return x, y


def quadratic(a, b, c):
    sqrt = math.sqrt(my_abs(b*b-4*a*c))
    x1 = (-b + sqrt) / (2*a)
    x2 = (-b - sqrt) / (2*a)
    return x1, x2


def power(x, n=2):
    s = 1
    while n >= 1:
        s = s * x
        n = n - 1
    return s


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def calc(*numbers):
    s = 0
    for i in numbers:
        s = s + i
    return s


def fun(x):
    return fun_iter(x, 0)


def fun_iter(x, s):
    if x <= 1:
        return s
    else:
        return fun_iter(x-1, s + x)


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数
        # 成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def gen():
    print("g-1")
    yield
    print('g-2')
    yield
    print('g-3')


# 杨辉三角
def triangles():
    t = [1]
    while True:
        yield t
        t = [m + n for m, n in zip([0]+t, t+[0])]


# 高阶函数
def hi(x, y, f):
    return f(x, y)


def add(x, y):
    return x + y


def normalize(name):
    # reduce(, name)
    pass


def prod(l):
    return reduce(lambda x, y: x * y, l)


def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    t = 10

    def str2(x):
        if x == '.':
            return 0
        else:
            DIGITS[x]
    return reduce(lambda x, y: x + y , map())
    pass


def is_odd(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_palindrome(n):
    s = str(n)
    pass


def re_fun(x):

    def add_():
        nonlocal x
        x = x * x
        return x

    return add_


def create_counter():
    x = 0

    def counter():
        nonlocal x
        x = x + 1
        return x

    return counter


def log(fun):
    @functools.wraps(fun)
    def wrapper(*arg, **kw):
        print("log-name:", fun.__name__)
        return fun(*arg, **kw)
    return wrapper


def log_begin_end(fun):
    @functools.wraps(fun)
    def wrapper(*arg, **kw):
        print("begin call:", fun.__name__)
        # 原函数返回值保存下，返回出去
        result = fun(*arg, **kw)
        print("end call:", fun.__name__)
        return result
    return wrapper


def log_all(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(func.__name__, '执行参数：', *text)
            return func(*args, **kw)
        return wrapper
    return decorator


# @ 后面要加的是一个decorator
# 在 Python 中，任何可调用的对象都可以用作装饰器，只要它接收一个函数或类作为参数，并返回一个函数或类。
# @log_begin_end
# @log
# @log_all('第一个', '第二个', '第三个')
@log_all()
def log_test():
    print("log_test")


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*arg, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*arg, **kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


def queryDocGeneral(query, **kwargs):
    print(kwargs)


# 向量相加
# 向量数乘
# 向量乘法

# 向量的逆
# 向量转置
