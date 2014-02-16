#coding:utf-8
#для python3
import sys, os

for stream in (sys.stdin, sys.stdout, sys.stderr):
    print(stream.fileno())  # номер дескриптора файла

sys.stdout.write('Some text method1\n')  # без \n следующая операция перезапишет текст,т.к. строка не перенесена

os.write(sys.stdout.fileno(), b'some text method2\n')

file = open(r'some.txt', 'w+')     # можно создать объект файла, а потом получить его дескриптор
file.write('Hello stdio file\n')  # и работать с ним для низкоуровневых операций файла
file.flush()
fd = file.fileno()
os.write(fd, b'Hello descriptor file\n')
file.seek(0)
print(file.read())
file.close()

fd_file = os.open('some.txt', os.O_RDWR)  # создать дескриптор
obj_file = os.fdopen(fd_file)  # и обернуть его объектом файла
print(obj_file.read())

fd_file = os.open('some.txt', os.O_RDWR)  #то же самое
obj_file = open(fd_file, 'r', encoding='utf-8', closefd=False)
print(obj_file.read())

fd_file = os.open('some.txt', os.O_RDWR)  #то же самое
obj_file = open(fd_file, 'r', encoding='utf-8', closefd=True)  # закрыть файловый дескриптор. Зачем?
print(obj_file.read())

print(os.listdir(os.curdir))