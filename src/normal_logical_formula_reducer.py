from reduce_normal_logical_formula_strategy import ReduceNormalLogicalFormulaStrategy
from normal_logical_formula import NormalLogicalFormula


class NormalLogicalFormulaReducer:
    def __init__(self, reduce_strategy: ReduceNormalLogicalFormulaStrategy):
        self._reduce_strategy = reduce_strategy

    @property
    def reduce_strategy(self):
        return self._reduce_strategy

    @reduce_strategy.setter
    def reduce_strategy(self, value: ReduceNormalLogicalFormulaStrategy):
        self._reduce_strategy = value

    def reduce(self, formula: NormalLogicalFormula):
        return self._reduce_strategy.reduce(formula)
