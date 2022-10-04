class Array(object):

	def __init__(self,*args):
		
		self._data = tuple(args)

	def append(self,new_element):
		self._data = self._data + (new_element,)

	def __add__(self, other_array):
		self._data = self._data + other_array.get_data()

	def __len__(self):
		return len(self._data)

	def get_data(self):
		return self._data

	def index(self,index):
		if index in self._data:
			return self._data.index(index)
		else:
			return -1
			
	def __getitem__(self,index):
		return self._data[index]

	def __iter__(self):	
		return iter(self._data)

	def __next__(self):

		self.num = 0
		if self.num < len(self._data):
			self.num+=1
			return self.num
		
	def __str__(self):
		return str(self._data)


a = Array(2,2,3)
a.append(4)
b = Array(5,6)

a+b

print(a)
print(len(a))
print(b[0])
print("\n")
for i in a:
	print(i)

