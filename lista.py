class Node():
    __slots__ = ("__prev", "__next", "__element")

    def set_element(self, element):
        self.__element = element


class List():
    __slots__ = ("__head", "__tail", "__length")

    def addAt(self, element, i):
        if not isinstance(element, Element) or i < 0 or i > self.__length:
            raise ValueError("It is not possible to add this element to the list.")
        node = Node()
        node.set_element(element)
        
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            if self.length == 1:
                if i == 0:
                    node.__next = __head
                    __head.__prev = node
                else:
                    node.__prev = __tail
                    __tail.__next = node
            else:
                change = getNodeAt(i)
                node.__prev = change.__prev
                change.__prev.__next = node
                node.__next = change
                change.__prev = node
            
    def getNodeAt(index):
        it = __head
        for i in range(__length):
            if i == index:
                return it
            it = __head.__next


