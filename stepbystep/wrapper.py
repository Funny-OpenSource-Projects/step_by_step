from .tracer import Tracer
import sys

def stepbystep(func):
  def wrapper(*args, **kwargs):

    print(Tracer._CLEAR_SCREEN)

    Tracer.watch(func)
    
    print("enter")
    #pdb.runcall(func, *args, **kwargs)
    sys.stdout.flush()
    
    func(*args, **kwargs)
    # current_level = 0
# 		source = inspect.getsource(func)
# 		source_lines = source.split("\n")
# 		for line in source_lines:
# 			print(line)
  
  return wrapper
