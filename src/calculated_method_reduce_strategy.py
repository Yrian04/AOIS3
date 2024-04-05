from copy import copy

from src.normal_logical_formula import NormalLogicalFormula
from src.reduce_normal_logical_formula_strategy import ReduceNormalLogicalFormulaStrategy
from src.conjuent import Conjuent


class CalculatedMethodReduceStrategy(ReduceNormalLogicalFormulaStrategy):
    def reduce(self, formula: NormalLogicalFormula):
        reduced = copy(formula)
        for i in range(1, max(map(lambda x: len(x.arguments), formula))):
            reduced = self.__reduce(reduced)
        self._remove_waste_implicants(reduced)
        return reduced

    def __reduce(self, formula: NormalLogicalFormula):
        reduced_formula = self._combine_conjuents(formula)

        return reduced_formula

    @classmethod
    def _remove_waste_implicants(cls, formula):
        args = list(formula.arguments)
        args.sort()
        for implicant in copy(formula):
            formula_without_implicant = copy(formula)
            formula_without_implicant.remove(implicant)

            bits = [False] * len(args)
            flag = True
            while flag:
                flag = not all(bits)
                kwargs = dict(zip(args, bits))
                if formula_without_implicant(**kwargs) != formula(**kwargs):
                    break

                cls._inc(bits)
            else:
                formula.remove(implicant)
                print(f"({implicant}) is waste")

    @staticmethod
    def _inc(bits):
        for i in range(len(bits) - 1, -1, -1):
            bits[i] = not bits[i]
            if bits[i]:
                break

    @classmethod
    def _combine_conjuents(cls, formula: NormalLogicalFormula) -> NormalLogicalFormula:
        reduced_formula = NormalLogicalFormula()
        unprocessed_subformulas = set(formula)
        used = set()
        for subformula1 in formula:
            unprocessed_subformulas.remove(subformula1)
            for subformula2 in unprocessed_subformulas:
                if cls.__are_subformulas_reducible(subformula1, subformula2):
                    reduced_subformula = cls.__reduce_subformulas(subformula1, subformula2)
                    reduced_formula.add(reduced_subformula)
                    print(f"({subformula1}) + ({subformula2}) -> ({reduced_subformula})")
                    used.add(subformula1)
                    used.add(subformula2)
            if subformula1 not in used:
                reduced_formula.add(subformula1)
        return reduced_formula

    @staticmethod
    def __are_subformulas_reducible(subformula1: Conjuent, subformula2: Conjuent):
        if len(subformula1) != len(subformula2):
            return False
        symmetric_difference = subformula1.arguments.symmetric_difference(subformula2.arguments)
        if len(symmetric_difference) != 2:
            return False
        for arg, mod in symmetric_difference:
            if (arg, not mod) not in symmetric_difference:
                return False
        return True

    @staticmethod
    def __reduce_subformulas(subformula1: Conjuent, subformula2: Conjuent):
        reduced = Conjuent()
        for arg in subformula1:
            if arg in subformula2:
                reduced.add(*arg)
        return reduced
