from sys import settrace
from pathlib import Path
import inspect
import traceback
import sys
import time

class Tracer:

  _FOREGROUND_YELLOW = '\x1b[33m'
  _FOREGROUND_RED = '\x1b[31m'
  _FOREGROUND_CYAN = '\x1b[36m'
  _CLEAR_SCREEN = '\x1b[2J'
  _STYLE_RESET_ALL = '\x1b[0m'

  accepted_functions = []
  source_code_col = {}

  def __enter__(self):
    print("enter to context")

  # def __init__(self, func_name):
  #   Tracer.accepted_functions.append(func_name)
  def watch(func):
    # print("watch")
    source_code = inspect.getsource(func)
    Tracer.accepted_functions.append(func.__name__)
    Tracer.source_code_col[func.__name__] = source_code

  def _is_internal_frame(frame):
    #print("frame:", frame.f_code.co_filename)
    caller_filename = inspect.stack()[-1].filename
    
    is_internal =  str(frame.f_code.co_filename) == str(caller_filename)
    if is_internal:
      # print("caller_filename:", caller_filename)
      # print("frame:", frame.f_code.co_filename)
      return True
    else:
      return False

  def find_by_value(array, value):
    return [index for (index , item) in enumerate(array) if item == value]

  def trace(frame, event, arg = None):

    # Tracer._is_internal_frame(frame)

    

    if not Tracer._is_internal_frame(frame):
      return None

    line_no = frame.f_lineno
    code = frame.f_code
    func_name = code.co_name

    filename = code.co_filename
    file_content = open(filename).readlines()
    current_line = file_content[line_no - 1].replace("\n", "")
    
    # if current_line.startswith("@"):
    #   return None
    if func_name not in Tracer.accepted_functions:
      return None
    
    print(Tracer._CLEAR_SCREEN)
    # print(current_line.startswith("@"))
    # print(Tracer.source_code_col[func_name].split("\n"))
    line_in_source_code = Tracer.source_code_col[func_name].split("\n").index(str(current_line))
    # print(line_in_source_code)

    source_code_lines = Tracer.source_code_col[func_name].split("\n")

    sys.stdout.flush()

    for index, source_code_line in enumerate(source_code_lines):
      if not source_code_line.startswith("@"):
        if index == line_in_source_code:
          print(Tracer._FOREGROUND_YELLOW + source_code_line + Tracer._STYLE_RESET_ALL)
        else:
          print(source_code_line)
    
    print("\n")

    variables = frame.f_locals.items()

    for i_variable in variables:
      print(Tracer._FOREGROUND_CYAN + i_variable[0] + ": " + Tracer._FOREGROUND_RED + str(i_variable[1]) + Tracer._STYLE_RESET_ALL)

    time.sleep(0.5)


    # extracts frame code

    #print("current_line:", current_line)
    

    # extracts calling function name
    
    
    
    # print(filename)
    
    # print(code.co_varnames)
    # print(code.co_freevars)
    # print(frame.f_locals.items())
    # extracts the line number
    #print(_is_internal_frame(frame))
    
    
    # print(f"A {event} encountered in \
    # {func_name}() at line number {line_no} ")
    
    return Tracer.trace

settrace(Tracer.trace)