import pytest
from stack import *

def test_pop():
    s = Stack(5)
    s.push(5)
    s.push(-10)
    assert s.pop() == -10
    assert s.pop() == 5
    assert s.pop() == 'Stack is empty. Nothing to pop.'