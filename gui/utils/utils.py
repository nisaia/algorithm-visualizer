import importlib
import random
import typing


def load_class(path: str):
    module_path, class_name = path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)

def get_unique_array(_min: int, _max: int, length: int) -> typing.List:

    _set = set()
    while len(_set) < length:
        _set.add(random.randint(_min, _max))

    return list(_set)

def get_sorted_unique_array(_min: int, _max: int, length: int) -> typing.List:

    return sorted(get_unique_array(_min, _max, length))