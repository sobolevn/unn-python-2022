from typing import Literal

from todo.custom_exceptions import UnitializedStorage, UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes
from todo.storage import Storage


class BaseCommand(object):
    label: str

    def perform(self, _storage: Storage) -> None:
        raise NotImplementedError()


class ListCommand(BaseCommand):
    label = 'list'

    def perform(self, storage: Storage) -> None:
        storage.print()
        print()


class NewCommand(BaseCommand):
    label = 'new'

    def perform(self, storage: Storage) -> None:
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{0}: {1}'.format(index, name))

        selected_key = None

        while True:
            try:
                selected_key = self._select_item(classes)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        selected_class = classes[selected_key]
        print('Selected: {0}'.format(selected_class.__name__))

        new_object = selected_class.construct()

        if storage.items is None:
            raise UnitializedStorage

        storage.items.append(new_object)
        print('Added {0}'.format(str(new_object)))
        print()

        return new_object

    def _load_item_classes(self) -> dict:
        # Dynamic load:
        return dict(find_classes(BaseItem))

    def _select_item(self, classes):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return list(classes.keys())[selection]


class BaseMarkCommand(object):
    operation = Literal['mark_done', 'mark_undone']

    def perform(self, storage: Storage) -> None:
        storage.print()
        if storage.is_empty():
            print()
            return

        selected_item = self._select_item(storage)

        print('{0} has been marked done'.format(selected_item))
        print()

        operation = getattr(selected_item, str(self.operation), None)
        assert operation is not None
        operation()

    def _select_item(self, storage: Storage) -> BaseItem:
        while True:
            try:
                selection = int(input('Choose number of item: '))
                if selection < 0:
                    raise IndexError('asdf')
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break
        if storage.items is None:
            raise UnitializedStorage
        return storage.items[selection]


class DoneCommand(BaseMarkCommand, BaseCommand):
    label = 'done'
    operation = 'mark_done'


class UndoneCommand(BaseMarkCommand, BaseCommand):
    label = 'undone'
    operation = 'mark_undone'


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _storage: Storage) -> None:
        raise UserExitException('See you next time!')
