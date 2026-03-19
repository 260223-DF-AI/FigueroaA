import pytest

def adder(a, b):
    return a + b

def test_answer():
    assert adder(1, 3)  == 7

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

def exception_fun():
    raise FileNotFoundError("Not found")

def test_exception_fun():
    with pytest.raises(FileNotFoundError):
        exception_fun()
print("done")