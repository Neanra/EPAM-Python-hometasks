"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class CustomListIterator:
    def __init__(self, initial_item):
        self.__item = initial_item

    def __iter__(self):
        return self

    def __next__(self):
        if self.__item is None:
            raise StopIteration

        result = self.__item.value
        self.__item = self.__item.next
        return result

class CustomList:
    def __init__(self, *data):
        self.__head = None
        for datum in reversed(data):
            self.add_start(datum)

    def append(self, value):
        if self.__head == None:
            self.add_start(value)
            return

        current_item = self.__head
        while current_item.next is not None:
            current_item = current_item.next
        
        current_item.next = Item(value, None)
    
    def add_start(self, value):
        self.__head = Item(value, self.__head)

    def remove(self, value):
        if self.__head == None:
            raise ValueError
        if self.__head.value == value:
            self.__head = self.__head.next
            return
        
        previous_item = self.__head
        current_item = self.__head.next
        while current_item is not None:
            if current_item.value == value:
                previous_item.next = current_item.next
                return
            previous_item = current_item
            current_item = current_item.next

        raise ValueError

    def __getitem_impl(self, index):
        if index < 0:
            raise IndexError

        current_item  = self.__head
        current_index = 0
        while current_item is not None:
            if current_index == index:
                return current_item
            current_item = current_item.next
            current_index += 1

        raise IndexError

    def __getitem__(self, index):
        return self.__getitem_impl(index).value

    def __setitem__(self, index, value):
        self.__getitem_impl(index).value = value

    def __delitem__(self, index):
        if index < 0:
            raise IndexError

        previous_item = None
        current_item  = self.__head
        current_index = 0
        while current_item is not None:
            if current_index == index:
                if current_item is not self.__head:
                    assert previous_item is not None
                    previous_item.next = current_item.next
                else:
                    self.__head = self.__head.next
                return
            previous_item = current_item
            current_item = current_item.next
            current_index += 1

        raise IndexError

    def find(self, value):
        current_item = self.__head
        current_index = 0
        while current_item is not None:
            if current_item.value == value:
                return current_index
            current_item = current_item.next
            current_index += 1

        raise ValueError

    def clear(self):
        self.__head = None

    def __len__(self):
        current_item = self.__head
        current_index = 0
        while current_item is not None:
            current_item = current_item.next
            current_index += 1

        return current_index

    def __iter__(self):
        return CustomListIterator(self.__head)