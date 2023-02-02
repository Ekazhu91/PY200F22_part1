import doctest


class Bottle:
    """ Класс, который описывает бутылку. """

    def __init__(self, volume_bootle: [int, float], volume_water: [int, float]):
        """
        Определяем коробку
        :param volume_bootle: Объем бутылки
        :param volume_water: Объем воды в бутылке

        Пример:
        >>> bootle = Bottle(500, 250)  # инициализация экземпляра класса
        """

        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.volume_bootle = volume_bootle
        self.volume_water = volume_water

        if not isinstance(volume_bootle, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if volume_bootle < 0:
            raise ValueError("Объем бутылки должен быть больше 0")
        self.volume_bootle = volume_bootle

        if not isinstance(volume_water, (int, float)):
            raise TypeError("Объем воды в бутылке должен быть типа int или float")
        if volume_water < 0:
            raise ValueError("Объем воды в бутылке должен быть больше 0")
        self.volume_water = volume_water

    def get_volume_bootle(self):
        """Метод, который определяет объем бутылки
         :return: возвращает значение атрибута volume_bootle"""
        ...

    def get_volume_water(self):
        """Метод, который определяет объем воды в бутылке
        :return: возвращает значение атрибута volume_water"""
        ...

    def is_empty_bottle(self):
        """
        Функция которая проверяет является ли бутылка пустой
        :return: является ли бутылка пустой

        Примеры:
        >>> bottle = Bottle(500, 250)
        >>> bottle.is_empty_bottle()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest

