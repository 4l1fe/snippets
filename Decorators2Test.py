# -*- coding: utf-8 -*-
from Decorators2 import rangetest, typetest

if __name__=='__main__':
    print __debug__

    @rangetest(age=(0,120))
    def persinfo(name,age):
        print '%s is %s years old' %(name, age)

    @rangetest(m=(1,12),d=(1,31),y=(0,2009))
    def birthday(m,d,y):
        print 'birthday={0}/{1}/{2}'.format(m,d,y)

    class Person():
        def __init__(self, name, job, pay):
            self.job=job
            self.pay=pay
        @rangetest(percent=(0.0,1.0))
        def give_raise(self, percent):
            self.pay=int(self.pay*(1+percent))

    persinfo('bob smith', 45)
    persinfo(age=33, name='BOBO')
    birthday(5, d=31, y=1963)
#    persinfo(age=121, name='not important')

    bob=Person('bob smoth', pay=100000, job='dev')
    sue=Person('sue jones', 'dev', 100000)
    sue.give_raise(0.10)
    bob.give_raise(0.20)
    print (sue.pay,bob.pay)
#    sue.give_raise(1.10)
#    bob.give_raise(1.20)

    print '='*40
    @typetest(a=int, c=unicode)
    def func(a,b,c,d='default value'):
        print (a,b,c,d)

    func(3,'as',c=u'some')


