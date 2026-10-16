from collections import OrderedDict
from cache_engine.base import EvictionStrategy

class MRUStrategy(EvictionStrategy):
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
            raise KeyError("Cannot evict from an empty MRU tracker.")
        key, _ = self.usage.popitem(last=True)
        return key

    def on_remove(self, key: str) -> None:
        self.usage.pop(key, None)