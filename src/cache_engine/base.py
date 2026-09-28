from abc import ABC, abstractmethod
from typing import Any, Optional

class EvictionStrategy(ABC):
    @abstractmethod
    def on_get(self, key: str) -> None:
        pass

    @abstractmethod
    def on_put(self, key: str) -> None:
        pass

    @abstractmethod
    def evict_key(self) -> str:
        pass

    @abstractmethod
    def on_remove(self, key: str) -> None:
        pass

