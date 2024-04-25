from __future__ import annotations


class KarnaughMapCeil:
    def __init__(self, value: bool = False):
        self.value = value

    def set(self, item: bool):
        self.value = item

    def __bool__(self) -> bool:
        return self.value

    def __str__(self):
        if self:
            return '1'
        else:
            return '0'
