"""
This module contains basic unit tests for math operations. 
Their purpose is to show hot to use the ptest framework by example.
"""

#----------------------------------------------------------------------------
# A most basic test function
#----------------------------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1  == 2


#----------------------------------------------------------------------------
# A test function to show assertion introspection
#----------------------------------------------------------------------------

def test_one_plus_two():
    a = 1
    b = 2
    c = 3 

    assert a + b == c