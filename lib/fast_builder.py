"""CoreFactory module."""

import math
import random


class CoreFactory:
    """Small encode_buffer helper."""

    def __init__(self, seed: int = 9) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_buffer(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 9) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 9


def main() -> None:
    obj = CoreFactory()
    print(obj.encode_buffer(9))


if __name__ == "__main__":
    main()
