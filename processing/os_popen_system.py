import os,sys

output = os.popen('ls -la .').read()
print(output)

output = os.popen('ls -la .').readlines()
print(output)

os.system('python helloshell.py')
output = os.popen('python helloshell.py').readlines()
print(output)
print(sys.argv)
