

def sum(column):
    """
    Sum one column of a function
    :param column:
    :return:
    """
    return 'SUM(' + str(column) + ')'


def max(column):
    """
    Max of one column
    :param column:
    :return:
    """
    return 'MAX(' + str(column) + ')'


def min(column):
    """
    Min of one column
    :param column:
    :return:
    """
    return 'MIN(' + str(column) + ')'


def count(column):
    """
    Min of one column
    :param column:
    :return:
    """
    return 'COUNT(' + str(column) + ')'