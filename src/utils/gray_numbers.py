def to_gray(integer: int) -> int:
    return integer ^ (integer >> 1)


def from_gray(gray: int) -> int:
    if gray == 0:
        return 0
    if gray == 1:
        return 1
    result = 0
    while gray:
        result ^= gray
        gray >>= 1
    return result
