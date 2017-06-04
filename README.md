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

print my_table.select(['NAME', 'SALARY']).where(my_table['SALARY'] >= 1000.0)

```

The sqlNice will give you a nice view of responses, good for notebooks like Jupyter:

```
```
