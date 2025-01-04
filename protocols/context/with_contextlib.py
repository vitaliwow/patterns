from contextlib import contextmanager
from typing import Generator, TextIO


@contextmanager
def managed_file(filename: str, mode: str) -> Generator[TextIO, None, None]:
    """Return Generator obj with context lib"""

    print(f"Opening file {filename} in mode {mode}")
    file_obj = open(filename, mode)
    try:
        yield file_obj
    finally:
        print(f"Closing file {filename}")
        file_obj.close()


if __name__ == "__main__":
    with managed_file("example.txt", "w") as file:
        file.write("Hello, Context Manager!")
