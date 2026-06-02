"""An implementation of an unordered dictionary.

Created to demonstrate various sorting and searching algorithms.

Classes:
    UnorderedDictionary:
        An implementation of an unordered dictionary; the main focus of
        this module.
"""

from typing import Any


class UnorderedDictionary[ElementType = Any]:
    """An implementation of an unordered dictionary.

    Created to demonstrate various sorting and searching algorithms.
    """

    # ---- Initializers ----

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

    # ---- Sort Implementations ----

    # ---- Getter Implementations ----

    type _GetterReturnType = tuple[ElementType, int] | None

    def get_by_linear_search(self, key: str) -> _GetterReturnType:
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

        return self.values[found_index], found_index

    def get_by_binary_search(self, key: str) -> _GetterReturnType:
        """Get an element of the dictionary using the Binary Search algorithm.

        The dictionary is expected to be sorted lexicographically before

        Args:
            key: The key associated with the value to get.

        Returns:
            The value associated with the key, or `None` if the key is
            not defined.
        """
        # Signifies the range that may contain the key we want.
        search_range: tuple[int, int] = (0, len(self.keys) - 1)

        while True:
            checked_key_index: int = int(
                (search_range[0] + search_range[1]) / 2
            )
            checked_key: str = self.keys[checked_key_index]

            if checked_key < key:
                search_range = (checked_key_index + 1, search_range[1])

            elif checked_key > key:
                search_range = (search_range[0], checked_key_index - 1)

            elif checked_key == key:
                return self.values[checked_key_index], checked_key_index

            # This always eventually is true when the key is undefined.
            if search_range[0] > search_range[1]:
                return None

    # ---- Dunder Methods ----
