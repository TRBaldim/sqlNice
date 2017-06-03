

class ColumnNice(object):
    def __init__(self, column_name, column_type):
        self.name = column_name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass
