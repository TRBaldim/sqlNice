import sqlite3
import numpy as np
from .test_lib import basic_lib_tests


def create_tabletest_table(db_name, table_name):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    try:
        c.execute('CREATE TABLE ' + table_name + ' (DATE TEXT, ID INTEGER, NAME TEXT, AMOUNT REAL)')
    except sqlite3.OperationalError:
        return None
    except Exception as error:
        print('Unexpected error during table creation', error)
        raise

    conn.commit()

    try:
        for i in range(100):
            query = 'INSERT INTO ' + table_name + ' VALUES (\'' + \
                    basic_lib_tests.random_date("1-1-2016", "1-1-2017", np.random.random()) + \
                    '\', ' + str(i) + ', \'' + \
                    basic_lib_tests.random_word(10) + '\', ' + \
                    str(float(np.random.randint(1, 25000))) + ')'
            c.execute(query)
    except Exception as error:
        raise Exception('Unable to insert data to database', error)

    conn.commit()
    conn.close()

    return True
