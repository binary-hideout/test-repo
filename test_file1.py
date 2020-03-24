
# ! dummy file

# ! test

def addition(x, y):
    '''Docstring.'''
    return x + y

def test_sum():
    assert addition(1, 2) == 3

def test_fail():
    assert addition(9, 9) == 9
