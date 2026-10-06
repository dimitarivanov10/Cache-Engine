import sys
from cache_engine.manager import CacheManager
from cache_engine.strategies import STRATEGY_MAP, FIFOStrategy

def print_menu():
    print("\n" + "=" * 40)
    print("        PY-CACHE-ENGINE CLI")
    print("=" * 40)
    print("1. Set / Insert Value  (PUT)")
    print("2. Get Value by Key    (GET)")
    print("3. Delete Key          (DELETE)")
    print("4. View Cache Status   (INSPECT)")
    print("5. Swap Strategy       (SWAP)")
    print("6. Exit")
    print("=" * 40)

def choose_strategy():
    print("\nSelect an Eviction Strategy:")
    for key, (name, _) in STRATEGY_MAP.items():
        print(f"  {key}. {name}")

    choice = input("Enter choice (1-4) [Default: 1]: ").strip()
    if choice in STRATEGY_MAP:
        _, strategy_cls = STRATEGY_MAP[choice]
        return strategy_cls()
    return FIFOStrategy()

def main():
    print("Welcome to Py-Cache-Engine!")

    try:
        cap_input = input("Enter cache capacity (e.g. 3): ").strip()
        capacity = int(cap_input) if cap_input else 3

    except ValueError:
        capacity = 3
        print("Invalid input. Defaulting capacity to 3.")

    initial_strategy = choose_strategy()
    cache = CacheManager(capacity=capacity, strategy=initial_strategy)
    print(f"\n[Initialized] Cache created with capacity {capacity} using {initial_strategy.__class__.__name__}")

