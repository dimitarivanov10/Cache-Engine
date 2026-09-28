from collections import deque
from cache_engine.base import EvictionStrategy

class FIFOStrategy(EvictionStrategy):
    """
    Evicts the oldest key inserted into the cache, regardless of 
    how frequently or recently it was accessed.
    """

    def __init__(self):
        self.order: deque[str] = deque()

    def on_get(self, key: str) -> None:
        pass

    def on_put(self, key: str) -> None:
        if key not in self.order:
            self.oder.append(key)

    def evict_key(self) -> str:
        if not self.order:
            raise KeyError("Cannot evict from an empty FIFO tracker. ")
        return self.order.popleft()

    def on_remove(self, key: str) -> None:
        if key in self.order:
            self.order.remove(key)