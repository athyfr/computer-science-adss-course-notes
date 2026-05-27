"""An implementation of an unordered dictionary."""

from typing import Any


class UnorderedDictionary[ElementType = Any]:
    """An implementation of an unordered dictionary.

    Created to demonstrate various sorting and searching algorithms.
    """

    def __init__(self, keys: list[str], values: list[ElementType]) -> None:
        """Initialize using raw `keys` and `values` lists.

        Args:
            keys: Keys of the elements.
            values: Values of each elements.

        Raises:
            ValueError:
                If the length of the `keys` and `values` lists do not match.
        """
        if len(keys) != len(values):
            msg: str = "Length of `keys` and `values` lists does not match."
            raise ValueError(msg)

        self.keys = keys
        self.values = values

    @staticmethod
    def from_dict(
        base_dict: dict[str, ElementType],
    ) -> UnorderedDictionary[ElementType]:
        """Create an `UnorderedDictionary` based on a Python `dict`.

        Args:
            base_dict: The `dict` to get the keys and values from.

        Returns:
            A `UnorderedDictionary` with the same keys and values as the
            provided `dict`.
        """
        return UnorderedDictionary(
            list(base_dict.keys()),
            list(base_dict.values()),
        )

    def get_by_linear_search(self, key: str) -> ElementType | None:
        """Get an element of the dictionary using a linear search algorithm.

        This is the simplest (and most inefficient) searching algorithm.

        Args:
            key: The key associated with the value to get.

        Returns:
            The value associated with the key, or `None` if the key is
            not defined.
        """
        found_index: int = -1

        for i, key_i in enumerate(self.keys):
            if key_i == key:
                found_index = i
                break

        if found_index == -1:
            return None

        return self.values[found_index]
