import unittest

from translator import englishToFrench, FrenchToEnglish


class Testtranslation(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("hello"), "bonjour")  # test when hello is given as input the output is bonjour.
        self.assertNotEqual(englishToFrench("Hello"), "bonjour")
    def test2(self):
        self.assertEqual(FrenchToEnglish("bonjour"), "hello") # test when bonjour is given as input the output is hello.
        self.assertNotEqual(FrenchToEnglish("onjour"), "hello")

if __name__ == '__Main__':
    unittest.main()