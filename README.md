# bloom filter
python implementation of bloom filter


## installation
```shell
$ pip install py-bloom-filter
```

## usage
Simple example

```python
from py_bloom_filter import BloomFilter, Response

bf = BloomFilter(init_size=2001, func_count=3)

bf.add_element("first")
bf.add_element("second")
bf.add_element({"num": "3"})

print(bf.query("4")     == Response.NO)     # True
print(bf.query("first") == Response.MAYBE)  # True

print(bf.false_positive_probability)  # 9.09884490736791e-08
print(bf.actual_size)                 # 2000  (round to multiple of 8 for storing the data on bits)
```

## test
### install dev requirements
```shell
$ pip install -r requirements-dev.txt
```

### run tests
#### only tests
```shell
$ pytest .
```

#### tests with coverage
```shell
$ pytest --cov-report=html --cov=py_bloom_filter tests/
```