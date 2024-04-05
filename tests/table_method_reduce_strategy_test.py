import unittest

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.reducer.table_method.table_method_reduce_strategy import TableMethodReduceStrategy
from src.formula.conjuent import Conjuent


class TestTableMethodReduceStrategy(unittest.TestCase):
    def test_reduce_multiple_variables(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
            Conjuent(args=[('a', False), ('b', False), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', False)]),
        ])
        strategy = TableMethodReduceStrategy()
        reduced_formula = strategy.reduce(formula)
        self.assertEqual(len(reduced_formula._conjuents), 2)


if __name__ == '__main__':
    unittest.main()
