class OrderedDict:
	""" A dictionnary class for which the order counts.

	Args:
		dict: a dictionnary (optionnal)
		**kwargs: keys/values (optionnal)

	"""

	def __init__(self, dictionnary={}, **kwargs):

		self._keys = []
		self._values = []
		
		if (type(dictionnary) is not dict):
			raise TypeError("The argument must be a dictionnary")

		elif (len(dictionnary) > 0):
			self.stock_dict(dictionnary)
		
		if (len(kwargs) > 0):
			self.stock_dict(kwargs)

	def __getitem__(self, item):
		""" Get a value with its key.

		Args:
			item

		"""
		self.check_item(item)
		return self._values[self._keys.index(item)]

	def __setitem__(self, item, value):
		""" Set a new key or edit an existing key.

		Args:
			item: the key
			value: the value
		
		"""
		if item in self._keys:
			self._values[self._keys.index(item)] = value

		else:
			self._keys.append(item)
			self._values.append(value)

	def __delitem__(self, item):
		""" Remove an item from the Ordered Dictionnary.

		Args:
			item: item to remove

		"""
		self.check_item(item)
		del self._values[self._keys.index(item)]
		del self._keys[self._keys.index(item)]

	def __contains__(self, item):
		""" Check if the Ordered Dictionnary contains the item
		as a key.

		Args:
			item: item to verify

		"""
		try:
			return self.check_item(item) # Return true if the item exists. Raise an exception if it doesn't.
		except:
			return False

	def __len__(self):
		""" Check the length of the Ordered Dictionnary. """

		return len(self._keys)

	def __repr__(self):
		""" Return all keys / values in a good shape. """

		mystr = "{" # Begenning of the string
		
		for key in self._keys: # Parse all keys of self._keys
			mystr += str(key)
			mystr += ": "
			mystr += str(self._values[self._keys.index(key)])
			mystr += ", "
		
		if (len(self._keys) > 0):
			mystr = mystr[:-2] # Remove the last comma and space if the dict is not empty.
		
		mystr += "}" # End of the string

		return mystr

	def __iter__(self):
		""" Iterator of the Ordered Dictionnary. It's based
		on the order of the keys. It returns the keys.
		A Generator is used to generate the iterator.

		"""
		for key in self._keys:
			yield key

	def __add__(self, ordict):
		""" Add two Ordered Dictionnaries together.

		Args:
			ordict: the new Ordered Dictionnary to add

		"""
		for key in ordict:
			self._keys.append(key)
			self._values.append(ordict[key])

		return self

	def stock_dict(self, dictionnary):
		""" Stock a dictionnary in the intern keys / values object

		Args:
			dict: a dictionnary

		"""
		if type(dictionnary) is not dict:
			raise TypeError("The argument must be a dictionnary")

		for key in dictionnary:
			self._keys.append(key)
			self._values.append(dictionnary[key])

	def check_item(self, item):
		""" Check if an item exists.

		Args:
			item: item to verify

		"""
		if (item not in self._keys):
			raise ValueError("[{}] doesn't exist.".format(item))

		else:
			return True

	def sort(self):
		""" Sort the Ordered Dictionnary by the keys. """
		tempdict = {}
		for key in self._keys:
			tempdict[key] = self._values[self._keys.index(key)]

		self._keys.sort() # Sort the keys

		newvalues = []
		for key in self._keys:
			newvalues.append(tempdict[key])

		self._values = list(newvalues)

	def reverse(self):
		""" Reverse the Order of the Ordered Dictionnary. """
		tempdict = {}
		for key in self._keys:
			tempdict[key] = self._values[self._keys.index(key)]

		newkeys = []
		for key in self._keys:
			newkeys.insert(0,key)
		self._keys = list(newkeys)

		newvalues = []
		for key in self._keys:
			newvalues.append(tempdict[key])
		self._values = list(newvalues)

	def keys(self):
		""" Return the keys of the Ordered Dictionnary. """
		return self._keys

	def values(self):
		""" Return the values of the Ordered Dictionnary. """
		return self._values

	def items(self):
		""" Return all the couples key/value of the Ordered Dictionnary. """
		templist = []
		for key in self._keys:
			templist.append((key, self._values[self._keys.index(key)]))
		return templist