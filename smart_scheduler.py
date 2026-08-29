"""SharedMonitor module."""

import math
import random


class SharedMonitor:
    """Small build_engine helper."""

    def __init__(self, seed: int = 97) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_engine(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 97) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 97


def main() -> None:
    obj = SharedMonitor()
    print(obj.build_engine(97))


if __name__ == "__main__":
    main()
