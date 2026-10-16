from cache_engine.strategies.fifo import FIFOStrategy
from cache_engine.strategies.lru import LRUStrategy
# from cache_engine.strategies.lfu import LFUStrategy
# from cache_engine.strategies.mru import MRUStrategy

STRATEGY_MAP = {
    "1": ("FIFO (First-In, First-Out)", FIFOStrategy),
    "2": ("LRU (Least Recently Used)", LRUStrategy),
    # "3": ("LFU (Least Frequently Used)", LFUStrategy),
    # "4": ("MRU (Most Recently Used)", MRUStrategy),
}

__all__ = [
    "FIFOStrategy",
    "LRUStrategy",
    "STRATEGY_MAP",
]