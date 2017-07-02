from logpy import Relation, facts, run, var


class Query(object):
    def __init__(self):
        self.statements = Relation()
        self.build_statements_relations()
        self.execution_statements = {}
        self.possible_choices = ()

    def build_statements_relations(self):
        '''
        Build the relation of each element of the query
        :return:
        '''
        self.statements = Relation()
        facts(self.statements, ('WHERE', 'SELECT'),
                               ('WHERE', 'UPDATE'),
                               ('WHERE', 'DELETE'),
                               ('GROUP_BY', 'SELECT'),
                               ('HAVING', 'GROUP_BY'),
                               ('LIMIT', 'SELECT'),
                               ('DISTINCT', 'SELECT'),
                               ('ASC', 'ORDER_BY'),
                               ('DESC', 'ORDER_BY'),
                               ('ORDER_BY', 'SELECT'),
                               ('AND', 'WHERE'),
                               ('OR', 'WHERE'))

    def check_logical_relation(self, statement):
        """
        Check the procedure of each statement if is possible com combine them or not
        :param statement: string with possible statements
        :return: boolean
        """
        x = var()

        if self.possible_choices == ():
            self.possible_choices = run(0, x, self.statements(x, statement))
            return True if self.possible_choices != () else False
        else:
            if statement in self.possible_choices:
                possible_list = run(0, x, self.statements(statement, x))
                return True if possible_list != () else False
            else:
                possible_statement_list = run(0, x, self.statements(statement, x))
                for p_statement in possible_statement_list:
                    if p_statement in self.execution_statements.keys():
                        return True
                return False

    def append(self, **kwargs):
        """
        Append the elements of query execution
        :param kwargs:
        :return:
        """

        for key in kwargs:
            if self.check_logical_relation(key):
                self.execution_statements[key] = kwargs[key]
            else:
                raise Exception('The statement ' + key + ' can\'t be part of this query')

