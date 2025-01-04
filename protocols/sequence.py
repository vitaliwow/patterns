"""The protocol describes behavior of the sequence

__getitem__ defines the way to get an element of the sequence by index or key
__len__ realizes the length of the sequence
"""

import typing


class MySequence:
    def __init__(self, data: list[typing.Any]) -> None:
        self.data = data

    def __getitem__(self, index: int) -> typing.Any:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)


if __name__ == "__main__":
    seq = MySequence([1, 2, 3])
    print(len(seq))  # 3
    print(seq[1])    # 2
