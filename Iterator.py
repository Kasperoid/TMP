from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

"""
Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections - Iterable, Iterator.
"""

class AlphabeticalOrderIterator(Iterator):

    _position: int = None # Текущее положение обхода

    _reverse: bool = False # Направление обхода

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any: # Возвращает следующий элемент
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []


    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:

        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")