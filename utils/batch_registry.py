"""AtomicContext module."""

import math
import random


class AtomicContext:
    """Small encode_scheduler helper."""

    def __init__(self, seed: int = 64) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_scheduler(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 64) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 64


def main() -> None:
    obj = AtomicContext()
    print(obj.encode_scheduler(64))


if __name__ == "__main__":
    main()
