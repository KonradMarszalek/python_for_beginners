import unittest

from sayWhat import say_what


class TestSayWhat(unittest.TestCase):
    def test_word(self):
        self.assertEqual(say_what('bla'), 'bla, what?')

    def test_blank(self):
        self.assertEqual(say_what(''), 'WHAT???')

    def test_what(self):
        self.assertEqual(say_what('what'), "WHAT WHAT WHAT???")
