import unittest
import server

class TestServer(unittest.TestCase):
    def test_set_password(self):
        self.assertEqual('a','a')

    def test_get_hash(self):
        self.assertEqual(server._get_hash('test'), '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08')

if __name__ == '__main__':
    unittest.main()
