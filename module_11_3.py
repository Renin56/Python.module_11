import inspect
import sys
import os
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
    try:
        name = obj.__name__
    except AttributeError:
        name = 'Без имени'

    print(f'Интроспекция объекта: "{obj}" Имя объекта: "{name}"')
    info = {}

    try:
        type_obj = type(obj)
    except AttributeError:
        type_obj = 'Не удается определить имя'

    try:
        attr = dir(obj)
        attribute = [attribute for attribute in attr if not callable(getattr(obj, attribute))]
    except AttributeError:
        attribute = 'Объект не имеет атрибутов'

    try:
        attr = dir(obj)
        method = [method for method in attr if callable(getattr(obj, method)) and not method.startswith('__')]
    except AttributeError:
        method = 'Объект не имеет методов'

    try:
        attr = dir(obj)
        stat_method = [method for method in attr if callable(getattr(obj, method)) and method.startswith('__')]
    except AttributeError:
        stat_method = 'Объект не имеет методов'

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
    info['Статические методы'] = stat_method
    info['Модуль'] = obj_module
    info['Описание'] = docstring
    info['Версия'] = version
    info['Автор'] = author

    return info


print('-' * 50)
t = Introspec(42)
print(t)
print('-' * 50)
# pprint(introspection_info(Introspec))
pprint(introspection_info(7))
# pprint(introspection_info(inspect))
# pprint(introspection_info(requests))
