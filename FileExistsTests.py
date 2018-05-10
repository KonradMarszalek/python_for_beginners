import unittest

from FileExists_function import exists


class TestFileExists(unittest.TestCase):
    def test_directory_not_exists(self):
        self.assertEqual(exists(file_name='bla', file_directory='bla'), False)

    def test_file_not_exists(self):
        directory = "/Users/kmarszalek/Downloads/"
        self.assertEqual(exists(file_name='bla', file_directory=directory), False)

    def test_file_exists(self):
        directory = "/Users/kmarszalek/Downloads/"
        filename = "Charter.pdf"
        self.assertEqual(exists(file_name=filename, file_directory=directory), True)
