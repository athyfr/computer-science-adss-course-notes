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
        self._len = len(keys)
        self._sorted = False

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

    # Elementary Sort Operations

    def _move_element(self, i_from: int, i_to: int) -> tuple[int, int]:
        self.keys.insert(i_to, self.keys.pop(i_from))
        self.values.insert(i_to, self.values.pop(i_from))

        return i_from, i_to

    def _swap_elements(self, i1: int, i2: int) -> tuple[int, int]:
        self.keys[i1], self.keys[i2] = self.keys[i2], self.keys[i1]
        self.values[i1], self.values[i2] = self.values[i2], self.values[i1]

        return i1, i2

    # Sort Algorithms

    def sort_by_bubble(self) -> None:
        """Sort the dictionary using the Bubble Sort algorithm.

        Based on <https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/>.
        """
        # Loop over each element, ensuring each one is in the
        # correct place.
        for i in range(self._len):
            swapped = False

            # Loop over each element *after* element `i`, as `i` and before
            # are already in place.
            for j in range(self._len - i - 1):
                if self.keys[j] > self.keys[j + 1]:
                    # Swap the entry with its successor.
                    self._swap_elements(j, j + 1)
                    # Track that this operation happened (see below).
                    swapped = True

            # If the inner loop didn't cause any sorting, this means no
            # more sorting is necessary.
            if not swapped:
                break

    def sort_by_insertion(self) -> None:
        """Sort the dictionary using the Insertion Sort algorithm.

        Based on <https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/>
        """
        # `i` represents the index of the first element which is unsorted.
        # Everything before `i` is sorted.
        for i in range(1, self._len):
            # Check its relation to each sorted element.
            #
            #  This can use any search algorithm, but here I'm using
            # a linear search for simplicity.
            #
            # As a little bit of a hack, it will end up comparing
            # against itself as a final case when it ends up at the
            # end of the sorted portion.
            for j in range(i + 1):
                if self.keys[j] >= self.keys[i]:
                    # Move it to the sorted position.
                    if i != j:
                        self._move_element(i, j)
                    break

        self._sorted = True

    # Default sort implementation
    def sort(self) -> None:
        """Sort the dictionary using an arbitrary algorithm."""
        self.sort_by_insertion()

    # ---- Getter Implementations ----

    type _GetterReturnType = tuple[ElementType, int]

    def get_by_linear_search(self, key: str) -> _GetterReturnType:
        """Get an element of the dictionary using a linear search algorithm.

        This is the simplest (and most inefficient) searching algorithm.

        Args:
            key: The key associated with the value to get.

        Returns:
            A tuple of the value associated with the key, and its index, for
            internal/advanced purposes.

        Raises:
            KeyError: If the key does not exist.
        """
        found_index: int = -1

        for i, key_i in enumerate(self.keys):
            if key_i == key:
                found_index = i
                break

        if found_index == -1:
            raise KeyError

        return self.values[found_index], found_index

    def get_by_binary_search(self, key: str) -> _GetterReturnType:
        """Get an element of the dictionary using the Binary Search algorithm.

        Args:
            key: The key associated with the value to get.

        Returns:
            A tuple of the value associated with the key, and its index, for
            internal/advanced purposes.

        Raises:
            KeyError: If the key does not exist.
        """
        if not self._sorted:
            self.sort()

        # Signifies the range that may contain the key we want.
        search_range: tuple[int, int] = (0, len(self.keys) - 1)

        while True:
            checked_key_index = int((search_range[0] + search_range[1]) / 2)
            checked_key: str = self.keys[checked_key_index]

            if checked_key < key:
                search_range = (checked_key_index + 1, search_range[1])

            elif checked_key > key:
                search_range = (search_range[0], checked_key_index - 1)

            elif checked_key == key:
                return self.values[checked_key_index], checked_key_index

            # This always eventually is true when the key is undefined.
            if search_range[0] > search_range[1]:
                raise KeyError

    # Default getter implementation
    def get(self, key: str) -> _GetterReturnType:
        """Get an element of the dictionary without specifying algorithm.

        Args:
            key: The key associated with the value to get.

        Returns:
            A tuple of the value associated with the key, and its index, for
            internal/advanced purposes.
        """
        return self.get_by_binary_search(key)

    # ---- Utility Methods ----

    def to_dict(self) -> dict:
        """Convert to a Python builtin `dict`.

        Returns:
            The converted Python `dict`.
        """
        output: dict[str, ElementType] = {}

        for i in range(self._len):
            output[self.keys[i]] = self.values[i]

        return output

    # ---- Dunder Methods ----

    def __len__(self) -> int:
        """Get the number of entries in the dictionary.

        Returns:
            An integer representing the number of entries in the dictionary.
        """
        return self._len

    def __delitem__(self, key: str) -> None:
        """Delete an element of the dictionary."""
        index: int = self.get(key)[1]

        del self.keys[index]
        del self.values[index]

    def __repr__(self) -> str:
        """Represent this object as a string.

        Returns:
            The string representation of the dictionary.
        """
        return str(self.to_dict())
