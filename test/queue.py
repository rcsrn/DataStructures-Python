import unittest
import sys
import time
import signal
import threading

sys.path.append('../src')

from my_queue import Queue

from exception.full_exception import FullException

class TestQueue(unittest.TestCase):
    
    def test_init(self):
        test_queue = Queue()
        self.assertTrue(test_queue.size() == 0)

        test_queue = Queue(1)
        self.assertFalse(test_queue.full())
        self.assertTrue(test_queue.empty())
        
    def test_put(self):
        test_queue = Queue(1)
        test_queue.put(1)
        self.assertTrue(test_queue.full())
        
        timeout = 3
        starting_time = time.time()
        with self.assertRaises(FullException):
            test_queue.put(1, True, timeout)
        ending_time = time.time()
        total_time = ending_time - starting_time
        self.assertEqual(timeout, int(total_time))
            
        with self.assertRaises(FullException):
            test_queue.put(1, False)

        test_queue = Queue(20)
            
        for i in range(20):
            test_queue.put(i)
        self.assertTrue(test_queue.full())

        timeout = 5
        starting_time = time.time()
        with self.assertRaises(FullException):
            test_queue.put(20, True, timeout)
        ending_time = time.time()
        total_time = ending_time - starting_time
        self.assertEqual(timeout, int(total_time))    

        with self.assertRaises(FullException):
            test_queue.put(20, False)
            
    def test_get(self):
        test_queue = Queue(2)
        for i in range(2):
            test_queue.put_nowait(i)
        # self.assertTrue(test_queue.full())
        # for i in range(2):
        #     self.assertEqual(i, test_queue.get())
        # self.assertEqual(0, test_queue.size())

        # with self.assertRaises(Empty):
        #     test_queue.get()
        
    
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

