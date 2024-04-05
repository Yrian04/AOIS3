import unittest

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent
from src.reducer.calculated_table_method.calculated_table_method_reduce_strategy import  CalculatedTableMethodReduceStrategy


class TestCalculatedTableMethodReduceStrategy(unittest.TestCase):

    def test_reduce(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('c', True)]),
            Conjuent(args=[('a', True), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
        ])
        strategy = CalculatedTableMethodReduceStrategy()
        reduced = strategy.reduce(formula)
        self.assertEqual(reduced.is_full, False)
        self.assertEqual(reduced.arguments, {'a', 'b', 'c'})

    def test_make_table(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('c', True)]),
            Conjuent(args=[('a', True), ('c', False)]),
        ])
        reduce_formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('c', True)]),
        ])
        strategy = CalculatedTableMethodReduceStrategy()
        table = strategy._CalculatedTableMethodReduceStrategy__make_table(formula, reduce_formula)
        self.assertEqual(len(table), 2)

    def test_process_ceil(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
            Conjuent(args=[('a', False), ('b', False), ('c', False)]),
        ])
        reduce_formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False)]),
            Conjuent(args=[('b', False), ('c', True)]),
        ])
        strategy = CalculatedTableMethodReduceStrategy()
        table = strategy._CalculatedTableMethodReduceStrategy__make_table(formula, reduce_formula)
        result = strategy._CalculatedTableMethodReduceStrategy__process_ceil(1, Conjuent(args=[('a', True), ('b', False)]), reduce_formula, table)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
