from todo.custom_exceptions import UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes


class BaseCommand(object):
    label: str

    def perform(self, _storage):
        raise NotImplementedError()


class ListCommand(BaseCommand):
    label = 'list'

    def perform(self, storage):
        storage.print()
        print()


class NewCommand(BaseCommand):
    label = 'new'

    def perform(self, storage):
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


class DoneCommand(BaseCommand):
    label = 'done'

    def perform(self, storage):

        storage.print()
        if storage.is_empty():
            print()
            return

        selected_item = None
        while True:
            try:
                selected_item = self._select_item(storage)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        print('{0} has been marked done'.format(selected_item))
        print()
        selected_item.mark_done();

    def _select_item(self, storage):
        selection = int(input('Choose number of item: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return storage.items[selection]


class UndoneCommand(BaseCommand):
    label = 'undone'

    def perform(self, storage):

        storage.print()
        if storage.is_empty():
            return

        selected_item = None
        while True:
            try:
                selected_item = self._select_item(storage)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        print('{0} has been marked done'.format(selected_item))
        print()
        selected_item.mark_undone();

    def _select_item(self, storage):
        selection = int(input('Choose number of item: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return storage.items[selection]


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _storage):
        raise UserExitException('See you next time!')
