"""FastDispatcher module."""

import math
import random


class FastDispatcher:
    """Small compute_registry helper."""

    def __init__(self, seed: int = 19) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_registry(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 19) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 19


def main() -> None:
    obj = FastDispatcher()
    print(obj.compute_registry(19))


if __name__ == "__main__":
    main()
