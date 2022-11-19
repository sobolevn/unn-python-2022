
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
            raise IndexError('Index needs to be >0')
        return list(classes.keys())[selection]


class MarkCommand(object):

    def perform(self, store):
        x = 0

        for obj in store.items:
            if str(obj)[0] == self.char_command:
                x += 1
        if x == 0:
            print("There are no {0} items in the storage.".format(self.char_command))
            return

        for index, obj in enumerate(store.items):
            if str(obj)[0] == self.char_command:
                print('{0}: {1}'.format(index, str(obj)))

        selected_item = self.select_item(store)

        print("{0} has been {1}\n".format(selected_item, self.operation))

        operation = getattr(selected_item, str(self.operation), None)
        assert operation is not None
        operation()

    def select_item(self, store):
        while True:
            try:
                user_selection = int(input("Input number of item: "))
                if user_selection < 0 or str(store.items[user_selection])[0] != self.char_command:
                    raise IndexError()
            except ValueError:
                print("Bad input")
            except IndexError:
                print("Bad index")
            else:
                break
        if store.items is None:
            print("There are no items in storage")
        return store.items[user_selection]


class DoneCommand(MarkCommand, BaseCommand):
    label = "done"
    char_command = '-'
    operation = "mark_done"


class UndoneCommand(MarkCommand, BaseCommand):
    label = "undone"
    char_command = '+'
    operation = "mark_undone"


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _store):
        raise UserExitException('See you next time!')
