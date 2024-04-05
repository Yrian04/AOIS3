from abc import ABC, abstractmethod
from src.formula.normal_logical_formula import NormalLogicalFormula


class ReduceNormalLogicalFormulaStrategy(ABC):
    @abstractmethod
    def reduce(self, formula: NormalLogicalFormula): pass
