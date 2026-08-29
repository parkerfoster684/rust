"""StreamBuffer module."""

import math
import random


class StreamBuffer:
    """Small compute_adapter helper."""

    def __init__(self, seed: int = 97) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_adapter(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 97) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 97


def main() -> None:
    obj = StreamBuffer()
    print(obj.compute_adapter(97))


if __name__ == "__main__":
    main()
