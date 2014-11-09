from openmdao.main.api import set_as_top
from openmdao.examples.simple.optimization_unconstrained import OptimizationUnconstrained

from openmdao.main.api import Assembly, Driver, Component, Workflow
import inspect

import sys, traceback

def log(func,outfile=sys.stdout):
    def wrapped(*qargs, **kwargs):
        #import pdb; pdb.set_trace()
        try:
            stack_level = len(traceback.extract_stack()) - 2
            classname = qargs[0].__class__.__name__
            methodname = func.__name__
            #print "%s<call func='%s.%s' params='%s'>" % (stack_level*' ', classname, methodname, qargs[1:])
            print >>outfile,"%s<call func='%s.%s' id='%d' params='%s'>" % (stack_level*' ', classname, methodname, id(qargs[0]), qargs[1:])
            try:
                return func(*qargs, **kwargs)
            except Exception, e:
                print >>outfile,'Exception in %s : %s' % (methodname, e)
        finally:
            #pass
            print >>outfile,"%s</call func='%s.%s'>" % (stack_level*' ', classname, methodname)
    return wrapped


model = OptimizationUnconstrained()
set_as_top(model)

#import pdb; pdb.set_trace()

f = open('method.log','w')

setattr( Assembly, 'run', log( Assembly.run, outfile=f ) )
setattr( Assembly, 'execute', log( Assembly.execute , outfile = f ) )
setattr( Assembly, 'configure_recording', log( Assembly.configure_recording , outfile = f ) )
setattr( Component, 'check_config', log( Component.check_config , outfile = f ) )
setattr( Component, '_pre_execute', log( Component._pre_execute , outfile = f ) )
setattr( Component, 'execute', log( Component.execute , outfile = f ) )
setattr( Component, '_post_execute', log( Component._post_execute , outfile = f ) )
setattr( Component, '_post_run', log( Component._post_run , outfile = f ) )
setattr( Component, 'run', log( Component.run , outfile = f ) )
setattr( Component, '_run_begins', log( Component._run_begins , outfile = f ) )
setattr( Component, '_run_terminated', log( Component._run_terminated , outfile = f ) )
setattr( Driver, 'run', log( Driver.run , outfile = f ) )
setattr( Driver, 'execute', log( Driver.execute , outfile = f ) )
setattr( Driver, 'start_iteration', log( Driver.start_iteration , outfile = f ) )
setattr( Driver, 'continue_iteration', log( Driver.continue_iteration , outfile = f ) )
setattr( Driver, 'pre_iteration', log( Driver.pre_iteration , outfile = f ) )
setattr( Driver, 'run_iteration', log( Driver.run_iteration , outfile = f ) )
setattr( Driver, 'post_iteration', log( Driver.post_iteration , outfile = f ) )
setattr( Workflow, 'run', log( Workflow.run , outfile = f ) )
setattr( Workflow, 'configure_recording', log( Workflow.configure_recording , outfile = f ) )
setattr( Workflow, '_record_case', log( Workflow._record_case , outfile = f ) )

#print "top"
model.run()
