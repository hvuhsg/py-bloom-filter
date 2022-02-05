from sys import getsizeof
import pytest

from easy_bloom_filter import BloomFilter, Response


def test_rounding_size():
    b_filter = BloomFilter(init_size=2001, func_count=3)
    assert b_filter.actual_size == 2000


def test_invalid_args():
    with pytest.raises(ValueError):
        BloomFilter(init_size=0, func_count=3)
    
    with pytest.raises(ValueError):
        BloomFilter(init_size=200, func_count=0)
    
    with pytest.raises(ValueError):
        BloomFilter(init_size=10, func_count=20)
    

def test_adding_elements():
    b_filter = BloomFilter(init_size=5000, func_count=3)
    for i in range(800):
        b_filter.add_element({"arg": i})

    assert b_filter._on_count >= 800

def test_quering_elements():
    b_filter = BloomFilter(init_size=5000, func_count=3)
    for i in range(800):
        b_filter.add_element({"arg": i})
    
    assert b_filter.query({"arg": 180}) == Response.MAYBE
    assert b_filter.query("not inserted") == Response.NO

def test_false_positive_probebility():
    b_filter = BloomFilter(init_size=5000, func_count=3)
    for i in range(800):
        b_filter.add_element({"arg": i})
    
    maybe = 0
    trys = 10000
    for i in range(trys):
        if b_filter.query(str(i)) is Response.MAYBE:
            maybe += 1
    test_probability = maybe / trys

    assert abs(b_filter.false_positive_probability - test_probability) < 0.05, f"{test_probability} {b_filter.false_positive_probability}"


def test_filter_size():
    b_filter = BloomFilter(init_size=1000, func_count=3)
    assert getsizeof(b_filter) == 198

def test_str():
    b_filter = BloomFilter(init_size=1000, func_count=3)
    print(b_filter.actual_size, b_filter.false_positive_probability)
    assert str(b_filter) == "BloomFilter(size=1000, func_count=3, false_positive_pob=0.0)"
