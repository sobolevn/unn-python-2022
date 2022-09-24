
class Array(object):
	
	#конструктор
	def __init__(self,*args):
		self._data = args;

	#object.append(element)
	def append(self, element):
		self._data = Array(*self._data,element); 

	#object + object
	def __add__(self,other):
		if not isinstance(other,Array):
			print("Правый операнд должен быть типом Array");
			return None;
		else:
			return Array(*self._data,*other._data);

	#object == object
	def __eq__(self,other):
		if not isinstance(other,Array):
			print("Правый операнд должен быть типом Array")
		#elif self._data == other._data: return True;
		else: 
			if (self._data == other._data):
				return True;

		return False;

	#len(object)
	def __len__(self):
		return len(self._data);

	#object.index(other)
	def index(self,other):
		try:
			return self._data.index(other)
		except:
			return -1;

	#object[index]
	def __getitem__(self,index):
		if not isinstance(index,int):
			print("Правый операнд должен быть типом int");
		else: 
			return self._data[index];

	#for i in object:
	def __iter__(self):
		return iter(self._data);

	#print(object)
	def __str__(self):
		return str(self._data);
