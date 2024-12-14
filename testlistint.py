import unittest
from listint import ListInteger

class TestListInteger(unittest.TestCase):

    def test_create_empty(self):
        s = ListInteger()
        self.assertEqual(len(s), 0)

    def test_create_with_data(self):
        s = ListInteger([1, 2, 3])
        self.assertEqual(s, [1, 2, 3])

    def test_setitem_int(self):
        s = ListInteger([1, 2, 3])
        s[1] = 10
        self.assertEqual(s, [1, 10, 3])

    def test_setitem_error(self):
        s = ListInteger([1, 2, 3])
        with self.assertRaises(TypeError):
            s[1] = 10.5

    def test_append_int(self):
        s = ListInteger([1, 2, 3])
        s.append(4)
        self.assertEqual(s, [1, 2, 3, 4])

    def test_append_error(self):
        s = ListInteger([1, 2, 3])
        with self.assertRaises(TypeError):
            s.append(4.5)

    def test_mixed_init_error(self):
        with self.assertRaises(TypeError):
            ListInteger([1, 2, 'a'])

if __name__ == '__main__':
    unittest.main()