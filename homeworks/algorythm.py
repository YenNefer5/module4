

class MyDict:
    def __init__(self):
        self._data = []

    def _find_index(self, key):
        # метод: вернуть индекс пары с данным ключом или -1
        for i, (k, _) in enumerate(self._data):
            if k == key:
                return i
        return -1

    def __getitem__(self, key):
        idx = self._find_index(key)
        if idx != -1:
            return self._data[idx][1]
        return None

    def __setitem__(self, key, value):
        idx = self._find_index(key)
        if idx != -1:
            self._data[idx] = (key, value)
        else:
            self._data.append((key, value))

    def __delitem__(self, key):
        idx = self._find_index(key)
        if idx != -1:
            self._data.pop(idx)

    def keys(self):
        return [k for (k, _) in self._data]

    def values(self):
        return [v for (_, v) in self._data]

    def items(self):
        return list(self._data)

    def __str__(self):
        # строковое представление в виде обычного словаря для удобства отладки
        parts = []
        for k, v in self._data:
            parts.append(f"{repr(k)}: {repr(v)}")
        return "{" + ", ".join(parts) + "}"

    def __contains__(self, key):
        return key in self._data




my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']