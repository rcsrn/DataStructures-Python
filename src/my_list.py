class Element():
    __slots__ = ("__value")

    def __init__(self, string):
        self.__value = string

    def get_value(self):
        return self.__value

    def __str__(self):
        return self.__value

class List():
    __slots__ = ("__head", "__tail", "__length")
    
    class Node():
        def __init__(self):
            self.__prev = None
            self.__next = None
            self.__element = None

        def set_element(self, element):
            self.__element = element

        def get_element(self):
            return self.__element

        def get_next(self):
            return self.__next

        def set_next(self, next_node):
            self.__next = next_node

        def get_prev(self):
            return self.__prev
            
        def set_prev(self, prev_node):
            self.__prev = prev_node

        def __next__(self):
            if self.__next == None:
                raise StopIteration
            else:
                self = self.__next
                return self.__element

    class Iterator():
        def __init__(self, head):
            self.__next_node = head

        def get_next(self):
            return self.__next_node
            
        def __next__(self):
            if self.__next_node == None:
                raise StopIteration
            element = self.__next_node.get_element()
            self.__next_node = self.get_next().get_next()
            return element
            
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    @classmethod
    def from_list(cls, list):
        new_list = List()
        i = 0
        for element in list:
            if not isinstance(element, Element):
                element = Element(element.__str__())
            new_list.add_at(element, i)
            i = i + 1
        return new_list
    
        
    def add_at(self, element, i):
        if not isinstance(element, Element) or i < 0 or i > self.get_length():
            raise ValueError("It is not possible to add this element to the list.")

        node = self.Node()
        node.set_element(element)

        if i == 0:
            self.add_to_start(node)
        elif i == self.__length:
            self.add_to_end(node)
        else:
             change = self.get_node_at(i)
                
             node.set_prev(change.get_prev())            
             prev_old = change.get_prev()
             prev_old.set_next(node)
             node.set_next(change)
             change.set_prev(node)             
                
        self.__length = self.__length + 1

    def add_to_start(self, node):
        if self.__length == 0:
            self.__head = node
            self.__tail = node
        else:
            node.set_next(self.__head)
            self.__head.set_prev(node)
            self.__head = node

    def add_to_end(self, node):
        if self.__length == 0:
            self.__head = node
            self.__tail = node
        else:
            node.set_prev(self.__tail)
            self.__tail.set_next(node)
            self.__tail = node
        
    def get_node_at(self, index):
        if index < 0 or index > self.__length - 1:
            raise ValueError("It is not an acceptable index.")
        it = self.__head
        for i in range(self.__length):
            if i == index:
                return it
            it = it.get_next()

    def get_element_at(self, index):
        element = self.get_node_at(index).get_element()
        return element.get_value()

    def is_empty(self):
        return self.__length == 0

    def get_length(self):
        return self.__length

    def __iter__(self):
        return self.Iterator(self.__head)

    def __str__(self):
        if self.is_empty():
            return "[]"
        it = self.__head
        string = "["
        for i in range(self.__length - 1):
            string += "'" + it.get_element().get_value() + "', "
            it = it.get_next()
        string += "'" + it.get_element().get_value() + "']"
        return string

    def clean(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def removeByValue(self, value):
        it = self.__head
        while it != None:
            if it.get_element().get_value() == value:              
                if (it == self.__head):
                    it.get_next().set_prev(None)
                    self.__head = it.get_next()
                elif (it == self.__tail):
                    it.get_prev().set_next(None)
                    self.__tail = it.get_prev()
                else: 
                    it.get_next().set_prev(it.get_prev())
                    it.get_prev().set_next(it.get_next())
                    
                self.__length = self.__length - 1
                break
        
            else:
                it = it.get_next()
        
    
