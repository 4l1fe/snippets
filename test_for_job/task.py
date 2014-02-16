from xml.etree.ElementTree import ElementTree
from textwrap import indent, dedent
from pprint import pprint
import sqlite3
import pdb

############################################################################################
# Cоздание словаря для удобного форматирования строк, содержащих код генерируемого сценария.
# Cтруктура словаря:
# {'objects':[{'name':'obj1',
#              'fields':[{'name':'field1', 'type':'int'}],
#              'methods':[{'name':'met1', 'return':'int', 'type':'python',
#                          'body':'text',
#                          'arguments':[{'name':'arg1', 'type':'str'}]
#                         }]
#            }]
# }
###########################################################################################
tree = ElementTree(file='template.xml')
SERIALIZED_DATA = {'objects':[]}
for i, OBJ in enumerate(tree.findall('object')):
    SERIALIZED_DATA['objects'].append({'name':OBJ.attrib.get('name'),  # Первоначальная структура, для послед заполнения.
                                       'fields':[],                    # Каждый объект - словарь, как элемент списка.
                                       'methods':[]})

    for FIELD in OBJ.findall('field'):  # Заполняем все поля.
        SERIALIZED_DATA['objects'][i]['fields'].append({'name':FIELD.attrib.get('name'),
                                                        'type':FIELD.attrib.get('type')})

    for METHOD in OBJ.findall('method'):  # заполняем все методы.
        arguments = [dict(name=argum.attrib.get('name'), type=argum.attrib.get('type')) for argum in METHOD.findall('argument')]
        SERIALIZED_DATA['objects'][i]['methods'].append({'name':METHOD.attrib.get('name'),
                                                         'return':METHOD.attrib.get('return'),
                                                         'type':METHOD.attrib.get('type'),
                                                         'body':METHOD.find('body').text,
                                                         'arguments':arguments})  # Методы имеют вложенный список аргументов -
                                                                                  # словарей, как элементов списка,
                                                                                  # его мы сформировали заранее - arguments
print('Словарь:')
pprint(SERIALIZED_DATA)
print('='*50)


###########################################################################################
# Создание/открытие БД для теста.
###########################################################################################
db_source = 'users.db'
conn = sqlite3.connect(db_source)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS user(id INTEGER UNIQUE,
                                                name TEXT UNIQUE,
                                                email TEXT UNIQUE,
                                                login TEXT UNIQUE)''')  # Создали таблицу БД
values = ((1, 'nikolai', 'kol@kol.de', 'kalil'),                        # и значения для теста,
          (2, 'sergei', 'ser@ser.fr', 'sega'),                          # заполнили этими значениями таблицу БД.
          (3, 'pavel', 'pav@pav.it', 'patch'))
for val in values:
    cur.execute('INSERT OR IGNORE INTO user VALUES(?,?,?,?)', val)
conn.commit()

print('Значения из таблицы БД:')
for row in cur.execute('SELECT * FROM user'):
    print(row)
print('='*50)
cur.close()
conn.close()


###########################################################################################
# Шаблон с кодом генерируемого сценария, его форматирование.
# Разбегаются глаза, никакого намёка на ООП, но делаем с некоторым расчетом на масштабирование,
# т.к. предполагается много объектов и методов(аргументов?),
# проще будет подправить любую строчку кода.
###########################################################################################
template = 'import sqlite3\n\n\n'
tab = '    '  # Будем отодвигать этим отступом строки кода, где потребуется.
for OBJ in SERIALIZED_DATA['objects']:

    fields_temp = ''
    for FIELD in OBJ['fields']:  # Формируем в цикле строку для подстановки аргументов(полей) в определение коструктора класса.
        fields_temp += ', {}'.format(FIELD['name'])
    #print('fields:',fields_temp)

    template += 'class {obj_name}:\n\n'.format(obj_name=OBJ['name'])  # Создадим строки кода для конструктора класса/его полей.
    template += indent('def __init__(self{fields_temp}):\n', tab).format(fields_temp=fields_temp)
    for FIELD in OBJ['fields']:
        template += indent('self.{field} = {field}\n', tab*2).format(field=FIELD['name'])

    template += '\n'
    for METHOD in OBJ['methods']:  # Строки кода для каждого метода/его аргументов/его тела.

        arguments_temp = ''  # Формируем строку для подстановки аргументов в определение метода.
        sql_prms_temp = ''   # Строка для подстановки в параметры sql запроса.
        for ARGUMENT in METHOD['arguments']:
            arguments_temp += ', {}'.format(ARGUMENT['name'])
            sql_prms_temp += ', "{0}":{0}'.format(ARGUMENT['name'])
        sql_prms_temp = '{' + sql_prms_temp + '}'
        sql_prms_temp = sql_prms_temp.replace(', ','',1)
        #print('sql_prms:', sql_prms_temp)
        #print('arguments:', arguments_temp)

        method_temp = indent('def {method}(self{args}):', tab).format(method=METHOD['name'], args=arguments_temp)
        if METHOD['type'].lower() == 'python':  # Исходя из типа метода, формируем строки кода его тела.
            template += method_temp
            template += indent(dedent(METHOD['body']), tab*2) + '\n'
        elif METHOD['type'].lower() == 'sql':  # Для метода с типом sql в его тело внесем подключение к БД.
            template += method_temp + '\n'
            template += indent('conn = sqlite3.connect("{db}")\n', tab*2).format(db=db_source)
            template += indent('cur = conn.cursor()\n', tab*2)
            template += indent('res = cur.execute("""{body}""", {prms})\n', tab*2).format(body=METHOD['body'],  # Метод cur.execute()
                                                                                         prms=sql_prms_temp)    # принимает одну сторку sql кода,
            template += indent('res = res.fetchall()\n', tab*2)                                                 # а параметры в стиле - :par1
            template += indent('cur.close()\n', tab*2)
            template += indent('conn.close()\n', tab*2)
            template += indent('return res\n', tab*2)
    template += '\n\n'

print('Сгенерированный код сценария:')
print(template)
print('='*50)

#========================================================================================
# Создание сценария из шаблона.
#========================================================================================
with open('generated_script.py', 'w+', encoding='utf-8') as temp_file:
    temp_file.write(template)


#========================================================================================
# Проверка работы сценария.
#========================================================================================
if __name__ == '__main__':
    from test_for_job import generated_script as g_s
    import inspect


    print('Cписок объектов и их методов:')
    for obj in inspect.getmembers(g_s, inspect.isclass):
        print(obj[0]+':')
        for meth in inspect.getmembers(obj[1], inspect.isfunction):
            print(indent(meth[0], tab))

    ob1 = g_s.ИмяОбъекта(2323, 5.3)
    ob2 = g_s.CustomClass(56, 8.668)
    print('Результаты:')
    print(ob1.ИмяМетода(True, 23))
    print(ob1.НайтиПользователя('sega'), end='\n\n')
    print(ob2.concatenation('once', 'upon', 'a time'))
    print(ob2.find_user('ser@ser.fr'), end='\n\n')
