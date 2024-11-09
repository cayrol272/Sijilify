import unittest
from sijilify import sijilify

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.sijil = sijilify()

    def test_readTemplate(self):
        
        lst = self.sijil.list_template()
        for i in lst:
            self.assertTrue(self.sijil.read_template(i))
    
    def test_loadConfig(self):
        self.assertTrue(self.sijil.load_config('seminar'))

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()