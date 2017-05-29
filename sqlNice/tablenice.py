

class TableNice(object):

    def __init__(self, table_name, columns, connection):
        self.table_name = table_name
        self.columns = columns
        self.connection = connection
        self.cursor = self.connection.cursor()

        self.strfy_columns = ', '.join(self.columns)
        self.query = []
        self.query_statements = []

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

    def check_statement(self, statement):
        """
        Return if the statement is already in query or not.
        :param statement: Statement Name
        :return: boolean
        """
        return True if statement in self.query_statements else False

    def execute_query(self):
        self.cursor.execute(' '.join(self.query))

    def __getitem__(self, itens):
        columns = [col for col in itens if col in self.columns]
        return self.select(*columns)

    def count(self):
        """
        Count all elements of the actual table
        :return:
        Int with count
        """
        pass

    def insert(self, *values):
        pass

    def select(self, *cols):
        """
        SELECT clause that build the main and first statement of the query.
        :param cols: need to be the columns added to the function
        :return: None
        """
        statement = 'SELECT'

        if self.check_statement(statement):
            raise Exception('SELECT Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)
        self.query.append(statement)

        if not cols:
            self.query.append('*')
        else:
            [self.query.append(col) for col in cols if col in self.columns]
        self.query.append('FROM')
        self.query.append(self.table_name)
        return self

    def __str__(self, limit=20):
        if not self.check_statement('SELECT'):
            self.select()
        query = ' '.join(self.query + ['LIMIT ' + str(limit)])
        self.cursor.execute(query)
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