class Root(object):
    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        if key   == 'activity':
            return Activity()
        elif key == 'quote':
            return AiwfQuotes()

class Activity(object):
	"""docstring for Activity"""
	__name__   = ''
	__parent__ = Root

	def __init__(self):
		pass

	def __getitem__(self, key):
		if key:
			return ActivityName(key)
		raise KeyError


class ActivityName(object):
	"""docstring for ActivityName"""
	def __init__(self, name):
		self.__name__ = name		


class AiwfQuotes(object):
    """Returns a pool of wonderful quotes from the public"""
    def __init__(self, request):
        self.request    = request
        self.settings   = request.registry.settings
        self.collection = request.db['quotes']

    # get a list of quotes
    def get_quotes(self, num_of_quotes = 3):
        quotes = self.collection.find( {}, {'quote': 1, 'fullname': 1} ) 
        return { quotes }

    # return number of quotes 
    def __len__(self): 
        return { self.collection.count() }

