'''
Created on Aug 7, 2014

@author: c3h3
'''

from PyTC.helloPyTC import helloPyTC

def test_hello():
    assert helloPyTC == "helloPyTC"

def test_hello2():
    assert helloPyTC != "helloPyTC1234"