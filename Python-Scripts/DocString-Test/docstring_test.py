# def add( a, b ):
#     '''
#     >>> add(2, 3)
#     5
#     >>> add(100, 300)
#     400
#     '''
#     return a + b

#To run a doc string test you run the following command:
# python3 -m doctest -v [filename]


def double(values):
    """ double the values in a list
    
    >>> double([1,2,3,4])
    [2, 4, 6, 8]
    
    >>> double([])
    []
   
    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    
    >>> double ([True, None])
    Traceback (most recent call last):
            ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]