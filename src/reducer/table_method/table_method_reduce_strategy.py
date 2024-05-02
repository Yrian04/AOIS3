import itertools

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.reducer.reduce_normal_logical_formula_strategy import ReduceNormalLogicalFormulaStrategy
from src.reducer.table_method.karnauhg_map.karnaugh_map import KarnaughMap


class TableMethodReduceStrategy(ReduceNormalLogicalFormulaStrategy):
    def reduce(self, formula: NormalLogicalFormula):
        karnaugh_map = KarnaughMap()
        karnaugh_map.build(formula)
        return self.get_formula_from_karnaugh_map(karnaugh_map)

    @staticmethod
    def get_formula_from_karnaugh_map(karnaugh_map: KarnaughMap):
        edges = karnaugh_map.find_max_edges()
        reduced_formula = NormalLogicalFormula()
        for edge in edges:
            reduced_formula.add(edge.get_implicant())
        return reduced_formula


