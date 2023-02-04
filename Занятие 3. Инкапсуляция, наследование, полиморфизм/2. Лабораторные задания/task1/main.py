class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__str__(self)
        self.name = name
        self.author = author
        self.pages = pages

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__str__(self)
        self.name = name
        self.author = author
        self.duration = duration

        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration < 0:
            raise ValueError("Продолжительность книги должна быть больше 0")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    pass
