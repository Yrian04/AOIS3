from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent


class NormalLogicalFormulaParser:
    def __init__(self, external_operation_symbol: str, internal_operation_symbol: str, negative_symbol: str):
        self._external_operation_symbol = external_operation_symbol
        self._internal_operation_symbol = internal_operation_symbol
        self._negative_symbol = negative_symbol

    def parse(self, string: str):
        full_formula = NormalLogicalFormula()
        for subformula in string.split(self._external_operation_symbol):
            full_formula.add(self.__parse_subformula(subformula))
        return full_formula

    def __parse_subformula(self, string: str) -> Conjuent:
        subformula = Conjuent()
        for arg in string[1:-1].split(self._internal_operation_symbol):
            if arg.startswith(self._negative_symbol):
                subformula.add(arg[1:], False)
            else:
                subformula.add(arg, True)
        return subformula
