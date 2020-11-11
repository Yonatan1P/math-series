from math_series.series_module import sum_series

def test_import():
    assert sum_series

def test_sum_series_0_fib():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_00_fib():
    actual = sum_series(0,0)
    expected = 0
    assert actual == expected

def test_sum_series_001_fib():
    actual = sum_series(0,0,1)
    expected = 0
    assert actual == expected

def test_sum_series_0_luc():
    actual = sum_series(0,2)
    expected = 2
    assert actual == expected

def test_sum_series_021_luc():
    actual = sum_series(0,2,1)
    expected = 2
    assert actual == expected 

def test_sum_series_5_fib():
    actual = sum_series(5,0)
    expected = 5
    assert actual == expected

def test_sum_series_5_luc():
    actual = sum_series(5,2)
    expected = 21
    assert actual == expected