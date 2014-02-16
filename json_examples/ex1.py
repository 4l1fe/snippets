#coding:utf-8
import json

data = [dict(a='A', b=(2, 4), c=3.0)]
print 'DATA', repr(data)

data_string = json.dumps(data)
print 'ENCODED', data_string

decoded = json.loads(data_string)
print 'DECODED', decoded

print 'DATA', type(data[0]['a']), type(data[0]['b'])
print 'ENCODED', type(data_string)
print 'DECODED', type(decoded[0]['a']), type(decoded[0]['b']) # будет отличаться от первоначальных типов
                                                              # str/unicode, tuple/list

###===============================================
print '='*30

data = [dict(a=1, b='asdads', c=u'трям', d={1: 'xxx', 2: 'zzz'}, e=([1,2,3], [4,5,6]), f=3.2323)]
print 'data----', data

unsorted_data = json.dumps(data)
print 'unsorted----', unsorted_data

separated_data = json.dumps(data, separators=(',', ':')) # уменьшает число битов, убраны пробелы у разделителй
print 'separated----', separated_data                    # можно менять разделители

sorted_data = json.dumps(data, sort_keys=True, indent=3) # сортировка ключей
print 'sorted----', sorted_data                          # и хороший вывод на нужное количество вхождений
                                                         # увеличивает число битов, не для отправки
###===============================================
print '='*30

data = [ {'a':'A', 'b':(2, 4), 'c':3.0, ('d',):'D tuple' } ]
print 'First attempt'
try:
    print json.dumps(data)
except(TypeError,ValueError), err:
    print 'ERROR:', err
print
print 'Second attempt'
print json.dumps(data, skipkeys=True) # пропускает ключи, которые не являются строкой


