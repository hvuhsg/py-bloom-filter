

# BloomFilter

BloomFilter is a probabilistic data structure used to determine if an element is a member of a set. It is used to reduce the number of false positives when searching for an element in a set.

## Constructor

The BloomFilter constructor takes two optional arguments: `init_size` and `func_count`. `init_size` is the number of bits used to store the BloomFilter and must be greater than 8. `func_count` is the number of hash functions used to calculate the index of a given element and must be greater than 0.

## Properties

The BloomFilter has two properties: `actual_size` and `false_positive_probability`. `actual_size` is the actual number of bits used to store the BloomFilter and is equal to `init_size` minus any remainder. `false_positive_probability` is the probability that an element is incorrectly identified as a member of the set.

## Methods

The BloomFilter has two methods: `add_element` and `query`. `add_element` takes an element of type `ElementType` and adds it to the BloomFilter. `query` takes an element of type `ElementType` and returns a `Response` enum value of either `NO` or `MAYBE`.

## String Representation

The BloomFilter has a string representation which includes the `actual_size`, `func_count`, and `false_positive_probability`.

## Size

The size of the BloomFilter can be determined using the `__sizeof__` method.