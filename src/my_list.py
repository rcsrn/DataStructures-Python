class Element():
    __slots__ = ("__value")

    def __init__(self, string):
        self.__value = string

    def get_value(self):
        return self.__value

    def __str__(self):
        return self.__value

class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.element = None

    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def get_prev(self):
        return self.prev

    def set_prev(self, prev_node):
        self.prev = prev_node


class List():
    __slots__ = ("__head", "__tail", "__length")

    class Node:
        def __init__(self):
            self.prev = None
            self.next = None
            self.element = None

        def set_element(self, element):
            self.element = element

        def get_element(self):
            return self.element

        def get_next(self):
            return self.next

        def set_next(self, next_node):
            self.next = next_node

        def get_prev(self):
            return self.prev
            
        def set_prev(self, prev_node):
            self.prev = prev_node

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add_at(self, element, i):
        if not isinstance(element, Element) or i < 0 or i > self.__length:
            raise ValueError("It is not possible to add this element to the list.")

        node = Node()
        node.set_element(element)

        if self.__length == 0:
            self.__head = node
            self.__tail = node
        else:
            if self.__length == 1:
                if i == 0:
                    node.set_next(self.__head)
                    self.__head.set_prev(node)
                else:
                    node.set_prev(self.__tail)
                    self.__tail.set_next(node)
            else:
                change = self.get_node_at(i)
                node.set_prev(change.get_prev)
                change.__prev.set_next(node)
                node.set_next(change)
                change.set_prev(node)
                
        self.__length = self.__length + 1
            
        
    def get_node_at(self, index):
        it = self.__head
        for i in range(self.__length):
            if i == index:
                return it
            it = it.__next

    def get_element_at(self, index):
        node = self.get_node_at(index).get_element()
        return node.get_value()

    def is_empty(self):
        return self.__length == 0

    def getLength(self):
        return self.__length

    def __str__(self):
        if self.is_empty():
            return "[]"
        it = self.__head
        string = "[ "
        string += it.get_element().__str__()
        it = it.get_next()
        for i in range(self.__length):
            string += ", " + it.get_element().__str__()
        string += "]"
        return string
    

