import unittest
import solution

class Test(unittest.TestCase):
    def test_should_say_hello(self):
        self.assertEqual(solution.say_hello('Seda'), "Hello, Seda!")

    def test_should_handle_blank_input(self):
        self.assertEqual(solution.say_hello(''), 'Hello there!')

if  __name__ == '__main__':
    unittest.main()


    

