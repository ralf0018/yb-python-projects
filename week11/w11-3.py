import unittest

class TestStringMethods(unittest.TestCase):
    
    # check if .upper() work correctly
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    # check if isupper() work correctly
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
    # check if .split() work correctly    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    # check if .isdigit() work correctly
    def test_isdigit(self):
        self.assertTrue('123'.isdigit())
    
    # show the output if one test fails
    def test_isdigit(self):
        self.assertTrue('123a'.isdigit())     
          
if __name__ == '__main__':
    unittest.main()