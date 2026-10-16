# Py-Cache-Engine 🚀

A lightweight, modular, object-oriented cache engine written in Python. It provides an interactive Command Line Interface (CLI) to experiment with and evaluate standard cache eviction policies in real-time.

Designed using the **Strategy Design Pattern**, `Py-Cache-Engine` maintains strict separation between core data storage (`CacheManager`) and tracking/eviction behavior (`EvictionStrategy`).

## Key Features

* **Multiple Eviction Strategies**:
  * **FIFO** (First-In, First-Out): Evicts the oldest entry based on insertion order.
  * **LRU** (Least Recently Used): Evicts the item least recently accessed or updated using `collections.OrderedDict`.
  * **LFU** (Least Frequently Used): Evicts the item with the lowest access frequency using `collections.Counter`.
  * **MRU** (Most Recently Used): Evicts the item accessed most recently.
* **Dynamic Strategy Swapping**: Switch eviction algorithms on the fly without clearing or losing existing cached data.
* **Interactive CLI**: Live operational menu for executing `PUT`, `GET`, `DELETE`, and `INSPECT` operations.
* **Extensible Architecture**: Easily add new custom caching algorithms by inheriting from the `EvictionStrategy` abstract base class.

## Project Structure

```text
Cache-Engine/
├── src/
│   ├── cache_engine/
│   │   ├── __init__.py
│   │   ├── base.py                 # Contains EvictionStrategy ABC
│   │   ├── manager.py              # Contains CacheManager
│   │   └── strategies/
│   │       ├── __init__.py         # Exports STRATEGY_MAP and classes
│   │       ├── fifo.py
│   │       ├── lru.py
│   │       ├── lfu.py
│   │       └── mru.py
│   └── main.py                     # CLI entry point
├── README.md
└── requirements.txt
```

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/py-cache-engine.git
   cd py-cache-engine
   ```

2. **Run the CLI:**

   The project uses a standard `src/` layout. Execute the main script directly using Python:

   ```bash
   python src/main.py
   ```

   > **Note:** `main.py` automatically resolves the `src/` module path at runtime, so no external environment variables are required.

## Usage Example

Upon launching, set your cache capacity and initial strategy, then interact with the menu:

```text
Welcome to Py-Cache-Engine!
Enter cache capacity (e.g. 3): 3

Select an Eviction Strategy:
  1. FIFO (First-In, First-Out)
  2. LRU (Least Recently Used)
  3. LFU (Least Frequently Used)
  4. MRU (Most Recently Used)
Enter choice (1-4) [Default: 1]: 2

[Initialized] Cache created with capacity 3 using LRUStrategy

========================================
        PY-CACHE-ENGINE CLI
========================================
1. Set / Insert Value  (PUT)
2. Get Value by Key    (GET)
3. Delete Key          (DELETE)
4. View Cache Status   (INSPECT)
5. Swap Strategy       (SWAP)
6. Exit
========================================
```

## Architecture Details

The core of the system relies on two main components:

1. **`CacheManager`**: Acts as the central warehouse. It holds a standard Python `dict` for $O(1)$ data storage and retrieval. It knows nothing about eviction rules; it simply alerts the active strategy whenever a `GET`, `PUT`, or `DELETE` occurs.
2. **`EvictionStrategy`**: An abstract base class defining lifecycle hooks (`on_get`, `on_put`, `evict_key`, `on_remove`). Concrete implementations (like `LRUStrategy` or `LFUStrategy`) manage lightweight internal data structures (like `OrderedDict` or `Counter`) to track only the keys and their relevant metadata.