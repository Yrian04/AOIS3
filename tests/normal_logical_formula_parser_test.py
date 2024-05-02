import unittest

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent
from src.formula.normal_logical_formula_parser import NormalLogicalFormulaParser


class TestNormalLogicalFormulaParser(unittest.TestCase):

    def test_parse(self):
        parser = NormalLogicalFormulaParser(external_operation_symbol='|',
                                            internal_operation_symbol=',',
                                            negative_symbol='!')
        string = '(a,b)|(c,!d)|(e,f)'
        formula = parser.parse(string)
        self.assertEqual(formula.is_full, False)
        self.assertEqual(formula.arguments, {'a', 'b', 'c', 'd', 'e', 'f'})

    def test_parse_subformula(self):
        parser = NormalLogicalFormulaParser(external_operation_symbol='|',
                                            internal_operation_symbol=',',
                                            negative_symbol='!')
        subformula = parser._NormalLogicalFormulaParser__parse_subformula('(a,b)')
        self.assertEqual(subformula.names_of_arguments, {'a', 'b'})
        self.assertEqual(subformula.modalities, {'a': True, 'b': True})

        subformula = parser._NormalLogicalFormulaParser__parse_subformula('(!a,b)')
        self.assertEqual(subformula.names_of_arguments, {'a', 'b'})
        self.assertEqual(subformula.modalities, {'a': False, 'b': True})

if __name__ == '__main__':
    unittest.main()
