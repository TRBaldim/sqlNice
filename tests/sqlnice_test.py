import unittest
from .generate_tables import create_tabletest_table
from sqlNice import sqlnice
from sqlNice.tablenice import TableNice


class TestCore(unittest.TestCase):

    def test_get_table_list(self):
        db_name = 'first_db.db'
        table_list = ['TABLE_1', 'TABLE_2']

        # creating the test table, to tests
        create_tabletest_table(db_name, table_list[0])
        create_tabletest_table(db_name, table_list[1])

        test_obj = sqlnice.SqlNice(db_name)

        self.assertEqual(test_obj.get_tables_names(), table_list)

    def test_get_columns_list_from_table_name(self):
        db_name = 'first_db.db'
        columns_names = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name = 'TABLE_1'

        test_obj = sqlnice.SqlNice(db_name)

        self.assertEqual(test_obj.get_columns_names(table_name), columns_names)

    def test_get_columns_by_table(self):
        db_name = 'first_db.db'
        columns_names_1 = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name_1 = 'TABLE_1'

        columns_names_2 = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name_2 = 'TABLE_2'

        test_obj = sqlnice.SqlNice(db_name)

        self.assertEqual(test_obj.get_tables_schemas(), {table_name_1: columns_names_1,
                                                         table_name_2: columns_names_2})

    def test_table_object_creation(self):
        db_name = 'first_db.db'
        table_name_1 = 'TABLE_1'

        test_obj = sqlnice.SqlNice(db_name)

        self.assertIsInstance(test_obj[table_name_1], TableNice)

    def test_get_cols(self):
        db_name = 'first_db.db'
        columns_names_1 = ['DATE', 'ID', 'NAME', 'AMOUNT']
        table_name_1 = 'TABLE_1'

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]

        self.assertEqual(table_obj.columns, columns_names_1)

    def test_selected_cols(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'DATE, ID', 'FROM', 'TABLE_1']
        table_name_1 = 'TABLE_1'

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('DATE', 'ID')
        self.assertEqual(table_obj.query, query_result)

    def test_execute_method(self):
        db_name = 'first_db.db'
        query_result = []
        table_name_1 = 'TABLE_1'

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('DATE', 'ID')
        table_obj.execute()
        self.assertEqual(table_obj.query, query_result)
