import unittest

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent
from src.reducer.calculated_method.calculated_method_reduce_strategy import CalculatedMethodReduceStrategy


class TestCalculatedMethodReduceStrategy(unittest.TestCase):

    def test_reduce(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('c', True)]),
            Conjuent(args=[('a', True), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
        ])
        strategy = CalculatedMethodReduceStrategy()
        reduced = strategy.reduce(formula)
        self.assertEqual(reduced.is_full, False)
        self.assertEqual(reduced.arguments, {'a', 'b', 'c'})

    def test_remove_waste_implicants(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('c', True)]),
            Conjuent(args=[('a', True), ('c', False)]),
        ])
        CalculatedMethodReduceStrategy._remove_waste_implicants(formula)
        self.assertEqual(len(formula), 2)

    def test_combine_conjuents(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('a', False)]),
            Conjuent(args=[('a', True), ('c', False)]),
        ])
        strategy = CalculatedMethodReduceStrategy()
        reduced_formula = strategy._combine_conjuents(formula)
        self.assertEqual(len(reduced_formula), 2)


if __name__ == '__main__':
    unittest.main()
