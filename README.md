# sqlNice

[![Build Status](https://api.travis-ci.org/TRBaldim/sqlNice.svg?branch=master)](https://travis-ci.org/TRBaldim/sqlNice)

sqlNice is a good option to create a cleaner and nicer way to do queries at sqlite3.
This will give you a nice view and a nice process of building your code with no ugly queries.

## Getting Started

How to use sqlNice?
This is easy and nice!

```
from sqlNice import SqlNice

# Get Access to your DB
my_db = SqlNice('my_db.db')

# Get your table
my_table = my_db['MY_TABLE']

# Run your query

print my_table.select(['NAME', 'SALARY']).where(my_table['SALARY'] >= 10000.0)

```

The sqlNice will give you a nice view of responses, good for notebooks like Jupyter:

```
+----------+-------+
|      NAME| SALARY|
+----------+-------+
| John Nice|14952.0|
|Alice Cool|23709.0|
| Myth Rare|16540.0|
|  Luke Sky|17249.0|
|    Master|17781.0|
|  Hadouken|20252.0|
+----------+-------+
```
Let's INSERT Something :D

```
my_table.insert('Josias Yeah', '1200.0').execute()
my_db.commit()

```

Why not update?

```
my_table.update(name='Mano Brown').where(my_table['NAME'] == 'Josias Yeah').execute()
my_db.commit()
```