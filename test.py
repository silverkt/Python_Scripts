<<<<<<< HEAD
class Controller():
    def __init__(self):
        self.x = 'name'
        self.y = 'action'
    def actionOrder(self):
        print('this is actionOrder')

c =  Controller()
print(c.x)
c.actionOrder()


=======
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
>>>>>>> 180ef59791bddddf8267c403fe783083b7e9cc27
