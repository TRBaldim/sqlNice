from sqlNice import ColumnNice


def handle_table_info(column):
    if isinstance(column, ColumnNice):
        column.table.query_statements.append('FUNCTION')
        ret = True
    else:
        ret = False
    return ret


def sum(column):
    """
    Sum one column of a function
    :param column:
    :return:
    """
    if not handle_table_info(column):
        raise Exception("Not a ColumnNice object")

    return 'SUM(' + str(column) + ')'


def max(column):
    """
    Max of one column
    :param column:
    :return:
    """
    if not handle_table_info(column):
        raise Exception("Not a ColumnNice object")

    return 'MAX(' + str(column) + ')'


def min(column):
    """
    Min of one column
    :param column:
    :return:
    """
    if not handle_table_info(column):
        raise Exception("Not a ColumnNice object")

    return 'MIN(' + str(column) + ')'


def count(column):
    """
    Min of one column
    :param column:
    :return:
    """
    if not handle_table_info(column):
        raise Exception("Not a ColumnNice object")

    return 'COUNT(' + str(column) + ')'
