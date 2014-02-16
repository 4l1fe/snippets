#coding: utf-8
import sys
import traceback
import example
import inspect
from pprint import pprint


#for name, data in inspect.getmembers(example):
#    if name.startswith('__'):
#        continue
#    print name, data


#for name, data in inspect.getmembers(example, inspect.isclass):
#    print name, data


#pprint(inspect.getmembers(example.A), width=65)
#pprint(inspect.getmembers(example.A, inspect.ismethod), width=65)
#pprint(inspect.getmembers(example.B, inspect.ismethod), width=65)
#print inspect.getdoc(example.B)
#print inspect.getcomments(example) # выводятся не все коменты, только первые и без пустых строк между ними...
#print inspect.getsource(example.A.get_name)
#pprint(inspect.getsourcelines(example.B)
#pprint(inspect.getargspec(example.module_level_function))


#for args, kwds in[ # показывает как с каждым шагом заполняются аргументы функции
#    (('a',),               {'unknown_name':'value'}),
#    (('a',),               {'arg2':'value'}),
#    (('a', 'b', 'c', 'd'), {}),
#    ((),                   {'arg1':'a'}),]:
#    print args, kwds
#    print '========='
#    callargs = inspect.getcallargs(example.module_level_function,
#                                    *args,**kwds)
#    pprint(callargs, width=100)
#    example.module_level_function(**callargs)
#    print '========='


def recurse(limit):
    local_variable = '.'*limit
    print limit, inspect.getargvalues(inspect.currentframe()) # фрэйм показывает текущее состояние памяти ?
    if limit <= 0:
        return
    recurse(limit-1)
    return
recurse(2)


#print inspect.stack() # возвращает frame, filename, line_num, func, src_code, src_index
#try:
#    s = 's'/2
#except:
#    print inspect.trace()
#    traceback.print_stack()
#    traceback.print_exc()
#print inspect.getouterframes(inspect.currentframe())
#print inspect.getouterframes(sys._getframe()) # currentframe() вызывает _getframe()
