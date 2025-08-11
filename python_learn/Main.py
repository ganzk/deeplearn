from my_abs import my_abs
from my_abs import *
from collections.abc import Iterable
import os
from functools import reduce

# print("hhhhhhh","dsfadf",'fffff',"""adadadsad""")
# print("""rqwerqwer
# rqerqewr""")
# print('klkll')
# print(2**10)
# print(2*10)
# print(2)
# print(2**-2)
# # name = input()
# # print(name)
# i = 1000_1000_000_000_000_000_00000000_000000000000_00000000000_00000000000_074814812849
# print(i ** 10)
# f = 0.121200000000000313212300000000000012312300000000013123_123123123123
# print(f**10)
# print("\"")
# print(r'dadfa\\\\\\\\\\\\\\\\\\\\\\')
# print(True and False)
# if i < 90:
#     print("大于90")
#     print("hahahahahahahah")
#     print("=================")
# # else if i > 100:
# #     print("afadfadf")
# print("llllll")
# s = "adsad"
# s1 = "llll"
# s3 = False
# s4 = 10
# s4 = s4 + 9
# print(s + s1)
# print(s3+s4)
# print(s4)
#
# a = "wwww"
# b = a
# a = "pppp"
# print(b)
# print(a)
#
# ss = len("ppppp")
# print(ss)
#
# print(chr(520))
#
# print(ord('增'))
#
# print('中文'.encode('utf-8'))
#
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#
# p = "九磅十五便士"
# j = "大家"
# print('衬衫的价格是：%s,欢迎%s购买'%(p, j))

# 数组
# strs = ["asdfa", "werqwe", "adadsadd"]
# print(strs)
# print(len(strs))
# print(strs[-1])
# print(strs.append("llll"))
# print(strs.insert(0, "oooo"))
# print(strs.pop(0))
# strs.append(["hhh", "ttt", "uuu"])
# print(strs[-1][2])
# print(strs)
#
# tup = ("llll", "mmmm", "nnnn")
# tup = ("yyy",)
# print(tup)

# 判断
# str = "12"
# i = int(str)
# # i = 11
# if i < 10:
#     print("小于10")
# elif 10 < i < 20:
#     print("大于10小于20")
# else:
#     print("大于20")
#
# # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# x = 10
# if x:
#     print("llll")
#
# # 模式匹配
# match x:
#     case 0:
#         print("0")
#     case 10:
#         print(10)
#     case _:
#         print("other")

# 循环
# sum = 0;
# xs = [1,2,3,4]
# for x in xs:
#     print(x)
#
# xs = range(101)
# for x in xs:
#     sum  = sum + x
# print(sum)
#
# x = 1
# while x < 10:
#     print("llll")
#     x = x + 1

# 字典
# m = {'test': 'hhh', 'testA': 'kkk', 'testB': 'mmm'}
# m1 = {'test': 'hhh', 'test': 'kkk', 'testB': 'mmm'}
# print(m['test'])
# m['testA'] = 10
# print('test' in m)
# print(m.get('hhh', 'ooo'))
# print(m.pop('test'))
# print(m)
# print(m1)
#
# # set
# a = set([1,2,3,4,5,6,6,5,4,3,2,1])
# a1 = {1,2,0,9,8,7}
# print(a)
# print(a & a1)
# print(a | a1)

# 函数
# print(abs(-1))
# print(max(1,2,4,0,3))
# a = abs
# print(a(-10))
# print(my_abs(-11))


# import my_abs
# 先定义再使用
# print(my_abs(-9))
# print(quadratic(2, 3, 1))
# print(power(2, 10))
# s = [1, 2, 3]
# print(calc(1, 2, 3))
# print(calc(*s))
# # print(power(2, n=9))
# city = 9
# person("gzk", 12, city = 'beijing', sex = 'nan')

# 递归  python没有进行尾递归优化
# print(fun(1000000))


# 切片
# l = ['o', 'p', 'q', 'r', 's']
# s = l[-4:]
# print(s)
#
# s = "opqrs"
# print(s[:3])
# print(s[-1:])

# 迭代
# print(isinstance('123', Iterable))
# print(isinstance(123, Iterable))
# print(isinstance(['1', '2', '3'], Iterable))

# m = {"a": 1, 'b': 2, 'c': 3}
# for k, v, i in enumerate(m.items()):
#     print(k, v, i)

# for i, j in enumerate(['a', 'b', 'c']):
#     print(j, i)

# 列表生成式
# print(list(range(1, 11)))
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n + d for m in 'ABC' for n in 'abc' for d in '123'])
# print([m for m in os.listdir('.')])
#
# L = ['Hello', 'World', 18, 'Apple', None]
# L2 = [m.lower() for m in L if isinstance(m , str)]
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 生成器  必须是列表生成式 才可以
# 成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# g = (x for x in "abcdef")
# print(next(g))
# a = gen()
# next(a)
# next(a)
# for n in a:
#     pass
# m = fib(9)
# for n in m:
#     print(n)

# t = [1]
# t1 = [0, 1, 0]
# print([m + n for m in t for n in t1])

# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 函数式编程
# f = abs
# print(f(-10))

# abs = power(2)
# print(abs(2))

# power不需要带括号
# x = power()
# print(hi(2, 3, x))

# r = map(power, [1, 2, 3, 4, 5])
# print(list(r))
# f = reduce(add, [1, 2, 3, 4, 5])
# print(f)



# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
#

# filter
# print(list(filter(is_odd, [1, 2, 3, 4, 5])))
#
# l = filter(is_odd, [1, 2, 3, 4, 5])
# print(next(l))


# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# x = re_fun(8)
# print(x())
#
# counterA = create_counter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = create_counter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 匿名函数
# f = lambda x : x * x
# print(f(5))

# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(lambda x : x%2 == 1, range(1, 20)))
#
# print(L)

# 装饰器
# f = add
# print(f.__name__)
# log_test()
# print(log_test.__name__)

# 偏函数


# ================模块====================
# import hello


# hello.test()


# ================面向对象=================
import school as s

# 创建实例
# stu = s.Student()
# print(stu)
# print(s.Student)
# stu.name = "gzk"
# print(stu.name)

# stu = s.Student("gzk_1", 26)
# print(stu.name)
# print(stu.age)
# stu.print_age()
#
# tea = s.Teacher("gan", 40, "语文")
# # print(tea.age)
# print(tea._Teacher__age)


# 继承和多态
import animal

cat = animal.Cat()
cat.run()

