# -*- coding: utf-8 -*-
#==================================================================
##показывает метод делегирования и запрашиваемый атрибут
#traceMe = False
#def trace(*args):
#    if traceMe: print '[' + ' '.join(map(str, args)) + ']'
#
##закрывает доступ к частным атрибутам,
##указанным в аргументах *privates
#def Private(*privates):
#
#    def onDecorator(aClass):
#
#        class onInstance():
#            #при создании декоратора создаётся экземпляр декорированного класса
#            #и записывается в self.wrapped
#            def __init__(self, *args, **kwargs): #args, kwargs нужны при передаче classA=decorator(privates)(classA)(args, kwargs)
#                self.wrapped=aClass(*args, **kwargs)
#
#            #при получении атрибута проверяет на вхождение в приватные
#            #выдаёт ошщибку при совпадении
#            def __getattr__(self, attr):
#                trace('get:', attr)
#                if attr in privates:
#                    raise TypeError('private attribure fetch. '+attr)
#                else:
#                    return getattr(self.wrapped, attr)
#
#            def __setattr__(self, attr, value):
#                trace('set:',attr,value)
#                #для предотвращения зацикливания, когда
#                #значение атрибута попадет на экземпляр класса(self.wrapped)
#                if attr == 'wrapped':
#                    self.__dict__[attr]=value
#                elif attr in privates:
#                    raise TypeError('private attribure fetch. '+attr)
#                else:
#                    setattr(self.wrapped, attr, value)
#
#        return onInstance
#
#    return onDecorator
#
#if __name__=='__main__':
#    traceMe=True
#    #декоратор не перехватывает обращение к частным атрибутам
#    #внутри класса Doubler, но перехватывает извне,
#    #потому что реализован механизм делегирования в перегруженных методах __getattr__, __setattr_
#    #но не наследование
#    @Private('data', 'size')#data, size -имена частных атрибутов
#    class Doubler():
#        def __init__(self, label, start):
#            self.label=label
#            self.data=start
#        def size(self):
#            return len(self.data)
#        def double(self):
#            for i in range(self.size()):
#                self.data[i]=self.data[i]*2
#        def display(self):
#            print '%s => %s' %(self.label, self.data)
#
#    x=Doubler('x is ', [1,2,3])
#    y=Doubler('y is ', [-10,-20,-30])
#
#    print x.label
#    x.display(); x.double(); x.display()
#
#    print y.label
#    y.display(); y.double(); y.label='spam'; y.display()
#    #закрывает доступ при этих обращениях
#    print(x.size)
#    print(x.data)
#    x.data = [1, 1, 1]
#    x.size = lambda S: 0
#    print(y.data)
#    print(y.size)
#==============================================================================
#реализация декораторов доступа только к атрибутам, объявленным публичными(остальные частные),
#либо к атрибутам, НЕ объявленным частными(остальные публичные)
#traceMe=False
#def trace(*args):
#    print '['+' '.join(map(str,args))+']'
#
#def accessControl(failIF):
#    def onDecorator(aClass):
#        class onInstance():
#            def __init__(self, *args, **kwargs):
#                self.__wrapped=aClass(*args, **kwargs)
#            def __getattr__(self, attr):
#                trace('get: ', attr)
#                if failIF(attr):
#                    raise TypeError('private attribure fetch. '+attr)
#                else:
#                    return getattr(self.__wrapped, attr)
#            def __setattr__(self, attr, value):
#                trace('set:', attr, value)
#                if attr=='_onInstance__wrapped':
#                    self.__dict__[attr]=value
#                elif failIF(attr):
#                    raise TypeError('private attribure fetch. '+attr)
#                else:
#                    setattr(self.__wrapped, attr, value)
#        return onInstance
#    return onDecorator
#
#def Private(*attributes):
#    return accessControl(failIF=(lambda attr:attr in attributes))
#
#def Public(*attributes):
#    return accessControl(failIF=(lambda attr:attr not in attributes))
#
#if __name__=='__main__':
#    @Private('age')
#    class Person1():
#        def __init__(self, name, age):
#            self.name=name
#            self.age=age
#
#    x=Person1('bob', 40)
##    print x.name;x.name='sue'; print x.name
##    #не даёт доступа к частному атрибуту, указанному в декораторе Private('age')
##    print x.age; x.age=777
#
#    @Public('name')
#    class Person2():
#        def __init__(self, gender, name, age):
#            self.name=name
#            self.gender=gender
#            self.age=age
#
#    y=Person2('man','Tom', 41)
#    print y.name;y.name='sue'; print y.name
#    #не даёт доступа к НЕ публичным атрибутам, указанным в декораторе Public('name')
#    print y.age; y.age=777; print y.gender
#===============================================================================================
#проверка значений позиционных
#аргументов на вхождение в заданный диапазон
trace=True

#позволяет задавать значения диапазона проверки вхождения как по именованным,
#так и по позиционным, и соттветственно с гибким порядком аргументов...

def rangetest(**argschecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            import sys
            code=func.__code__
            allargs=code.co_varnames[:code.co_argcount]
            funcname=func.__name__
            def onCall(*pargs, **kwargs):
                positionals=list(allargs)
                positionals=positionals[:len(pargs)]
                for (argname,(low, high)) in argschecks.items():
                    if argname in kwargs:
                        if kwargs[argname]<low or kwargs[argname]>high:
                            errormsg='{0} argument "{1}" not in {2}..{3}'
                            errormsg=errormsg.format(funcname, argname, low, high)
                            raise TypeError(errormsg)
                    elif argname in positionals:
                        position=positionals.index(argname)
                        if pargs[position]<low or pargs[position]>high:
                            errormsg='{0} argument "{1}" not in {2}..{3}'
                            errormsg=errormsg.format(funcname, argname, low, high)
                            raise TypeError(errormsg)
                    else:
                        if trace:
                            print ('Argument {0} is defaulted'.format(argname))
                return func(*pargs, **kwargs)

            return onCall
    return onDecorator

#==========================================================================
#проверка типов на основе декоратора
def typetest(**argschecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            import sys
            code=func.__code__
            allargs=code.co_varnames[:code.co_argcount]
            funcname=func.__name__
            def onCall(*pargs, **kwargs):
                positionals=list(allargs)[:len(pargs)]
                for (argname, type) in argschecks.items():
                    if argname in kwargs:
                        if not isinstance(kwargs[argname],type):
                            errormsg='не правильный тип именованного аргумента'
                            raise TypeError(errormsg)
                    elif argname in positionals:
                        position=positionals.index(argname)
                        if not isinstance(pargs[position], type):
                            errormsg='не правильный тип позиционного аргумента'
                            raise TypeError(errormsg)
                    else:
                        if trace:
                            print ('Argument {0} is defaulted'.format(argname))
                return func(*pargs, **kwargs)

            return onCall
    return onDecorator














