from abc import ABC, abstractmethod
from src.normal_logical_formula import NormalLogicalFormula


class ReduceNormalLogicalFormulaStrategy(ABC):
    @abstractmethod
    def reduce(self, formula: NormalLogicalFormula): pass
