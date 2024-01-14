from in_out import InOut
from exception.full_exception import FullException
import threading

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

    def __init__(self, maxsize : int = 0):
        self.__head = None
        self.__tail = None
        self.__length = 0
        self.__maxsize = maxsize
        self.__unfinished_tasks = 0

    def empty(self):
        return self.__length == 0

    def full(self):
        return self.__length == self.__maxsize
        
    def size(self):
        return self.__length

    def put(self, element, block=True, timeout=None):
        if block:
            if timeout != None:
                event = threading.Event()
                threading.Thread(target=_verify_free_slot(event)).start()
                if event.wait(timeout):
                    self._add(element)
                else:
                    raise FullException("There is no a free slot in the queue")
            else:
                event = threading.Event()
                threading.Thread(target=self._verify_free_slot(event)).start()
                event.wait()
                self._add(element)
        else:
            if self.__length == self.__size:
                raise FullException("There is no a free slot in the queue")
            self._add(element)


    def _add(self, element):
        if self.__length == 0:
            node = self.Node(element)
            self.__head = node
            self.__tail = node
        else:
            self.__tail.__next = node
            self.__tail = node
            
        self.__length += 1
        self.__unfinished_tasks += 1

    def _verify_free_slot(self, event):
        print("se")
    

    def put_nowait(self, element):
        print("code goes here")
        
    def get(self, block=True, timeout=None):
        print("code goes here")

    def get_nowait(self):
        print("code goes here")

    def join(self):
        print("code goes here")

    def task_done(self):
        print("code goes here")

    def __str__(self):
        print("code goes here")
