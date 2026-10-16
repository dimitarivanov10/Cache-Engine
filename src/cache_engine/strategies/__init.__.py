from cache_engine.strategies.fifo import FIFOStrategy
from cache_engine.strategies.lru import LRUStrategy

STRATEGY_MAP = {
    "1": ("FIFO (First-In, First-Out)", FIFOStrategy),
    "2": ("LRU (Least Recently Used)", LRUStrategy),
}

__all__ = [
    "FIFOStrategy",
    "LRUStrategy",
    "STRATEGY_MAP",
]