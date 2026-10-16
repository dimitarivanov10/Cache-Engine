from collections import Counter
from cache_engine.base import EvictionStrategy

class LFUStrategy(EvictionStrategy):
    def __init__(self):
        self.frequencies: Counter[str] = Counter()

    def on_get(self, key: str) -> None:
        if key in self.frequencies:
            self.frequencies[key] += 1

    def on_put(self, key: str) -> None:
        if key in self.frequencies:
            self.frequencies[key] += 1
        else:
            self.frequencies[key] = 1

    def evict_key(self) -> str:
        if not self.frequencies:
            raise KeyError("Cannot evict from an empty LFU tracker.")
        least_frequent_key = min(self.frequencies, key=self.frequencies.get)
        del self.frequencies[least_frequent_key]
        return least_frequent_key

    def on_remove(self, key: str) -> None:
        self.frequencies.pop(key, None)