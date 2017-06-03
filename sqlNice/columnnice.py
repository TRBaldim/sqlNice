

class ColumnNice(object):
    def __init__(self, column_name):
        self.name = column_name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        """
        this < other
        :param other:
        :return: string of sql query
        """
        return str(self) + ' < ' + str(other)

    def __le__(self, other):
        """
        this <= other
        :param other:
        :return:
        """
        return str(self) + ' <= ' + str(other)

    def __eq__(self, other):
        """
        this == other
        :param other:
        :return:
        """
        return str(self) + ' == ' + str(other)

    def __ne__(self, other):
        """
        this != other
        :param other:
        :return:
        """
        return str(self) + " != " + str(other)

    def __gt__(self, other):
        """
        this > other
        :param other:
        :return:
        """
        return str(self) + ' > ' + str(other)

    def __ge__(self, other):
        """
        this >= other
        :param other:
        :return:
        """
        return str(self) + ' >= ' + str(other)

    def __contains__(self, item):
        """
        this in other
        :param item:
        :return:
        """
        pass

    def like(self, other):
        pass
