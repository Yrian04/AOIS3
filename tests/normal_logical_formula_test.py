import unittest

from src.formula.conjuent import Conjuent
from src.formula.normal_logical_formula import NormalLogicalFormula


class TestNormalLogicalFormula(unittest.TestCase):

    def test_init(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('b', False), ('a', True)])
        formula = NormalLogicalFormula(conjuents=[c1, c2])
        self.assertEqual(formula.is_full, True)
        self.assertEqual(formula.arguments, {'a', 'b'})

    def test_add(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('b', False), ('a', True)])
        formula = NormalLogicalFormula(conjuents=[c1, c2])
        c3 = Conjuent(args=[('a', True), ('c', True)])
        formula.add(c3)
        self.assertEqual(formula.is_full, False)
        self.assertEqual(formula.arguments, {'a', 'b', 'c'})

    def test_remove(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('a', False), ('b', True)])
        formula = NormalLogicalFormula(conjuents=[c1, c2])
        formula.remove(c1)
        self.assertEqual(formula.is_full, True)
        self.assertEqual(formula.arguments, {'a', 'b'})

    def test_call(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('a', False), ('b', True)])
        formula = NormalLogicalFormula(conjuents=[c1, c2])
        self.assertTrue(formula(a=True, b=False))
        self.assertTrue(formula(a=False, b=True))

    def test_len(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('a', False), ('b', True)])
        formula = NormalLogicalFormula(conjuents=[c1, c2])
        self.assertEqual(len(formula), 2)

    def test_copy(self):
        c1 = Conjuent(args=[('a', True), ('b', False)])
        c2 = Conjuent(args=[('b', False), ('a', True)])
        formula = NormalLogicalFormula(conjuents=[c1, c2])
        formula_copy = formula.__copy__()
        self.assertEqual(formula_copy.is_full, True)
        self.assertEqual(formula_copy.arguments, {'a', 'b'})


if __name__ == '__main__':
    unittest.main()
