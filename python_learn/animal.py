#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
继承多态
"""


class Animal(object):

    def run(self):
        print(self)
        print('Animal is running...')

    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass

