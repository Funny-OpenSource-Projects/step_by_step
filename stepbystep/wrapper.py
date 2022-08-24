from .tracer import Tracer
import sys

def stepbystep_wrapper(time_between_steps=0.5):

  def Inner(func):
  
    def wrapper(*args, **kwargs):
      Tracer.watch(func)
      Tracer.setTimeBetweenSteps(time_between_steps)
      sys.stdout.flush()
      func(*args, **kwargs)
    return wrapper
  return Inner