from sys import settrace
import inspect
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
  time_between_steps = 0.5

  def setTimeBetweenSteps(time_between_steps):
    Tracer.time_between_steps = time_between_steps

  def watch(func):
    source_code = inspect.getsource(func)
    Tracer.accepted_functions.append(func.__name__)
    Tracer.source_code_col[func.__name__] = source_code

  def _is_internal_frame(frame):
    caller_filename = inspect.stack()[-1].filename
    return str(frame.f_code.co_filename) == str(caller_filename)

  def find_by_value(array, value):
    return [index for (index , item) in enumerate(array) if item == value]

  def trace(frame, event, arg = None):

    if not Tracer._is_internal_frame(frame):
      return None

    line_no   = frame.f_lineno
    code      = frame.f_code
    func_name = code.co_name
    filename  = code.co_filename

    file_content = open(filename).readlines()
    current_line = file_content[line_no - 1].replace("\n", "")

    if func_name not in Tracer.accepted_functions:
      return None
    
    print(Tracer._CLEAR_SCREEN)

    line_in_source_code = Tracer.source_code_col[func_name].split("\n").index(str(current_line))
    source_code_lines   = Tracer.source_code_col[func_name].split("\n")

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

    time.sleep(Tracer.time_between_steps)
    
    return Tracer.trace

settrace(Tracer.trace)