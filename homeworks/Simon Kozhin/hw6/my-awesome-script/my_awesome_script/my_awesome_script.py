import argparse


ARG_HELP_FUNC = '''cowsay "Some text" - you get a cow what say your text ***
              highligh "*Your code*" - you get a highlighted code **********
              time Region/City - you get a real time in this city '''

ARG_HELP_PARAM = 'the argument of function ("Your text"), "*Your code*" etc.'



def main():
  parser = argparse.ArgumentParser(description='Ultra super useful script')
  parser.add_argument('function',  help=ARG_HELP_FUNC)
  parser.add_argument('param_of_func', help=ARG_HELP_PARAM)
  args = parser.parse_args()

  # if args.function == 'cowsay':
  #   cowsay(args.param_of_func)
  # if args.function == 'highligh':
  #   highligh(args.param_of_func)
  # if args.function == 'time':
  #   time(args.param_of_func)
  FOO.get(args.function)(args.param_of_func)

def cowsay(param):
  from cowpy import cow

  msg = cow.milk_random_cow(param)
  print(msg)


def highligh(param):
  from pygments import highlight
  from pygments.lexers import PythonLexer
  from pygments.formatters import TerminalFormatter

  lexer = PythonLexer()
  formatter = TerminalFormatter(linenos = True)
  print(highlight(param, lexer, formatter)) 
  

def time(param):
  from datetime import datetime
  from pytz import timezone

  dt_format = "%d-%m-%Y %H:%M:%S"
  timedate = datetime.now(timezone(param))
  print('Дата и время выбранной зоны: \n', timedate.strftime(dt_format))


FOO = {
    'cowsay':  cowsay,
    'highligh':  highligh,
    'time':  time, 
  }