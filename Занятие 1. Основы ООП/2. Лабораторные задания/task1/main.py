import doctest


class Box:
    """ Класс, который описывает коробку. """

    def __init__(self, height: [int, float], width: [int, float]):
        """
        Определяем коробку
        :param height: Высота коробки
        :param width: Ширина коробки

        Пример:
        >>> box = Box(60, 80)  # инициализация экземпляра класса
        """

        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.height = height
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота коробки должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота коробки должна быть больше 0")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина коробки должна быть типа int или float")
        if width < 0:
            raise ValueError("Ширина коробки должна быть больше 0")
        self.width = width

    def get_height(self):
        """Метод, который определяет высоту
         :return: возвращает значение атрибута height"""
        ...

    def get_width(self):
        """Метод, который определяет ширину
        :return: возвращает значение атрибута width"""
        ...

    def is_empty_box(self):
        """
        Функция которая проверяет является ли коробка пустой
        :return: Является ли коробка пустой

        Примеры:
        >>> box = Box(100, 50)
        >>> box.is_empty_box()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest

