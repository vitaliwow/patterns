"""Context protocol refers to objects which are managing resources through 'with' keyword

Methods __enter__, __exit__ must be defined for the object to be used
as a context manager.
Context manager completes resource purging and preparing, for instance,
 for opening/closing files, database connections.
"""
from types import TracebackType
from typing import ContextManager, TypeVar, Optional, TextIO, Type

T = TypeVar("T")  # For return type from __enter__


class FileManager(ContextManager[str]):
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file: Optional[TextIO] = None

    def __enter__(self) -> T:
        """The method calls on entering  in context ('with')

        Returns resource (f.ex. opened file) to use it inside 'with' block
        """
        print(f"Opening file {self.filename} in mode {self.mode}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> bool:
        """Called on exit from the context no matter is exception raised or not

        exc_type - exception type if it was raised
        exc_value - exception instance
        traceback - traceback of the exception

        returns True, the exception is suppressed, otherwise it is rethrown.
        """

        if self.file:
            print(f"Closing file {self.filename}")
            self.file.close()
        return False

    def write(self, text: str) -> None:
        print("Write text ", text)


if __name__ == "__main__":
    with FileManager("../example.txt", "w") as file:
        file.write("Hello, Context Manager!")
