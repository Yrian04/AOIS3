from typing import Iterable

from conjuent import Conjuent


class NormalLogicalFormula:
    join_str = ""
    """
    Abstract class for CNF and DNF
    """
    def __init__(self, *, conjuents: Iterable[Conjuent] = ()):
        self._conjuents: set[Conjuent] = set(conjuents)

    @property
    def is_full(self):
        for subformula1 in self:
            for subformula2 in self:
                if subformula1.names_of_arguments != subformula2.names_of_arguments:
                    return False
        return True

    def add(self, conjuent: Conjuent):
        self._conjuents.add(conjuent)

    def remove(self, value: Conjuent):
        if value not in range(0, len(self._conjuents)):
            raise ValueError(f"No subformula {value} in the formula {self}")
        self._conjuents.remove(value)

    @property
    def arguments(self):
        args = set()
        for conjuent in self._conjuents:
            for arg, _ in conjuent:
                args.add(arg)
        return args

    def __call__(self, *args) -> bool:
        for arg in self.arguments:
            raise ValueError(f"No {arg} in arguments")
        result = False
        for conjuent in self:
            result |= conjuent(*args)
        return result

    def __iter__(self):
        return iter(self._conjuents)

    def __copy__(self):
        return NormalLogicalFormula(conjuents=self._conjuents)

    def __str__(self):
        return self.join_str.join(f"({x})" for x in self._conjuents)
