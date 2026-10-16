from typing import Any, Optional
from cache_engine.base import EvictionStrategy

class CacheManager:

    def __init__(self, capacity: int, strategy: EvictionStrategy):
        if capacity <= 0:
            raise ValueError("Cache capacity must be greater than 0.")

        self.capacity = capacity
        self.strategy = strategy
        self.storage: dict[str, Any] = {}

    def get(self, key: str) -> Optional[Any]:
        if key not in self.storage:
            return None
        self.strategy.on_get(key)
        return self.storage[key]

    def put(self, key: str, value: Any) -> None:
        if key in self.storage:
            self.storage[key] = value
            self.strategy.on_put(key)
            return

        if len(self.storage) >= self.capacity:
            evicted_key = self.strategy.evict_key()
            del self.storage[evicted_key]
            print(f"\n [Eviction] Cache full. Evicted key '{evicted_key} using {self.strategy.__class__.__name__}'")

        self.storage[key] = value
        self.strategy.on_put(key)

    def delete(self, key: str) -> bool:
        if key in self.storage:
            del self.storage[key]
            self.strategy.on_remove(key)
            return True
        return False

    def set_strategy(self, new_strategy: EvictionStrategy) -> None:
        self.strategy = new_strategy
        for key in self.storage:
            self.strategy.on_put(key)

        print(f"\n [Strategy Swapped] Active strategy is now {new_strategy.__class__.__name__}")