import unittest

from src.formula.conjuent import Conjuent


class TestConjuent(unittest.TestCase):

    def test_init(self):
        c = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        self.assertEqual(c.names_of_arguments, {'a', 'b', 'c'})
        self.assertEqual(c.modalities, {'a': True, 'b': False, 'c': True})
        self.assertEqual(c.arguments, {('a', True), ('b', False), ('c', True)})

    def test_add(self):
        c = Conjuent()
        c.add('a', True)
        self.assertEqual(c.names_of_arguments, {'a'})
        self.assertEqual(c.modalities, {'a': True})
        self.assertEqual(c.arguments, {('a', True)})

    def test_remove(self):
        c = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        c.remove(('b', False))
        self.assertEqual(c.names_of_arguments, {'a', 'c'})
        self.assertEqual(c.modalities, {'a': True, 'c': True})
        self.assertEqual(c.arguments, {('a', True), ('c', True)})

    def test_call(self):
        c = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        self.assertTrue(c(a=True, b=False, c=True))
        self.assertFalse(c(a=True, b=True, c=True))

    def test_eq(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('b', False), ('a', True)])
        c3 = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)

    def test_ne(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('b', False), ('a', True)])
        c3 = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        self.assertFalse(c1 != c2)
        self.assertTrue(c1 != c3)

    def test_len(self):
        c = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        self.assertEqual(len(c), 3)

    def test_contains(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('b', False), ('a', True)])
        c3 = Conjuent(args=[('a', True), ('b', False), ('c', True)])
        self.assertTrue('a' in c1)
        self.assertTrue('b' in c1)
        self.assertFalse('c' in c1)
        self.assertTrue(c2 in c1)
        self.assertFalse(c3 in c1)


if __name__ == '__main__':
    unittest.main()