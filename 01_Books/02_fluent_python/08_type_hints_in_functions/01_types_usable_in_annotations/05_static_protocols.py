from typing import Protocol, Any
from collections.abc import Iterable


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


def top[LT: SupportsLessThan](series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
