

class ColumnNice(object):
    def __init__(self, column_name):
        self.name = column_name
        self.operation = None

    def __str__(self):
        return self.name

    def __lt__(self, other):
        """
        this < other
        :param other:
        :return: string of sql query
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation = str(self) + ' < ' + str(other)
        return self

    def __le__(self, other):
        """
        this <= other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation = str(self) + ' <= ' + str(other)
        return self

    def __eq__(self, other):
        """
        this == other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation = str(self) + ' == ' + str(other)
        return self

    def __ne__(self, other):
        """
        this != other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation = str(self) + ' != ' + str(other)
        return self

    def __gt__(self, other):
        """
        this > other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation = str(self) + ' > ' + str(other)
        return self

    def __ge__(self, other):
        """
        this >= other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation = str(self) + ' >= ' + str(other)
        return self

    def __contains__(self, item):
        """
        this in other
        :param item:
        :return:
        """
        pass

    def __and__(self, other):
        self.operation += ' AND ' + other.operation
        return self

    def __or__(self, other):
        self.operation += ' OR ' + other.operation
        return self

    def like(self, other):
        pass
