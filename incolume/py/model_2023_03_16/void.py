"""Void Module."""
import inspect
import logging


def void(*args: tuple, **kwargs: dict) -> dict:
    """void funtion.
    args:
        args: Arguments
        kwargs: Key Word Arguments

    returns:
        dictionary with all params.

    raises:
        No One

    examples:
        >>> void()
        {}

        >>> void(1, 2, 3)
        {'args': (1, 2, 3)}

        >>> void(a=1, b=2)
        {'a': 1, 'b': 2}

        >>> void(1, 2, a=1, b=2)
        {'args': (1, 2), 'a': 1, 'b': 2}

    """
    result = {"args": args} if args else {}
    result.update(kwargs)
    logging.debug(result)
    logging.info(f"ran {inspect.stack()[0][3]}")
    return result
