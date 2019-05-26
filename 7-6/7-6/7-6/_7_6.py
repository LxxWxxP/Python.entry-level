#-*- coding:utf-8 -*-
def greet(s='world'):
    print 'hello, ', s, '.'

greet()#未输入别的参数时输出默认的值
greet('Bart')#输入了具体值就覆盖了原有值
