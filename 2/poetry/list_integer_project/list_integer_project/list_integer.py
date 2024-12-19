# list_integer_project/list_integer.py

class ListInteger(list):
    def __init__(self, iterable=()):
        # Проверяем элементы в переданном итерируемом объекте
        if not all(isinstance(x, int) for x in iterable):
            raise TypeError("можно передавать только целочисленные значения")
        super().__init__(iterable)

    def __setitem__(self, index, value):
        # Проверяем, что новое значение — целое число
        if not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        super().__setitem__(index, value)

    def append(self, value):
        # Проверяем, что добавляемое значение — целое число
        if not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        super().append(value)
