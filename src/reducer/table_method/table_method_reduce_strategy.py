import itertools

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.reducer.reduce_normal_logical_formula_strategy import ReduceNormalLogicalFormulaStrategy
from src.reducer.table_method.karnaugh_map import KarnaughMap


class TableMethodReduceStrategy(ReduceNormalLogicalFormulaStrategy):
    def reduce(self, formula: NormalLogicalFormula):
        kmap = KarnaughMap()
        kmap.build(formula)
        edges = kmap.find_max_edges()
        print(kmap)
        print("MAX EDGES")
        print(*edges, sep="\n" + '**'*kmap.column_count + "\n")
        print(*(x.row_vars + x.column_vars for x in edges))
        reduce_formula = NormalLogicalFormula()
        for edge in edges:
            reduce_formula.add(edge.get_implicant())
        return reduce_formula

