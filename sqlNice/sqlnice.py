from __future__ import print_function

import sqlite3
from .tablenice import TableNice


class SqlNice(object, sqlite3):
    def __init__(self, sqlite_path_db):
        # Connection is automatic during the contructor
        self.conn = self.connect(sqlite_path_db)

        self.cursor = self.conn.cursor()
        self.table_list_names = self.get_tables_names()
        self.columns_by_tables = self.get_tables_schemas()
        self.table_list_obj = {}

    def close(self):
        self.rollback()
        self.conn.close()

    def commit(self):
        # TODO: Add a control to find if has anything to commit
        # https://trello.com/c/8wahdvLz/48-checking-queries-before-commit
        self.conn.commit()

    def rollback(self):
        # TODO: Add the same control of queries to rollback
        self.conn.rollback()

    def create_table(self, table_name, columns, types=None):
        pass

    def drop_table(self, table_name):
        pass

    def get_tables_names(self):
        """
        Take the tables inside the sqlite3 db
        :return:
        List of tables names
        """
        res = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [str(name[0]) for name in res]

    def get_columns_names(self, table_name):
        """
        Take the columns details and add to attributes of the class
        :return:
        List of Columns Names
        """
        self.cursor.execute("SELECT * FROM " + table_name)
        return [name[0] for name in self.cursor.description]

    def get_tables_schemas(self):
        """
        Build a dict with each data from columns by table
        :return:
        Dict with {Table_name: [Columns_names]}
        """
        return {table: self.get_columns_names(table) for table in self.table_list_names}

    def __getitem__(self, item):
        """
        Build the table object if it was requested.
        :param item: Table name
        :return: Dict element of the item
        """
        if item in self.table_list_obj:
            return self.table_list_obj[item]
        else:
            if item in self.table_list_names:
                t = TableNice(item, self.columns_by_tables[item], self.conn)
            else:
                raise Exception('The table ' + str(item) + ' doesn\'t belong to this database')
            self.table_list_obj[item] = t
            return self.table_list_obj[item]

    def __del__(self):
        self.close()