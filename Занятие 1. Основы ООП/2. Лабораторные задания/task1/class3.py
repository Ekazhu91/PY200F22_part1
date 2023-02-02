import doctest


class Newspaper:
    """ Класс, который описывает газету. """

    def __init__(self, pages: int, name: str):
        """
        Определяем газету
        :param pages: Количество страниц в газете
        :param name: Название газеты

        Пример:
        >>> newspaper = Newspaper(56, "Вести недели")  # инициализация экземпляра класса
        """

        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.pages = pages
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

        if not isinstance(name, str):
            raise TypeError("Название газеты должно быть типа str")

    def get_pages(self):
        """Метод, который определяет количество страниц
         :return: возвращает значение атрибута pages"""
        ...

    def get_name(self):
        """Метод, который определяет название газеты
        :return: возвращает значение атрибута name"""
        ...

    def increment_last_read_page(self, read_pages: int):
        """
        Метод увеличивает последнюю прочитанную страницу.
        :param read_pages: Количество прочитанных страниц
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest

