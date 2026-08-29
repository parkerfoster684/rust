"""HybridRouter module."""

import math
import random


class HybridRouter:
    """Small fetch_provider helper."""

    def __init__(self, seed: int = 41) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_provider(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 41) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 41


def main() -> None:
    obj = HybridRouter()
    print(obj.fetch_provider(41))


if __name__ == "__main__":
    main()
