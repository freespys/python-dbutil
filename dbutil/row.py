from pprint import saferepr

class row(object):
    def __init__(self, desc, data):
        object.__init__(self)
        self.__data = dict(zip([x[0] for x in desc], data))

    def __getitem__(self, key):
        return self.__data[key]

    def __getattr__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            raise AttributeError

    def __repr__(self):
        return "row(%s)" % saferepr(self.__data)
