from sys import getsizeof
from typing import Union
from hashlib import sha256
import json
from enum import IntEnum

ElementType = Union[dict, str]

class Response(IntEnum):
    NO = 0
    MAYBE = 1


class BloomFilter:
    def __init__(self, init_size: int = 1000, func_count: int = 3) -> None:
        if init_size < 8:
            raise ValueError("Can't craete bloom filter with less then a byte (8 bits) of data, Enter init_size bigger then 8.")
        if func_count <= 0:
            raise ValueError("func_count must be bigger then 0")
    
        self.size = init_size  # number of bits
        self.func_count = func_count
        
        if func_count > self.actual_size:
            raise ValueError("func count cant be bigger then filter size")

        self.function_salts = [sha256(str(i).encode()).hexdigest()[:8] for i in range(self.func_count)]
        self._on_count = 0
        self._filter = bytearray(self.size // 8)

    @property
    def actual_size(self) -> int:
        return self.size - (self.size % 8)

    @property
    def false_positive_probability(self):
        return (self._on_count / self.size)**self.func_count

    def _check_bit(self, index: int) -> bool:
        byte = self._filter[index // 8]
        bit_filter = 2 ** (7 - (index % 8))
        return bool(byte & bit_filter)
    
    def _turn_on_bit(self, index: int):
        byte_index = index // 8
        byte = self._filter[byte_index]
        bit_filter = 2 ** (7 - (index % 8))
        self._filter[byte_index] = byte | bit_filter

    def _element_indexs(self, element: ElementType):
        if isinstance(element, dict):
            element = json.dumps(element, sort_keys=True)

        for i in range(self.func_count):
            elem_bytes = (element + self.function_salts[i]).encode()
            hash_value = int.from_bytes(sha256(elem_bytes).digest(), 'little')
            index = hash_value % self.actual_size
            yield index

    def add_element(self, element: ElementType):
        for index in self._element_indexs(element):
            if self._check_bit(index) is True:
                continue
            self._on_count += 1
            self._turn_on_bit(index)

    def query(self, element: ElementType) -> Response:
        """
        Check if the element is added to the filter

        :returns: Maybe if all the bits are on else NO
        """
        for index in self._element_indexs(element):
            if self._check_bit(index) is False:
                return Response.NO

        return Response.MAYBE

    def __str__(self) -> str:
        return f"BloomFilter(size={self.actual_size}, func_count={self.func_count}, false_positive_pob={self.false_positive_probability})"

    def __sizeof__(self) -> int:
        return getsizeof(self._filter)