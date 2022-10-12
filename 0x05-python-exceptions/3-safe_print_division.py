#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result.
    Args:
       a: first integer
       b: second integer
    Returns: result or None
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
    except TypeError:
        result = None 
    finally:
        print("inside result: {}".format(result))
