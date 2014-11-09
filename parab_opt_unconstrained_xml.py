from openmdao.main.api import set_as_top
from openmdao.examples.simple.optimization_unconstrained import OptimizationUnconstrained

from openmdao.main.api import Assembly, Driver, Component, Workflow
import inspect

import sys, traceback

def log(func):
    def wrapped(*qargs, **kwargs):
        #import pdb; pdb.set_trace()
        try:
            stack_level = len(traceback.extract_stack()) - 1
            classname = qargs[0].__class__.__name__
            methodname = func.__name__
            #print "%s<call func='%s.%s' params='%s'>" % (stack_level*' ', classname, methodname, qargs[1:])
            print "%s<call func='%s.%s' id='%d' params='%s'>" % (stack_level*' ', classname, methodname, id(qargs[0]), qargs[1:])
            try:
                return func(*qargs, **kwargs)
            except Exception, e:
                print 'Exception in %s : %s' % (methodname, e)
        finally:
            #pass
            print "%s</call func='%s.%s'>" % (stack_level*' ', classname, methodname)
    return wrapped


model = OptimizationUnconstrained()
set_as_top(model)

#import pdb; pdb.set_trace()

setattr( Assembly, 'run', log( Assembly.run ) )
setattr( Assembly, 'execute', log( Assembly.execute ) )
setattr( Assembly, 'configure_recording', log( Assembly.configure_recording ) )
setattr( Component, 'check_config', log( Component.check_config ) )
setattr( Component, '_pre_execute', log( Component._pre_execute ) )
setattr( Component, 'execute', log( Component.execute ) )
setattr( Component, '_post_execute', log( Component._post_execute ) )
setattr( Component, '_post_run', log( Component._post_run ) )
setattr( Component, 'run', log( Component.run ) )
setattr( Component, '_run_begins', log( Component._run_begins ) )
setattr( Component, '_run_terminated', log( Component._run_terminated ) )
setattr( Driver, 'run', log( Driver.run ) )
setattr( Driver, 'execute', log( Driver.execute ) )
setattr( Driver, 'start_iteration', log( Driver.start_iteration ) )
setattr( Driver, 'continue_iteration', log( Driver.continue_iteration ) )
setattr( Driver, 'pre_iteration', log( Driver.pre_iteration ) )
setattr( Driver, 'run_iteration', log( Driver.run_iteration ) )
setattr( Driver, 'post_iteration', log( Driver.post_iteration ) )
setattr( Workflow, 'run', log( Workflow.run ) )
setattr( Workflow, 'configure_recording', log( Workflow.configure_recording ) )
setattr( Workflow, '_record_case', log( Workflow._record_case ) )

#print "top"
model.run()