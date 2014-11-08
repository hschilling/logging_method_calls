import inspect

def log(func):
    def wrapped(*args, **kwargs):
        try:
            print "Entering: [%s] with parameters %s" % (func.__name__, args)
            try:
                return func(*args, **kwargs)
            except Exception, e:
                print 'Exception in %s : %s' % (func.__name__, e)
        finally:
            print "Exiting: [%s]" % func.__name__
    return wrapped

def trace(cls):
    for name, m in inspect.getmembers(cls, inspect.ismethod):
        setattr(cls,name,log(m))
    return cls

#@trace
class X(object):
    def first_x_method(self):
        print 'doing first_x_method stuff...'
    def second_x_method(self):
        print 'doing second_x_method stuff...'

x=X()
import pdb; pdb.set_trace()
x.first_x_method()
x.second_x_method()