from openmdao.main.api import set_as_top
from openmdao.examples.simple.optimization_unconstrained import OptimizationUnconstrained

from openmdao.main.api import Assembly, Driver, Component, Workflow
from openmdao.main.systems import SimpleSystem,VarSystem,InVarSystem,EqConstraintSystem, SerialSystem, ParallelSystem, OpaqueSystem
import inspect
import sys, traceback
def log(func,outfile=sys.stdout):
    def wrapped(*qargs, **kwargs):
        try:
            stack_level = len(traceback.extract_stack()) - 2
            line_num_called_from = traceback.extract_stack()[-2][1]
            line_num_of_func = inspect.getsourcelines(func)[1]
            classname_of_self = qargs[0].__class__.__name__
            classname_of_method = func.im_class.__name__
            methodname = func.__name__
            method_args = []
            for anarg in qargs[1:]:
                if hasattr(anarg,"__module__"):
                    method_args.append( anarg.__module__ + "." + anarg.__class__.__name__ )
                else:
                    method_args.append(anarg)
            print >>outfile,'%s<call func="%s.%s(%d)" self="%s(%d)" params="%s">' % (stack_level*' ', classname_of_method, methodname, line_num_of_func, classname_of_self, id(qargs[0]), method_args)
            try:
                return func(*qargs, **kwargs)
            except Exception, e:
                print >>outfile,'Exception in %s.%s : %s' % (classname_of_method,methodname, e)
        finally:
            print >>outfile,"%s</call><!-- func=%s.%s -->" % (stack_level*' ', classname_of_method, methodname)
    return wrapped

f = open('method_with_fix.xml','w')

setattr( SimpleSystem, 'run', log( SimpleSystem.run, outfile=f ) )
setattr( VarSystem, 'run', log( VarSystem.run, outfile=f ) )
setattr( InVarSystem, 'run', log( InVarSystem.run, outfile=f ) )
setattr( EqConstraintSystem, 'run', log( EqConstraintSystem.run, outfile=f ) )
setattr( SerialSystem, 'run', log( SerialSystem.run, outfile=f ) )
setattr( ParallelSystem, 'run', log( ParallelSystem.run, outfile=f ) )
setattr( OpaqueSystem, 'run', log( OpaqueSystem.run, outfile=f ) )
setattr( Assembly, 'execute', log( Assembly.execute , outfile = f ) )
setattr( Assembly, '_pre_execute', log( Assembly._pre_execute , outfile = f ) ) # not showing up !
setattr( Assembly, 'configure_recording', log( Assembly.configure_recording , outfile = f ) )
setattr( Component, 'check_config', log( Component.check_config , outfile = f ) )
setattr( Component, '_pre_execute', log( Component._pre_execute , outfile = f ) ) # not showing up !
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
setattr( Driver, 'configure_recording', log( Driver.configure_recording , outfile = f ) )
setattr( Workflow, 'run', log( Workflow.run , outfile = f ) )
setattr( Workflow, 'configure_recording', log( Workflow.configure_recording , outfile = f ) )
setattr( Workflow, '_record_case', log( Workflow._record_case , outfile = f ) )



model = OptimizationUnconstrained()
set_as_top(model)

#import pdb; pdb.set_trace()

f = open('method.log','w')


#print "top"
model.run()
