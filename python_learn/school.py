#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象
"""


__author__ = 'gzk'


class People(object):
    # 相当于构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法
    def print_age(self):
        print(self.age)


class Student(object):
    # 相当于构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法
    def print_age(self):
        print(self.age)






