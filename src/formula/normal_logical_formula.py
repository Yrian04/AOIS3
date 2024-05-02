from typing import Iterable

from src.formula.conjuent import Conjuent


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
            if subformula1.names_of_arguments != self.arguments:
                return False
        return True

    def add(self, conjuent: Conjuent):
        self._conjuents.add(conjuent)

    def remove(self, value: Conjuent):
        if value not in self._conjuents:
            raise ValueError(f"No subformula {value} in the formula {self}")
        self._conjuents.remove(value)

    @property
    def arguments(self):
        args = set()
        for conjuent in self._conjuents:
            for arg, _ in conjuent:
                args.add(arg)
        return args

    def print(self, out_symbol: str, in_symbol: str):
        return out_symbol.join(f"({x.print(in_symbol)})" for x in self._conjuents)

    def __call__(self, **kwargs) -> bool:
        for arg in self.arguments:
            if arg not in kwargs:
                raise ValueError(f"No argument {arg}")
        result = False
        for conjuent in self:
            result |= conjuent(**kwargs)
        return result

    def __len__(self):
        return len(self._conjuents)

    def __iter__(self):
        return iter(self._conjuents)

    def __copy__(self):
        return NormalLogicalFormula(conjuents=self._conjuents)

    def __str__(self):
        return self.join_str.join(f"({x})" for x in self._conjuents)
