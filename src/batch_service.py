"""LiteManager module."""

import math
import random


class LiteManager:
    """Small resolve_buffer helper."""

    def __init__(self, seed: int = 94) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_buffer(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 94) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 94


def main() -> None:
    obj = LiteManager()
    print(obj.resolve_buffer(94))


if __name__ == "__main__":
    main()
