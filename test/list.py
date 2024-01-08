import unittest
import list
# main_script.py
import sys
import random

sys.path.append('../src')

from my_list import *


class TestList(unittest.TestCase):

    correct_list = ["1", "2", "3", "4", "5"]
    test_list = None 

    def test_add_at(self):
        TestList.test_list = List()
        test_list = TestList.test_list
        try: 
            test_list.add_at("1", 0)
        except ValueError as ve:
            self.assertFalse(test_list.get_length() == 1)
            pass

        #Add one single element:
        
        test_list.add_at(Element("1"), 0)
        self.assertTrue(test_list.get_length() == 1)
        element = test_list.get_element_at(0)
        self.assertTrue(element == "1")

        #Add several elements at the beginning of the list:
        
        test_list.add_at(Element("2"), 0)
        self.assertTrue(test_list.get_element_at(0) == "2")
        
        test_list.add_at(Element("3"), 0)
        self.assertTrue(test_list.get_element_at(0) == "3")
        
        test_list.add_at(Element("4"), 0)
        self.assertTrue(test_list.get_element_at(0) == "4")
        
        test_list.add_at(Element("5"), 0)

        element = test_list.get_element_at(0)

        self.assertTrue(element == "5")

        element = test_list.get_element_at(1)
        self.assertTrue(element == "4")
        
        self.assertTrue(test_list.get_length() == 5)

        #Add several elements at the final of the list:

        test_list.add_at(Element("10"), test_list.get_length())
        self.assertTrue(test_list.get_element_at(test_list.get_length() - 1) == "10")
        
        test_list.add_at(Element("11"), test_list.get_length())
        self.assertTrue(test_list.get_element_at(test_list.get_length() - 1) == "11")
        
        test_list.add_at(Element("12"), test_list.get_length())
        self.assertTrue(test_list.get_element_at(test_list.get_length() - 1) == "12")
        
        test_list.add_at(Element("13"), test_list.get_length())
        self.assertTrue(test_list.get_element_at(test_list.get_length() - 1) == "13")
        
         #Add several elements randomly in the list :

        random_index = random.randint(0, test_list.get_length())

        test_list.add_at(Element("6"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "6")

        random_index = random.randint(0, test_list.get_length())
        
        test_list.add_at(Element("7"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "7")

        random_index = random.randint(0, test_list.get_length())
        
        test_list.add_at(Element("8"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "8")

        random_index = random.randint(0, test_list.get_length())
        
        test_list.add_at(Element("9"), random_index)
        self.assertTrue(test_list.get_element_at(random_index) == "9")

        self.assertTrue(test_list.get_length() == 13)

    def test_str(self):
        TestList.test_list = List()
        test_list = TestList.test_list

        for i in range(5):
            value = i + 1
            test_list.add_at(Element(value.__str__()), test_list.get_length())
            
        self.assertTrue(test_list.__str__() == TestList.correct_list.__str__())

    def test_clean(self):
        TestList.test_list.clean()
        self.assertTrue(TestList.test_list.__str__() == "[]")
        self.assertTrue(TestList.test_list.get_length() == 0)

    def test_from_list(self):
        TestList.test_list = List.from_list(TestList.correct_list)
        self.assertTrue(TestList.test_list.__str__() == TestList.correct_list.__str__())
        
    def test_remove(self):
        test_list = TestList.test_list
        correct_list = TestList.correct_list.copy()

        last_value = test_list.get_length()
        
        test_list.removeByValue("5")
        correct_list.remove("5")
        
        self.assertTrue(test_list.__str__() == correct_list.__str__())
        
        self.assertTrue(test_list.get_length() == last_value - 1)

        last_value = test_list.get_length()
        
        test_list.removeByValue("1")
        correct_list.remove("1")

        self.assertTrue(test_list.__str__() == correct_list.__str__())
        
        self.assertTrue(test_list.get_length() == last_value - 1)

        last_value = test_list.get_length()
        
        test_list.removeByValue("3")
        correct_list.remove("3")

        self.assertTrue(test_list.__str__() == correct_list.__str__())
        
        self.assertTrue(test_list.get_length() == last_value - 1)
        
         
if __name__ == '__main__':
    unittest.main()
