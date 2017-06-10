import unittest

from sqlNice import sqlnice
from sqlNice.tablenice import TableNice
from tests.test_lib.generate_tables import *


class TestSqlNice(unittest.TestCase):

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

    def test_insert(self):
        db_name = 'first_db.db'
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)
        db_object = sqlnice.SqlNice(db_name)
        table_obj = db_object[table_name_1]
        user_id = np.random.randint(100000, 999999)
        table_obj.insert('2017-10-10',
                         user_id,
                         'JOSIAS',
                         float(np.random.randint(1, 10000))).execute()
        db_object.commit()
        table_obj.select().where(table_obj['ID'] == user_id).execute()
        values = table_obj.cursor.fetchall()
        self.assertEqual(user_id, values[0][1])

    def test_multiple_inserts(self):
        db_name = 'first_db.db'
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)
        db_object = sqlnice.SqlNice(db_name)
        table_obj = db_object[table_name_1]
        user_id_list = []
        for i in range(10):
            user_id = np.random.randint(100000, 999999)
            user_id_list.append(user_id)
            table_obj.insert('2017-10-10',
                             user_id,
                             'JOSIAS',
                             float(np.random.randint(1, 10000))).execute()
        db_object.commit()
        table_obj.select().where(table_obj['ID'].is_in(user_id_list)).execute()
        values = table_obj.cursor.fetchall()
        ids = [elem[1] for elem in values]
        self.assertIn(np.random.choice(user_id_list), ids)

    def test_update(self):
        db_name = 'first_db.db'
        table_name_1 = 'TABLE_1'
        table_list = ['TABLE_1', 'TABLE_2']
        build_databases(db_name, table_list)
        db_object = sqlnice.SqlNice(db_name)
        table_obj = db_object[table_name_1]

        table_obj.update(name='AAAAA').where(table_obj['AMOUNT'] > 1000.0).execute()
        db_object.commit()
        table_obj.select().where(table_obj['NAME'] == 'AAAAA').execute()
        values = table_obj.cursor.fetchall()
        name = values[0][2]
        self.assertEqual(name, 'AAAAA')

if __name__ == '__main__':
    unittest.main()
