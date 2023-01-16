
# easy_bloom_filter module

This module contains the BloomFilter class, which is used for efficient probabilistic data structure for set membership queries. It allows for the testing of whether an element is a member of a set or not, with a small probability of false positives.

## Usage

To use the BloomFilter class, simply import it from the easy_bloom_filter module.

```
from easy_bloom_filter import BloomFilter
```

The constructor for BloomFilter takes two arguments: `init_size` and `func_count`. `init_size` defines the size of the filter and `func_count` defines the number of hash functions used to generate the filter.

The `add_element` method allows you to add elements to the filter.

The `query` method allows you to query the filter for elements. It will return either `Response.MAYBE` if the element is possibly in the filter or `Response.NO` if the element is definitely not in the filter.

The `false_positive_probability` attribute gives the probability of a false positive when querying the filter.

The `_on_count` attribute gives the number of elements currently in the filter.

The `actual_size` attribute gives the actual size of the filter, which is rounded down to the nearest power of two.

The `__str__` method returns a string representation of the filter.

## Testing

The module also contains several tests for the BloomFilter class. These tests check the validity of the arguments, the number of elements added to the filter, the accuracy of querying elements, the false positive probability and the size of the filter.