import sys
from cache_engine.manager import CacheManager
from cache_engine.strategies.fifo import FIFOStrategy
from cache_engine.strategies.lru import LRUStrategy

STRATEGY_MAP = {
    "1": ("FIFO (First-In, First-Out)", FIFOStrategy),
    "2": ("LRU (Least Recently Used)", LRUStrategy),
}


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

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            key = input("Enter Key: ").strip()
            val = input("Enter Value: ").strip()

            if key:
                cache.put(key, val)
                print(f"[Sucess] Set '{key}' = '{val}'")
            else:
                print("[Error] Key cannot be empty.")

        elif choice == "2":
            key = input("Enter Key to fetch: ").strip()
            val = cache.get(key)
            if val is not None:
                print(f"[FOUND] {key} -> {val}")
            else:
                print(f"[MISS] Key '{key}' not found in cache")

        elif choice == "3":
            key = input("Enter Key to delete: ").strip()
            if cache.delete(key):
                print(f"[Deleted] Key '{key}' removed.")
            else:
                print(f"[Error] Key '{key}' not found.")

        elif choice == "4":
            print("\n--- Current Cache State ---")
            print(f"Capacity: {len(cache.storage)} / {cache.capacity}")
            print(f"Active Strategy: {cache.strategy.__class__.__name__}")
            print(f"Contents: {cache.storage}")

        elif choice == "5":
            new_strategy = choose_strategy()
            cache.set_strategy(new_strategy)

        elif choice == "6":
            print("\nExiting Cache Engine. Goodbye!")
            sys.exit(0)

        else:
            print("[Error] Invalid option. Please select 1-6.")


if __name__ == "__main__":
    main()

