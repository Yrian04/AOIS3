from __future__ import annotations

import itertools

from src.formula.normal_logical_formula import NormalLogicalFormula
from src.formula.conjuent import Conjuent
from src.reducer.table_method.karnauhg_map.karnaugh_map_ceil import KarnaughMapCeil
import src.utils as utils


class KarnaughMap:
    def __init__(self, parent: KarnaughMap | None = None):
        self._parent = parent
        self._map: list[list[KarnaughMapCeil]] = []
        self._row_vars: list[str] = []
        self._column_vars: list[str] = []
        self._processed_edge: list[KarnaughMap] = []

    def build(self, formula: NormalLogicalFormula) -> None:
        if not formula.is_full:
            raise ValueError(f"Formula is not full: {formula}")

        # distribute arguments for rows and columns
        args = list(formula.arguments)
        args.sort()
        for i, arg in enumerate(args):
            if i >= len(args)//2:
                self._row_vars.append(arg)
            else:
                self._column_vars.append(arg)

        # fill the map
        n = len(args)
        rows = 2**len(self._column_vars)
        columns = 2**len(self._row_vars)
        self._map = [[KarnaughMapCeil() for _ in range(columns)] for _ in range(rows)]
        for subformula in formula:
            bits = tuple(map(lambda a: subformula.modalities[a], args))
            x = utils.from_gray(self.__to_integer(bits[:n // 2]))
            y = utils.from_gray(self.__to_integer(bits[n // 2:]))
            self[x][y].set(True)

    @property
    def row_vars(self) -> list[str]:
        return self._row_vars.copy()

    @property
    def column_vars(self) -> list[str]:
        return self._column_vars.copy()

    @property
    def vars(self):
        return self.column_vars + self.row_vars

    @property
    def row_count(self) -> int:
        return len(self._map)

    @property
    def column_count(self) -> int:
        if not self:
            return 0
        return len(self[0])

    def is_full_of_true(self) -> bool:
        return all([all(x) for x in self])

    def is_full_of_false(self) -> bool:
        return not any([any(x) for x in self])

    def append(self, item: list[KarnaughMapCeil]) -> None:
        self._map.append(item)

    @staticmethod
    def _remove_included_edges(edges: list[KarnaughMap]):
        return [x for x in edges if not any(y != x and x in y for y in sorted(edges, key=lambda x: x.__weight()))]

    @staticmethod
    def _remove_useless_edges(edges: list[KarnaughMap]):
        return [x for x in edges if any(any(all(y is x or ceil not in y for y in edges) for ceil in row) for row in x)]

    def find_max_edges(self):
        if self.row_count == 1 and self.column_count == 1:
            if self._map[0][0]:
                return [self]
            else:
                return []
        edges = self.__find_true_edges()
        intersected_edges = self._remove_included_edges(edges)
        # max_edges = []
        # processed_edges = []
        # for x in intersected_edges:
        #     for row in x:
        #         for ceil in row:
        #             for y in intersected_edges:
        #                 if y in processed_edges and y not in max_edges:
        #                     continue
        #                 if ceil in y:
        #                     break
        #             else:
        #                 max_edges.append(x)
        #                 break
        # return max_edges
        return self._remove_useless_edges(intersected_edges)

    def get_implicant(self) -> Conjuent:
        if self._parent is None:
            raise AttributeError("This is root")
        implicant = Conjuent()
        args = [x for x in self._parent.vars if x not in self.vars]
        for arg in args:
            index = len(self._parent.vars) - 1 - self._parent.vars.index(arg)
            modality = bool(self._parent.get_grey_index(self._map[0][0]) & (1 << index))
            implicant.add(arg, modality)
        return implicant

    def get_grey_index(self, ceil: KarnaughMapCeil) -> int:
        if ceil not in self:
            raise ValueError("Ceil not in map")
        for i, row in enumerate(self):
            if ceil in row:
                row_index = utils.to_gray(i)
                column_index = utils.to_gray(row.index(ceil))
                return (row_index << len(self.row_vars)) + column_index

    def __weight(self):
        weight = 0
        for row in self:
            for ceil in row:
                weight += 1 if ceil else 0

        return weight

    def __find_true_edges(self) -> list[KarnaughMap]:
        # print(self)
        # print('-'*self.column_count)
        if not self or self.is_full_of_false():
            return []
        if self.is_full_of_true():
            return [self]
        edges: list[KarnaughMap] = []
        for edge in self.__get_edges(self._parent if self._parent else self):
            if edge not in edge._parent._processed_edge:
                edge._parent._processed_edge.append(edge)
                edges += edge.__find_true_edges()
        return edges

    @classmethod
    def _create_empty_edge(cls, parent):
        return cls(parent)

    def __get_edges(self, parent: KarnaughMap | None) -> list[KarnaughMap]:
        edges: list[KarnaughMap] = []

        # y edges
        for (c, var), module in itertools.product(enumerate(self._column_vars), (False, True)):
            edge = self._create_empty_edge(parent)

            # add vars in map
            edge._row_vars = self._row_vars
            for column_var in self._column_vars:
                if column_var != var:
                    edge._column_vars.append(column_var)

            for i, row in enumerate(self):
                if bool(utils.to_gray(i) & (1 << (len(self._column_vars) - 1 - c))) == module:
                    edge.append(row)
            edges.append(edge)

        # x edges
        for (c, var), module in itertools.product(enumerate(self._row_vars), [False, True]):
            edge = self._create_empty_edge(parent)

            # add vars in map
            edge._column_vars = self._column_vars
            for row_var in self._row_vars:
                if row_var != var:
                    edge._row_vars.append(row_var)

            for row in self:
                edge_row = []
                for j, ceil in enumerate(row):
                    if bool(utils.to_gray(j) & (1 << (len(self._row_vars) - 1 - c))) == module:
                        edge_row.append(ceil)
                edge.append(edge_row)
            edges.append(edge)

        return edges

    @staticmethod
    def __to_integer(bits):
        result = 0
        for i in range(len(bits)):
            if bits[-i - 1]:
                result += pow(2, i)
        return result

    def __contains__(self, item):
        if isinstance(item, KarnaughMapCeil):
            return any([item in row for row in self])
        if isinstance(item, KarnaughMap):
            for row in item:
                for ceil in row:
                    if ceil not in self:
                        return False
            return True
        return item in self._map

    def __getitem__(self, item: int) -> list[KarnaughMapCeil]:
        if not self._map:
            raise AttributeError("Karnaugh map was empty")
        if item >= len(self._map):
            raise IndexError("Index out of range")
        return self._map[item]

    def __setitem__(self, key: int, value: KarnaughMapCeil):
        if 0 < key < 1 << len(self.vars):
            raise IndexError(f"Index {key} out of range")

        index = utils.from_gray(key)

        i = index & ((1 << self.column_count) - 1)
        j = index & (((1 << self.row_count) - 1) << self.column_count)

        self[i][j] = value

    def __bool__(self):
        return bool(self._map)

    def __iter__(self):
        return iter(self._map)

    def __eq__(self, other):
        if isinstance(other, KarnaughMap):
            return self in other and other in self
        return False

    def __copy__(self):
        result = KarnaughMap()
        result._map = self._map.copy()
        result._vars = self._vars.copy()
        return result

    def __len__(self):
        return len(self._map)

    def __str__(self):
        if self._parent:
            return '\n'.join([' '.join([str(x) if x in self else 'x' for x in row]) for row in self._parent])
        return '\n'.join([' '.join([str(x) for x in row]) for row in self])
