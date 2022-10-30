
from ast import List
from todo.custom_exceptions import UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes


class BaseCommand(object):
    label: str

    def perform(self, store):
        raise NotImplementedError()


class ListCommand(BaseCommand):
    label = 'list'

    def perform(self, store):
        if len(store.items) == 0:
            print('There are no items in the storage.')
            return

        for index, obj in enumerate(store.items):
            print('{0}: {1}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    label = 'new'

    def perform(self, store):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{0}: {1}'.format(index, name))

        selection = None
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
        print()

        new_object = selected_class.construct()

        store.items.append(new_object)

        print('Added {0}'.format(str(new_object)))
        print()

        return new_object

    def _load_item_classes(self) -> dict:
        # Dynamic load:
        return dict(find_classes(BaseItem))

    def _select_item(self, classes):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >= 0')
        return list(classes.keys())[selection]


class DoneCommand(BaseCommand):
    label = 'done'

    def perform(self, store):
        ListCommand().perform(store)

        while True:
            try:
                selection = self._select_item(store)
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        store.items[selection].done = True
        print('Marked {0} as done'.format(str(store.items[selection])))
        print()

    def _select_item(self, store):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >= 0')
        if selection >= len(store.items):
            raise IndexError('Index needs to be < amount_of_items')
        return selection


class UndoneCommand(BaseCommand):
    label = 'undone'

    def perform(self, store):
        ListCommand().perform(store)

        while True:
            try:
                selection = DoneCommand()._select_item(store)
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        store.items[selection].done = False
        print('Marked {0} as undone'.format(str(store.items[selection])))        
        print()


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _store):
        raise UserExitException('See you next time!')
