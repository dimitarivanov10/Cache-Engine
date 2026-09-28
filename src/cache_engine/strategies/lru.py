from collections import OrderedDict
from cache_engine.base import EvictionStrategy

class LRUStrategy(EvictionStrategy):
    """Evicts the key that has not been accessed or updated for the longest duration."""

def __init__(self):
    self.usage: OrderedDict[str, None] = OrderedDict()

def on_get(self, key: str) -> None:
    if key in self.usage:
        self.usage.move_to_end(key)

def on_put(self, key: str) -> None:
    self.usage[key] = None
    self.usage.move_to_end(key)

def evict_key(self) -> str:
    if not self.usage:
        raise KeyError("Cannot evict from an empty LRU tracker.")
    key, _ = self.usage.popitem(last=False)
    return key

def on_remove(self, key: str) -> None:
    self.usge.pop(key, None)