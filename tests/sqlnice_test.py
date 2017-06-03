import unittest
from .generate_tables import create_tabletest_table
from sqlNice import sqlnice
from sqlNice.tablenice import TableNice


def build_databases(db_name, table_list):
    # creating the test table, to tests
    create_tabletest_table(db_name, table_list[0])
    create_tabletest_table(db_name, table_list[1])


class TestCore(unittest.TestCase):

    def test_get_table_list(self):
        db_name = 'first_db.db'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)

        test_obj = sqlnice.SqlNice(db_name)

        self.assertEqual(test_obj.get_tables_names(), table_list)

    def test_get_columns_list_from_table_name(self):
        db_name = 'first_db.db'
        columns_names = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)

        test_obj = sqlnice.SqlNice(db_name)

        self.assertEqual(test_obj.get_columns_names(table_name), columns_names)

    def test_get_columns_by_table(self):
        db_name = 'first_db.db'
        columns_names_1 = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name_1 = 'TABLE_1'

        columns_names_2 = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name_2 = 'TABLE_2'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)

        test_obj = sqlnice.SqlNice(db_name)

        self.assertEqual(test_obj.get_tables_schemas(), {table_name_1: columns_names_1,
                                                         table_name_2: columns_names_2})

    def test_table_object_creation(self):
        db_name = 'first_db.db'
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)

        test_obj = sqlnice.SqlNice(db_name)

        self.assertIsInstance(test_obj[table_name_1], TableNice)

    def test_get_cols(self):
        db_name = 'first_db.db'
        columns_names_1 = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)
        table_obj = sqlnice.SqlNice(db_name)[table_name_1]

        self.assertEqual(table_obj.columns, columns_names_1)

    def test_selected_cols(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'DATE, ID', 'FROM', 'TABLE_1']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('DATE', 'ID')
        self.assertEqual(table_obj.query, query_result)

    def test_execute_method(self):
        """
        Validate if query is going to empty after it runs execute() method
        :return:
        """
        db_name = 'first_db.db'
        query_result = []
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('DATE', 'ID')
        table_obj.execute()
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_lt(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT > 1000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'] > 1000)
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_le(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT >= 1000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'] >= 1000)
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_eq(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT == 1000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'] == 1000)
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_ne(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT != 1000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'] != 1000)
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_gt(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT < 1000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'] < 1000)
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_ge(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT <= 1000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'] <= 1000)
        self.assertEqual(table_obj.query, query_result)

if __name__ == '__main__':
    unittest.main()
