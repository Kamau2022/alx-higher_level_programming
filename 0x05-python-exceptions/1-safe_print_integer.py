#!/usr/bin/python3

def safe_print_integer(value):

    """a function that prints an integer
    Args:
        value: value to be printed
    Return: True or False
    """
    
    try:
            print("{:d}" .format(value))
            return True
    except TypeError:
            return False
    except ValueError:
            return False
        
            
            
