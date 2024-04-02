from conjuent import Subformula


class NormalLogicalFormula:
    join_str = ""
    """
    Abstract class for CNF and DNF
    """
    def __init__(self, *, subformulas=()):
        self._subformulas = set(subformulas)

    @property
    def is_full(self):
        for subformula1 in self:
            for subformula2 in self:
                if subformula1.names_of_arguments != subformula2.names_of_arguments:
                    return False
        return True

    def add(self, subformula: Subformula):
        self._subformulas.add(subformula)

    def remove(self, value: Subformula):
        if value not in range(0, len(self._subformulas)):
            raise ValueError(f"No subformula {value} in the formula {self}")
        self._subformulas.remove(value)

    @property
    def arguments(self):
        args = set()
        for subformula in self._subformulas:
            for arg, _ in subformula:
                args.add(arg)
        return args

    def __iter__(self):
        return iter(self._subformulas)

    def __copy__(self):
        return NormalLogicalFormula(subformulas=self._subformulas)

    def __str__(self):
        return self.join_str.join(f"({x})" for x in self._subformulas)
