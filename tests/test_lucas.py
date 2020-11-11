from math_series.series_module import lucas

def test_import():
    assert lucas

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 3
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 5
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 8
    assert actual == expected

def test_lucas_4():
    actual = lucas(4)
    expected = 13
    assert actual == expected

def test_lucas_5():
    actual = lucas(5)
    expected = 21
    assert actual == expected

def test_lucas_6():
    actual = lucas(6)
    expected = 34
    assert actual == expected
def test_lucas_7():
    actual = lucas(7)
    expected = 55
    assert actual == expected

def test_lucas_8():
    actual = lucas(8)
    expected = 89
    assert actual == expected

def test_lucas_9():
    actual = lucas(9)
    expected = 144
    assert actual == expected

def test_lucas_10():
    actual = lucas(10)
    expected = 233
    assert actual == expected
