from src.math_op import add, sub, mul

def test_add():
    assert add(2,3)==5
    assert add(7,3)==10
def test_sun():
    assert sub(6,2)==4
    assert sub(3,5)==-2
    assert sub(2,5)==-3
def test_mul():
    assert mul(5,5)==25