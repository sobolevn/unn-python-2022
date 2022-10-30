import inspect
import sys


def find_classes(base_class) -> tuple:
    return inspect.getmembers(
        sys.modules[base_class.__module__],
        _reflect_filter(base_class),
    )


def _reflect_filter(base_class):
    def class_filter(klass):
        return inspect.isclass(
            klass,
        ) and klass.__module__ == base_class.__module__ and issubclass(
            klass, base_class,
        ) and klass is not base_class
    return class_filter
