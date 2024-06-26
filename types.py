from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class SimpleString:
    data: str
    
    
@dataclass
class Error:
    data: str
    

@dataclass
class Integer:
    value: int
    
    
@dataclass
class BulkString:
    data: bytes
    

@dataclass
class Array:
    data: list
    
    def __get_item__(self,i):
        return self.data[i]
    
    def __len__(self):
        return len(self.data)
        