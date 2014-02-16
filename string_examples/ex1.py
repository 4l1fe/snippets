#coding: utf-8
import string
import re

#[===============================]
s = 'some bla translate this sentence'
print string.capwords(s)

#[===============================]
s = 'podstavlyat vmesto bukv cifri'
table = string.maketrans('oias', '01@5')
print string.translate(s, table)

#[===============================]
values = {'first': '123',
          'second': 'strochku',
          'third': 'prawn'}
template = string.Template('podstavit $first v $second s okrujaushim tekstom sea fish-${third}_${third}"s')
print template.substitute(values)       # вызовет ошибку при отсутсвии переменных
print template.safe_substitute(values)  # выведет строку как есть, в месте ошибки

#[===============================]
class MyTemplate(string.Template):
    delimiter = '#'
    idpattern = '[a-z]+_[a-z]+'
template = MyTemplate('delimiter: ## || replaced: #with_underscore || ignored: #withoutunderscore')
values = {'with_underscore': 'zzzZZZ',
          'withoutunderscore': '999_999'}  # будет проигнорировано, не соотв шаблоеу idpattern(нет подчеркивания)
print template.safe_substitute(values)     # поэтому используется safe_substitute()

#[===============================]
template = string.Template('$var')
print template.pattern.pattern

#[===============================]
class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
     \{\{(?:
     (?P<escaped>\{\{)|
     (?P<named>[_a-z][_a-z0-9]*)\}\}|
     (?P<braced>[_a-z][_a-z0-9]*)\}\}|
     (?P<invalid>)
     )
     '''
template = MyTemplate('''{{{{{{var}}''')
print template.pattern.findall(template.template)
print template.safe_substitute(var='replacement')