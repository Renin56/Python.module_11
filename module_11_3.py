import inspect
from pprint import pprint

import requests


class Introspec:
    """Класс созданный в рамках изучения интроспекции"""
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return f'Класс для изучения интроспекции'

    def smt(self):
        return 2 + 5


def introspection_info(obj):
    print(f'Интроспекция объекта: {obj.__name__}')
    info = {}

    name = obj.__name__
    type_obj = type(obj)
    attribute = dir(obj)
    method = [method for method in attribute if callable(getattr(obj, method)) and not method.startswith('__')]
    try:
        author = obj.__author__
    except AttributeError:
        author = 'Без автора'

    try:
        version = obj.__version__
    except AttributeError:
        version = 'Без версии'

    try:
        obj_module = obj.__module__
    except AttributeError:
        obj_module = 'Без модуля'

    if not obj.__doc__:
        docstring = obj.__doc__
    else:
        docstring = 'Нет описания'

    info['Название'] = name
    info['Тип'] = type_obj
    info['Аттрибуты'] = attribute
    info['Методы'] = method
    info['Модуль'] = obj_module
    info['Описание'] = docstring
    info['Версия'] = version
    info['Автор'] = author

    return info


print('-' * 50)
t = Introspec(42)
print(t)
print('-' * 50)
pprint(introspection_info(Introspec))
# pprint(introspection_info(inspect))
# pprint(introspection_info(requests))
