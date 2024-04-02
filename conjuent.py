class Conjuent:
    """
    Class for conjunctions in FCNF or disjunctions in FDNF
    """
    join_str = ", "

    def __init__(self, *, args=()):
        self._args = set(args)

    @property
    def names_of_arguments(self) -> set:
        return set(map(lambda x: x[0], self._args))

    @property
    def modalities(self) -> dict:
        return dict(self._args)

    @property
    def arguments(self) -> set:
        return self._args.copy()

    def add(self, argument: str, modality: bool) -> None:
        """
        :param argument: name of argument
        :param modality: if negative then false else true
        :raise ValueError
        """
        if not argument.isalpha():
            raise ValueError(f"{argument} is not valid name for argument")
        self._args.add((argument, modality))

    def remove(self, arg) -> None:
        """
        :param arg: argument for remove
        :raise: IndexError
            """
        if arg not in self._args:
            raise ValueError(f"No argument {arg} in the subformula {self}")
        self._args.remove(arg)

    def __eq__(self, other):
        return self._args == other._args

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return len(self._args)

    def __iter__(self):
        return iter(self._args)

    def __hash__(self):
        return hash(str(self))

    def __str__(self) -> str:
        return self.join_str.join([f"!{x[0]}" if not x[1] else x[0] for x in self._args])
