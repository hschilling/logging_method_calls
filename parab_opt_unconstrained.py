from openmdao.main.api import set_as_top
from openmdao.examples.simple.optimization_unconstrained import OptimizationUnconstrained

from openmdao.main.api import Assembly, Driver
import inspect

import sys, traceback

def log(func):
    def wrapped(*qargs, **kwargs):
        #import pdb; pdb.set_trace()
        try:
            stack_level = len(traceback.extract_stack()) - 1
            classname = qargs[0].__class__.__name__
            methodname = func.__name__
            print "%sEntering %s.%s with parameters %s" % (stack_level*' ', classname, methodname, qargs[1:])
            try:
                return func(*qargs, **kwargs)
            except Exception, e:
                print 'Exception in %s : %s' % (methodname, e)
        finally:
            #pass
            print "%sExiting %s.%s" % (stack_level*' ', classname, methodname)
    return wrapped


model = OptimizationUnconstrained()
set_as_top(model)

#import pdb; pdb.set_trace()

setattr( Assembly, 'run', log( Assembly.run ) )
setattr( Driver, 'run', log( Driver.run ) )

print "top"
model.run()
