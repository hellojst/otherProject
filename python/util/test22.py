import random
import sys
import test
a='bestworld'
print(a)
print(a[1:3])
print(a[-1])
tuple = (1, '2', 3, 'g')
print(3 * random.random())
print(tuple)
list = [1,'r', 'd','r',[1]]
print(list)
list[-1]=['replace','hhh']
print(list)
print('我叫%s，今年%d岁'%('stjia',26))
print (sys.path)
print('s')

sys.path.append("E:\project\python\mypython")
print(sys.path)
print('aaaaa')

def fib(a):
    print(a)