

class ColumnNice(object):
    def __init__(self, column_name, table):
        self.name = column_name
        self.representation = column_name
        self.operation = []
        self.table = table

    def __str__(self):
        return self.representation

    def __repr__(self):
        return self.representation

    def __lt__(self, other):
        """
        this < other
        :param other:
        :return: string of sql query
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation.append(str(self) + ' < ' + str(other))
        return self

    def __le__(self, other):
        """
        this <= other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation.append(str(self) + ' <= ' + str(other))
        return self

    def __eq__(self, other):
        """
        this == other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation.append(str(self) + ' == ' + str(other))
        return self

    def __ne__(self, other):
        """
        this != other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation.append(str(self) + ' != ' + str(other))
        return self

    def __gt__(self, other):
        """
        this > other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation.append(str(self) + ' > ' + str(other))
        return self

    def __ge__(self, other):
        """
        this >= other
        :param other:
        :return:
        """
        if type(other) == str:
            other = "\"" + other + "\""

        self.operation.append(str(self) + ' >= ' + str(other))
        return self

    def is_in(self, items):
        """
        this in other
        :param items: should be a iterable object
        :return:
        """
        if not hasattr(items, '__iter__'):
            raise TypeError('Object ' + type(items).__name__ + ' is not Iterable')
        # fixing strings to ran at sqlite
        casted_items = map(lambda elem: str(elem) if type(elem) != str else '\"' + str(elem) + '\"', items)

        self.operation.append(str(self) + ' IN (' + ', '.join(elem for elem in casted_items) + ')')
        return self

    def __and__(self, other):
        """
        this and other
        :param other: Should be a columnNice object
        :return:
        """
        if other is self:
            count_position = 1
            while count_position <= len(self.operation):
                if self.operation[count_position] != 'AND' and self.operation[count_position] != 'OR':
                    self.operation.insert(count_position, 'AND')
                    break
                count_position += 2
        else:
            self.operation.append('AND')
        return self

    def __or__(self, other):
        """
        this or other
        :param other: Should be a columnNice object
        :return:
        """
        if other is self:
            count_position = 1
            while count_position <= len(self.operation):
                if self.operation[count_position] != 'AND' and self.operation[count_position] != 'OR':
                    self.operation.insert(count_position, 'OR')
                    break
                count_position += 2
        else:
            self.operation.append('OR')
        return self

    def like(self, other):
        """
        this like other
        :param other: other should be a string object
        :return:
        """
        self.operation.append(str(self) + ' LIKE \"%' + str(other) + '%\"')
        return self

    def alias(self, name):
        self.name = name
        self.representation += ' AS ' + name
        return self

    def set_function(self, function_string):
        #self.name = function_string
        self.representation = function_string

    def restore_default_name(self):
        self.representation = self.name
