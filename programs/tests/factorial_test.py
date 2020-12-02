
from programs import factorial

def test_factorial():
    assert factorial.fact(4) == 4*3*2*1

def test_factorial_zero():
    assert factorial.fact(0) == 1