import inspect

def info(object, spacing=10, collapse=1):
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

class Some():
    def la(self):
        print 'method'

if __name__ == '__main__':
#    print inspect.getsource(info)
#    print inspect.getfile(info)
    print inspect.getsourcefile(info)