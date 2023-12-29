import unittest
import list
# main_script.py
import sys
import random

sys.path.append('../src')

from my_list import *


class TestList(unittest.TestCase):

    correct_list = ["1", "2", "3", "4", "5"]
    
    def test_add_at(self):
        test_list = List()
        try: 
            test_list.add_at("1", 0)
        except ValueError as ve:
            self.assertFalse(test_list.getLength() == 1)
            pass
        
        #Add one single element:
        
        test_list.add_at(Element("1"), 0)
        self.assertTrue(test_list.getLength() == 1)
        element = test_list.get_element_at(0)
        self.assertTrue(element == "1")

        #Add several elements at the beginning of the list:
        
        test_list.add_at(Element("2"), 0)
        test_list.add_at(Element("3"), 0)
        test_list.add_at(Element("4"), 0)
        test_list.add_at(Element("5"), 0)

        element = test_list.get_element_at(0)
        self.assertTrue(element == 5)
        element = test_list.get_element_at(1)
        self.assertTrue(element == 4)
        
        self.assertTrue(test_list.getLength() == 5)

        #Add several elements at the final of the list:

        test_list.add_at(Element("10"), test_list.getLength())
        self.assertTrue(test_list.get_element_at(test_list.getLength) == "10")
        
        test_list.add_at(Element("11"), test_list.getLength())
        self.assertTrue(test_list.get_element_at(test_list.getLength) == "11")
        
        test_list.add_at(Element("12"), test_list.getLength())
        self.assertTrue(test_list.get_element_at(test_list.getLength) == "12")
        
        test_list.add_at(Element("13"), test_list.getLength())
        self.assertTrue(test_list.get_element_at(test_list.getLength) == "13")
        
         #Add several elements randomly in the list :

        random_index = random.randint(0, test_list_getLength())

        test_list.add_at(Element("6"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "6")

        random_index = random.randint(0, test_list_getLength())
        
        test_list.add_at(Element("7"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "7")

        random_index = random.randint(0, test_list_getLength())
        
        test_list.add_at(Element("8"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "8")

        random_index = random.randint(0, test_list_getLength())
        
        test_list.add_at(Element("9"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "9")

        self.assertTrue(test_list.getLength() == 13)
        
        
         
if __name__ == '__main__':
    unittest.main()
