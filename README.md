# bloom filter
[![tests](https://github.com/hvuhsg/py-bloom-filter/actions/workflows/tests.yml/badge.svg)](https://github.com/hvuhsg/py-bloom-filter/actions/workflows/tests.yml)
[![PyPI version](https://badge.fury.io/py/easy-bloom-filter.svg)](https://badge.fury.io/py/easy-bloom-filter)  

python implementation of bloom filter  
  
What is bloom filter? https://en.wikipedia.org/wiki/Bloom_filter

## installation
```shell
$ pip install easy-bloom-filter
```

## usage
Simple example

```python
from easy_bloom_filter import BloomFilter, Response

bf = BloomFilter(init_size=2001, func_count=3)

bf.add_element("first")
bf.add_element("second")
bf.add_element({"num": "3"})

print(bf.query("4")     == Response.NO)     # True (not added to filter)
print(bf.query("first") == Response.MAYBE)  # True (maybe added to filter check with the source of truth)

print(bf.false_positive_probability)  # 9.09884490736791e-08
print(bf.actual_size)                 # 2000  (round to multiple of 8 for storing the data on bits)
```

### install dev requirements
```shell
$ pip install -r requirements-dev.txt
```

#### only tests
```shell
$ pytest .
```

#### tests with coverage
```shell
$ pytest --cov-report=html --cov=py_bloom_filter tests/
```