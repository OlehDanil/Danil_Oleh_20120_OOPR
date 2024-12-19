class ListInteger(list):
    def __init__(self, initial_list=None):
        super().__init__()
        if initial_list is not None:
            for item in initial_list:
                self.append(item)  # Используем переопределённый append

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(value)