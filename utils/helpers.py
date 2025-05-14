from traceback import print_exception


def custom_exception_traceback(exception: Exception) -> None:
    """Creates a custom traceback for exceptions.

    Args:
        exception (Exception): Exception to be printed.

    Returns:
        None: _description_
    """    
    return print_exception(exc=type(exception), value=exception, TracebackType=exception.__traceback__)