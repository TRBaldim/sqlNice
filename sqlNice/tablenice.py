from columnnice import ColumnNice
import sqlite3


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
        """
        :param list_of_rows:
        :param list_of_widths:
        :param fill:
        :param separtor_char:
        :return:
        """
        output_table = []

        for row in list_of_rows:
            list_justfied = []

            for elem, width in zip(row, list_of_widths):
                list_justfied.append(str(elem).rjust(width, fill))

            output_table.append(separtor_char +
                                separtor_char.join(list_justfied) +
                                separtor_char)

        return output_table

    @staticmethod
    def build_insert_values(values):
        out_list = []
        for elem in values:
            if isinstance(elem, str):
                out_list.append('\"' + str(elem) + '\"')
            else:
                out_list.append(str(elem))
        return "(" + ', '.join(out_list) + ")"

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
        return ColumnNice(col, self)

    def insert(self, *values):
        """
        INSERT should have the value for all columns, if a column has NULL should be added.
        The order of the values should be taken from self.columns to see if the values are right.
        :param values:
        :return:
        """
        if len(values) != len(self.columns):
            raise IndexError('Columns not match')

        statement = 'INSERT'

        if self.check_statement('SELECT') or \
                self.check_statement('UPDATE'):
            raise Exception('SELECT Statement with INSERT is not allowed')

        if self.check_statement(statement):
            self.query.append(", " + self.build_insert_values(values))
        else:
            self.query.append('INSERT INTO ')
            self.query.append(self.table_name)
            self.query.append("(" + ', '.join(self.columns) + ")")
            self.query.append("VALUES")
            self.query.append(self.build_insert_values(values))
        return self

    def update(self, **kwargs):
        """
        Update should be associate with each kind of values as kwargs
        update(id=1234, name='jeremias')
        :param kwargs:
        :return:
        """
        statement = 'UPDATE'

        if self.check_statement('SELECT'):
            raise Exception('SELECT Statement with UPDATE is not allowed')
        elif self.check_statement('INSERT'):
            raise Exception('INSERT Statement with UPDATE is not allowed')
        elif self.check_statement(statement):
            raise Exception('UPDATE Statement already in use')

        self.query_statements.append(statement)
        self.query.append('UPDATE')
        self.query.append(self.table_name)
        self.query.append('SET')

        col_usage_list = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                col_usage_list.append(str(i.upper()) + ' = \"' + kwargs[i] + '\"')
            else:
                col_usage_list.append(str(i.upper()) + ' =  ' + str(kwargs[i]))

        self.query.append(', '.join(col_usage_list))
        return self

    def delete(self):
        """

        :return:
        """
        statement = 'UPDATE'

        if self.check_statement('SELECT'):
            raise Exception('SELECT Statement with UPDATE is not allowed')
        elif self.check_statement('INSERT'):
            raise Exception('INSERT Statement with UPDATE is not allowed')
        elif self.check_statement(statement):
            raise Exception('UPDATE Statement already in use')

        self.query_statements.append(statement)
        self.query.append('DELETE')
        self.query.append('FROM')
        self.query.append(self.table_name)
        return self

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
            self.columns_selected = self.columns
        else:
            # TODO: Build something that check the query in a better form
            # https://trello.com/c/ry77XUGb/70-rebuild-the-handle-of-query-build
            # self.columns_selected = [col for col in cols if col in self.columns]
            self.columns_selected = cols
            self.query.append(', '.join(self.columns_selected))
        self.query.append('FROM')
        self.query.append(self.table_name)
        return self

    def group_by(self, *cols):
        statement = 'GROUP BY'

        if self.check_statement(statement):
            raise Exception('GROUP BY Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)
        self.query.append(statement)

        if not cols:
            raise Exception('Unable to group by, need to have columns to Aggregate')
        else:
            self.query.append(', '.join(cols))
        return self

    def where(self, where_statement_operation):
        """
        :param where_statement_operation:
        :return:
        """
        statement = 'WHERE'

        if self.check_statement(statement):
            raise Exception('WHERE Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)

        # Checking if has SELECT before Where
        if self.check_statement('SELECT'):
            self.query.append(statement)
        elif self.check_statement('UPDATE'):
            self.query.append(statement)
        else:
            raise Exception('WHERE without SELECT')

        self.query.append(where_statement_operation.operation)

        return self

    def build_query_str(self):
        """
        :return:
        """
        return ' '.join(self.query)

    def execute(self):
        """
        :return:
        """
        self.cursor.execute(self.build_query_str())
        self.query = []
        self.query_statements = []
        self.columns_selected = []

    def limit(self, limit=20):
        """
        :param limit:
        :return:
        """
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

    def distinct(self):
        """
        :return:
        """
        statement = 'DISTINCT'

        if self.check_statement(statement):
            raise Exception('DISTINCT Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)

        # Checking if has SELECT before Where
        if self.check_statement('SELECT'):
            self.query.insert(1, 'DISTINCT')
        else:
            raise Exception('DISTINCT without SELECT')
        return self

    def order_by(self, *columns):
        statement = 'ORDER BY'

        if self.check_statement(statement):
            raise Exception('ORDER BY Statement already in use. \n'
                            'Use a clear query method to run the statement')

        self.query_statements.append(statement)

        # Checking if has SELECT before Where
        if self.check_statement('SELECT'):
            self.query.append('ORDER BY')
            self.query.append(', '.join([str(col) for col in columns]))
        else:
            raise Exception('ORDER BY without SELECT')
        return self

    def __str__(self):
        if not self.check_statement('SELECT'):
            query = 'SELECT * FROM ' + self.table_name + ' LIMIT  20'
            self.columns_selected = self.columns
        else:
            query = ' '.join(self.query)
        try:
            self.cursor.execute(query)
        except sqlite3.OperationalError:
            raise Exception('Error in query execution please see the query: ' + query)

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
