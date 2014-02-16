# -*- coding: utf-8 -*-
#===============================================================
#
#class tracer(object):
#    def __init__(self, func):
#        self.calls=0
#        self.func=func
#    def __call__(self, *args, **kwargs):
#        self.calls+=1
#        print 'call %s to %s' % (self.calls, self.func.__name__)
#        self.func(*args, **kwargs)
#
#    def __get__(self, instance, owner):
#        def wraper(*args, **kwargs):
#            print self
#            print instance
#            print owner
#            print instance.name
#            #типа возвращает вызов себя же , сработает метод __call__
#            return self(instance, *args, **kwargs)
#        return wraper
##декоратор tracer выступает в роли дескриптора, вызывающего метод __get__
##при вызове атрибутов giveRaise, lastName
#class Person():
#    def __init__(self, name, pay):
#        self.name = name
#        self.pay = pay
#    @tracer
#    def giveRaise(self, percent):
#        self.pay *= 1.0 + percent
#    @tracer
#    def lastName(self):
#        return self.name.split()[-1]
#
##слишком запутано
##class wraper():
##    def __init__(self, descrip, subj):
##        self.descrip=descrip
##        self.subj=subj
##    def __call__(self, *args, **kwargs):
##        return self.descrip(self.subj, *args, **kwargs)
#
#
#@tracer
#def spam(a,b,c):
#    print a+b+c
#
#if __name__=='__main__':
#    spam(7,3,2)
#
#    bob = Person('Bob Smith', 50000)
#    sue = Person('Sue Jones', 100000)
#    print(bob.name, sue.name)
#    sue.giveRaise(.10)
#    print (sue.pay)
#    print bob.lastName()
#    print sue.lastName()

#=============================================================
#декорирование функций для определения времени, затраченного на выполнение
#import time
#
#class timer():
#    def __init__(self, func):
#        self.alltime=0
#        self.func=func
#    def __call__(self, *args, **kwargs):
#        start=time.clock()
#        result=self.func(*args, **kwargs)
#        elapsed=time.clock()-start
#        self.alltime+=elapsed
#        print '%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime)
#        return result
#
#@timer
#def listcomp(n):
#    return [x*2 for x in range(n)]
#
#@timer
#def mapcall(n):
#    return map((lambda x: x*2), range(n))
#
#if __name__=='__main__':
#    for function in (listcomp, mapcall):
#        result = function(5)
#        function(50000)
#        function(500000)
#        function(1000000)
#        print result
#        print 'allTime = %s' % function.alltime
#        print '-'*30
#    print 'map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3)
#===========================================================================
#декорирование для всех экземпляров в целом
#instances={}
##если имя такого класс/такой класс уже есть,
##то вернет существующий экземпляр этого класса, не создавая новый
#def getInstance(aClass, *args):
#    if aClass not in instances:
#        instances[aClass]=aClass(*args)
#    return instances[aClass]
#
#def singleton(aClass):
#    def onCall(*args):
#        return getInstance(aClass, *args)
#    return onCall
#
#@singleton
#class Person():
#    def __init__(self, name, hours, rate):
#        self.name=name
#        self.hours=hours
#        self.rate=rate
#    def pay(self):
#        return self.hours*self.rate
#
#@singleton
#class Spam():
#    def __init__(self, value):
#        self.attr=value
#
#if __name__=='__main__':
#    bob=Person('bob',40,10)
#    print bob.name
#    print bob.pay()
#    sue=Person('sue',50,20)
#    print sue.name
#    print sue.pay()
#    x=Spam(33)
#    y=Spam(55)
#    print x.attr
#    print y.attr
#===========================================================================
#экземпляры food=Spam() bob=Person() как бы становятся экземплярами Wrapper(),
#поэтому отрабатывает метод __getattr__
#def Tracer(aClass):
#    class Wrapper():
#        def __init__(self, *args, **kwargs):
#            self.fetches=0
#            self.wrapped=aClass(*args, **kwargs)
#        def __getattr__(self, attrname):
#            print('Trace: '+attrname)
#            self.fetches+=1
#            return getattr(self.wrapped, attrname)
#
#    return Wrapper
#
#@Tracer
#class Spam():
#    def display(self):
#        print('spam'*10)
#
#@Tracer
#class Person():
#    def __init__(self, name, hours, rate):
#        self.name=name
#        self.hours=hours
#        self.rate=rate
#    def pay(self):
#        return self.hours*self.rate
#
#if __name__=='__main__':
##    food=Spam()
##    food.display()
##    print [food.fetches]
##    bob=Person('bob',40,50)
##    print bob.name
##    print bob.pay()
##    print bob.hours
##    sue=Person('sue',100,60)
##    print sue.name
##    print sue.pay()
##    print bob.name
##    print bob.pay()
##    print [bob.fetches, sue.fetches]

##    интересный пример использования декоратора на встроенный класс
#    @Tracer
#    class MyList(list): pass
#    x=MyList([1,2,3,4,5])
#    x.append(77)
#    print(x.wrapped)
#===========================================================================
#декрорирование МЕТОДОВ класса на этапе создания объекта класса
from types import FunctionType


def counter(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {} to {}%s'.format((calls, func.__name__)))
        return func(*args, **kwargs)

    return onCall


def decorateAll(decorator):

    def DecoDecorate(class_):
        for attr, attrval in class_.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(class_, attr, decorator(attrval))
        return class_

    return DecoDecorate

@decorateAll(counter)
class Person: # Применяет декоратор tracer к методам

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]

if __name__=='__main__':
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)
    print(sue.pay)
    print(bob. lastName(), sue.lastName())



