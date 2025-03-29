from src.math_operation import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(-1, 0) == -1
    
def test_subtract():
    assert sub(5, 3) == 2
    assert sub(-1, 1) == -2
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0
    assert sub(-1, 0) == -1
    
def test_multiply():
    assert mul(5, 3) == 15
    assert mul(-1, 1) == -1
    assert mul(0, 0) == 0
    assert mul(-1, -1) == 1
    assert mul(-1, 0) == 0
    
def test_divide():
    assert div(6, 3) == 2
    assert div(-1, 1) == -1
    assert div(0, 1) == 0
    assert div(-1, -1) == 1
    assert div(-1, 0) == "Error: Division by zero is not allowed"

