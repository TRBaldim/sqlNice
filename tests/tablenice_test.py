import unittest
from tests.test_lib.generate_tables import *
from sqlNice import sqlnice


class TestTableNice(unittest.TestCase):

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

    def test_where_clause_and(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT >= 1000 AND AMOUNT <= 5000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where((table_obj['AMOUNT'] >= 1000) &
                                                           (table_obj['AMOUNT'] <= 5000))
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_or(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT >= 1000 OR AMOUNT <= 5000']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where((table_obj['AMOUNT'] >= 1000) |
                                                           (table_obj['AMOUNT'] <= 5000))
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_in(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT IN (14.0, 20252.0)']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'].is_in([14.0, 20252.0]))
        self.assertEqual(table_obj.query, query_result)

    def test_where_clause_like(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'WHERE', 'AMOUNT LIKE \"%JOSIAS%\"']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)

        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').where(table_obj['AMOUNT'].like('JOSIAS'))
        self.assertEqual(table_obj.query, query_result)

    def test_limit(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'LIMIT', '10']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)
        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').limit(10)
        self.assertEqual(table_obj.query, query_result)

    def test_distinct(self):
        db_name = 'first_db.db'
        query_result = ['SELECT', 'DISTINCT', 'ID, AMOUNT', 'FROM', 'TABLE_1', 'LIMIT', '10']
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']

        build_databases(db_name, table_list)
        table_obj = sqlnice.SqlNice(db_name)[table_name_1]
        table_obj = table_obj.select('ID', 'AMOUNT').limit(10).distinct()
        self.assertEqual(table_obj.query, query_result)
