#!/usr/env/python3

def func1():
    x = 5
    def func2():
        nonlocal x
        x = x + 1
        return x
    return func2

c = func1()
print(c)
x = c()
print(x)
