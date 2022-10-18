from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from cowpy import cow
from datetime import datetime, timedelta
from pytz import timezone
import pytz

class DoHighlight():
	def __init__(self,text):
		print(highlight(text,PythonLexer(),TerminalFormatter()))

class DoCowSay():
	def __init__(self,text):
		msg = cow.milk_random_cow(text)
		print(msg)

class DoTime():
	def __init__(self,text):
		local_date = datetime.now(pytz.timezone(text))     
		print("{0} {1}".format(local_date.date(), local_date.time()))


