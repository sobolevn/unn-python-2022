
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


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _store):
        raise UserExitException('See you next time!')

class DoneUndone():

    def change_done(self,store,flag,string):
        if len(store.items) == 0:
            print('There are no items in the storage.')
            return

        print('Select item id')

        while True:
            try:
                self._take_change_done(self._take_id(),store,flag)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break
        self._exit(string)

    def _take_id(self):
        user_id_take = int(input('Enter id: '))
        if user_id_take<0:
            raise IndexError('Index needs to be >0')
        return user_id_take

    def _take_change_done(self,index,store,flag):
        if index > len(store.items):
            raise IndexError('Out of list')
        store.items[index].done = flag;

    def _exit(self,string):
        print(string)


class DoneCommand(BaseCommand,DoneUndone):
    label = 'done'
    def perform(self,store):
        self.change_done(store,True,'Done')

class UndoneCommand(BaseCommand,DoneUndone):
    label = 'undone'
    def perform(self,store):
        self.change_done(store,False,'Undone')