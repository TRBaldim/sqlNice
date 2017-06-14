import unittest

from sqlNice import sqlnice
from sqlNice.tablenice import TableNice
from tests.test_lib.generate_tables import *
from sqlNice.functions import *


class TestFunctions(unittest.TestCase):

    def test_sum(self):
        db_name = 'first_db.db'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)

        test_obj = sqlnice.SqlNice(db_name)
        table_obj = test_obj['TABLE_1']
        query = table_obj.select(sum(table_obj['AMOUNT'])).query

        query_result = ['SELECT', 'SUM(AMOUNT)', 'FROM', 'TABLE_1']

        self.assertEqual(query, query_result)
