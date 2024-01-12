from in_out import InOut

class Queue(InOut):

    class Node():
        def __init__(self, element):
            self.__element = element
            self.__next = None

        def set_element(self, element):
            self.element = element

        def get_element(self):
            return self.__element
        
        def set_next(self, next):
            self.__next = next
            
        def get_next(self):
            return self.__next

    def __init__(self, size : int = 0):
        self.__head = None
        self.__length = 0
        self.__size = size

    def empty(self):
        return self.__length == 0

    def full(self):
        return self.__length == self.__size
        
    def size(self):
        return self.__size

    def put(self, element):
        print("code goes here")

    def put_nowait(self, element):
        print("code goes here")
        
    def get(self):
        print("code goes here")

    def join(self):
        print("code goes here")

    def __str__(self):
        print("code goes here")
      
    def __iterator__(self):
        print("code goes here")
