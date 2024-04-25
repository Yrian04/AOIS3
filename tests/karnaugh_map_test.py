import unittest

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent
from src.reducer.table_method.karnauhg_map.karnaugh_map import KarnaughMap


class TestKarnaughMap(unittest.TestCase):
    def test_build_single_variable(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True)])
        ])
        karnaugh_map = KarnaughMap()
        karnaugh_map.build(formula)
        self.assertEqual(karnaugh_map.row_vars, ['a'])
        self.assertEqual(karnaugh_map.column_vars, [])
        self.assertEqual(karnaugh_map.row_count, 1)
        self.assertEqual(karnaugh_map.column_count, 2)

    def test_get_implicant_empty(self):
        karnaugh_map = KarnaughMap()
        self.assertRaises(AttributeError, karnaugh_map.get_implicant)

    def test_get_grey_index_zero(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
            Conjuent(args=[('a', False), ('b', False), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
        ])
        karnaugh_map = KarnaughMap()
        karnaugh_map.build(formula)
        index = karnaugh_map.get_grey_index(karnaugh_map[0][0])
        self.assertEqual(index, 0)

    def test_find_max_edges_empty(self):
        formula = NormalLogicalFormula(conjuents=[])
        karnaugh_map = KarnaughMap()
        karnaugh_map.build(formula)
        edges = karnaugh_map.find_max_edges()
        self.assertEqual(edges, [])

    def test_find_max_edges_multiple_variables(self):
        formula = NormalLogicalFormula(conjuents=[
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
            Conjuent(args=[('a', False), ('b', False), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', False)]),
            Conjuent(args=[('a', True), ('b', False), ('c', True)]),
        ])
        karnaugh_map = KarnaughMap()
        karnaugh_map.build(formula)
        edges = karnaugh_map.find_max_edges()
        self.assertEqual(len(edges), 2)

if __name__ == '__main__':
    unittest.main()
