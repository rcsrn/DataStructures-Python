import unittest
import sys
import time
import signal
import threading

sys.path.append('../src')

from my_queue import Queue

sys.path.append('../src/exception')

from full_exception import FullException

class TestQueue(unittest.TestCase):

    def test_init(self):
        test_queue = Queue()
        self.assertTrue(test_queue.size() == 0)

        test_queue = Queue(1)
        self.assertFalse(test_queue.full())
        self.assertTrue(test_queue.empty())
        
    def test_put(self):
        test_queue = Queue(5)
        for i in range(5):
            test_queue.put(i)
        self.assertTrue(test_queue.full())

        with assertRaises(FullException):
            test_queue.put(1, False)

        test_queue = Queue(1)
        test_queue.put(1)
        with assertRaises(TimeoutError):
            signal.alarm(5)
            test_queue.put(1, True)
      
        test_queue = Queue(5)

        for i in range(5):
            test_queue.put(i)
            
        with assertRaises(FullException):
            with assertRaisesTimeout(3):
                test_queue.put(1, True, 3)

    def test_get(self):
        test_queue = Queue(5)
        for i in range(5):
            test_queue.put_nowait(i)
        i = 0
        while not test_queue.empty():
            self.assertEqual(i, test_queue.get())
            i = i + 1


    test_queue = Queue(5)

    def join(self):
        test_queue = TestQueue.test_queue
        
        try:
            signal.alarm(5)
            threading.Thread(target=auxiliar, daemon=True).start()
            for i in range(5):
                test_queue.put_nowait(i)
            
            test_queue.join()
        except (TimeoutError):
            self.fail("Timeout error")

        self.assertTrue(test_queue.empty())

    def auxiliar():
        test_queue = TestQueue.test_queue
        while not test_queue.empty():
            test_queue.get()
            test_queue.task_done()
    
        
            
if __name__ == "__main__":
    unittest.main()

