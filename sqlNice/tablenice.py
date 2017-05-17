

class TableNice(object):

    def __init__(self, table_name, columns, connection):
        self.table_name = table_name
        self.columns = columns
        self.connection = connection
        self.cursor = self.connection.cursor()

        self.strfy_columns = ', '.join(self.columns)

    @staticmethod
    def justfy_list(list_of_rows, list_of_widths, fill, separtor_char='|'):

        output_table = []

        for row in list_of_rows:
            list_justfied = []

            for elem, width in zip(row, list_of_widths):
                list_justfied.append(str(elem).rjust(width, fill))

            output_table.append(separtor_char +
                                separtor_char.join(list_justfied) +
                                separtor_char)

        return output_table

    def __getitem__(self, itens):
        columns = [col for col in itens if col in self.columns]
        return TableNice(self.table_name, columns, self.connection)

    def count(self):
        """
        Count all elements of the actual table
        :return:
        Int with count
        """
        pass

    def __str__(self):
        # TODO: Need to change the query building process, NEVER MOCKED
        self.cursor.execute('SELECT ' + self.strfy_columns +
                            ' FROM ' + self.table_name + ' LIMIT 20')
        list_of_rows = self.cursor.fetchall()
        list_of_widths = []

        # Iterate to check largest char in each row
        for col_val, col_name in zip(list_of_rows[0], self.columns):
            len_name = len(str(col_name))
            len_val = len(str(col_val))
            list_of_widths.append(len_name if len_name > len_val else len_val)

        # Justfy the elements
        separator = self.justfy_list([['' for _ in self.columns]], list_of_widths, '-', '+')
        output_rows = self.justfy_list(list_of_rows, list_of_widths, ' ')
        output_header = self.justfy_list([self.columns], list_of_widths, ' ')

        # Build the structure of elements
        output_rows.insert(0, separator[0])
        output_rows.insert(0, output_header[0])
        output_rows.insert(0, separator[0])
        output_rows.append(separator[0])

        return '\n'.join(output_rows)