#app.py

def addition(a,b):
    return a + b

def test_addition():
    assert addition(1,2) == 3
    assert addition(5,5) == 10

test_addition()
