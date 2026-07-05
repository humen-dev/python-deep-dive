from collections.abc import Sequence
from random import shuffle
from collections.abc import Iterable, Hashable
from collections import Counter
from decimal import Decimal
from fractions import Fraction


def sample[T](population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError("size must be >= 1")

    result = list(population)
    shuffle(result)
    return result[:size]


# Restricted TypeVar
def mode[NumberT: (float, Decimal, Fraction)](data: Iterable[NumberT]) -> NumberT:
    return 1


# Bounded TypeVar
def mode_v2[HashableT: Hashable](data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]
