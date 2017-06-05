from columnnice import ColumnNice


class TableNice(object):

    def __init__(self, table_name, columns, connection):
        self.table_name = table_name
        self.columns = columns
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.columns_selected = []
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

    def __getitem__(self, col):
        return ColumnNice(col)

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
            self.columns_selected = [col for col in cols if col in self.columns]
            self.query.append(', '.join(self.columns_selected))
        self.query.append('FROM')
        self.query.append(self.table_name)
        return self

    def where(self, where_statement_operation):
        statement = 'WHERE'

        if self.check_statement(statement):
            raise Exception('WHERE Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)

        # Checking if has SELECT before Where
        if self.check_statement('SELECT'):
            self.query.append(statement)
        else:
            raise Exception('WHERE without SELECT')

        self.query.append(where_statement_operation.operation)

        return self

    def build_query_str(self):
        return ' '.join(self.query)

    def execute(self):
        self.cursor.execute(self.build_query_str())
        self.query = []
        self.query_statements = []
        self.columns_selected = []

    def limit(self, limit=20):
        statement = 'LIMIT'

        if self.check_statement(statement):
            raise Exception('LIMIT Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)

        # Checking if has SELECT before Where
        if self.check_statement('SELECT'):
            self.query.append('LIMIT')
            self.query.append(str(limit))
        else:
            raise Exception('LIMIT without SELECT')

        return self

    def __str__(self):
        if not self.check_statement('SELECT'):
            query = 'SELECT * FROM ' + self.table_name + ' LIMIT  20'
            self.columns_selected = self.columns
        else:
            query = ' '.join(self.query)

        self.cursor.execute(query)
        list_of_rows = self.cursor.fetchall()
        list_of_widths = []

        # Iterate to check largest char in each row
        if len(list_of_rows) != 0:
            for col_val, col_name in zip(list_of_rows[0], self.columns_selected):
                len_name = len(str(col_name))
                len_val = len(str(col_val))
                list_of_widths.append(len_name if len_name > len_val else len_val)
        else:
            for col_name in self.columns_selected:
                len_name = len(str(col_name))
                list_of_widths.append(len_name)
        # Justfy the elements
        separator = self.justfy_list([['' for _ in self.columns_selected]], list_of_widths, '-', '+')
        output_rows = self.justfy_list(list_of_rows, list_of_widths, ' ')
        output_header = self.justfy_list([self.columns_selected], list_of_widths, ' ')

        # Build the structure of elements
        output_rows.insert(0, separator[0])
        output_rows.insert(0, output_header[0])
        output_rows.insert(0, separator[0])
        output_rows.append(separator[0])

        return '\n'.join(output_rows)
