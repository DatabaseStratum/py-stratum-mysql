from pystratum_common.BuildContext import BuildContext

from pystratum_mysql.wrapper.MySqlBulkWrapper import MySqlBulkWrapper
from pystratum_mysql.wrapper.MySqlFunctionsWrapper import MySqlFunctionsWrapper
from pystratum_mysql.wrapper.MySqlLogWrapper import MySqlLogWrapper
from pystratum_mysql.wrapper.MySqlMultiWrapper import MySqlMultiWrapper
from pystratum_mysql.wrapper.MySqlNoneWrapper import MySqlNoneWrapper
from pystratum_mysql.wrapper.MySqlRow0Wrapper import MySqlRow0Wrapper
from pystratum_mysql.wrapper.MySqlRow1Wrapper import MySqlRow1Wrapper
from pystratum_mysql.wrapper.MySqlRowsWithIndexWrapper import MySqlRowsWithIndexWrapper
from pystratum_mysql.wrapper.MySqlRowsWithKeyWrapper import MySqlRowsWithKeyWrapper
from pystratum_mysql.wrapper.MySqlRowsWrapper import MySqlRowsWrapper
from pystratum_mysql.wrapper.MySqlSingleton0Wrapper import MySqlSingleton0Wrapper
from pystratum_mysql.wrapper.MySqlSingleton1Wrapper import MySqlSingleton1Wrapper
from pystratum_mysql.wrapper.MySqlWrapper import MySqlWrapper


# ----------------------------------------------------------------------------------------------------------------------

def create_routine_wrapper(context: BuildContext) -> MySqlWrapper:
    """
    A factory for creating the appropriate object for generating a wrapper method for a stored routine.

    :param context: The build context.

    :rtype: MySqlWrapper
    """
    if context.routine['designation'] == 'bulk':
        wrapper = MySqlBulkWrapper()
    elif context.routine['designation'] == 'function':
        wrapper = MySqlFunctionsWrapper()
    elif context.routine['designation'] == 'log':
        wrapper = MySqlLogWrapper()
    elif context.routine['designation'] == 'multi':
        wrapper = MySqlMultiWrapper()
    elif context.routine['designation'] == 'none':
        wrapper = MySqlNoneWrapper()
    elif context.routine['designation'] == 'row0':
        wrapper = MySqlRow0Wrapper()
    elif context.routine['designation'] == 'row1':
        wrapper = MySqlRow1Wrapper()
    elif context.routine['designation'] == 'rows_with_index':
        wrapper = MySqlRowsWithIndexWrapper()
    elif context.routine['designation'] == 'rows_with_key':
        wrapper = MySqlRowsWithKeyWrapper()
    elif context.routine['designation'] == 'rows':
        wrapper = MySqlRowsWrapper()
    elif context.routine['designation'] == 'singleton0':
        wrapper = MySqlSingleton0Wrapper()
    elif context.routine['designation'] == 'singleton1':
        wrapper = MySqlSingleton1Wrapper()
    else:
        raise Exception("Unknown routine type '{0!s}'.".format(context.routine['designation']))

    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
