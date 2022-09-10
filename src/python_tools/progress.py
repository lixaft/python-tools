"""Progress bar for terminal."""
import sys


class ProgressBar:
    """Progess bar object."""


    def __init__(self, minimum: int = 0, maximum: int = 100, step: int = 1, length: int = 50) -> None:
        self._length = length
        self._maximum = maximum
        self._minimum = minimum
        self._step = step

        self._current = 0

    def next(self):
        """Add a step to the progress bar."""
        self._current += self._step
        if not (self._minimum < self._current < self._maximum):
            raise RuntimeError("Somethinf wrong with the current value.")

        length = int(self._length * self._current // self._length)
        bar = "█" * self._current + "-" * (self._length - length)
        msg = f"Progress: |{bar}| ..."

        sys.stdout.write(msg + "\r")

    def print(self):
        """Print the progress bar."""
        bar = "█" * self._current + "-" * (self._length - self._current)
        print(f"|{bar }|", end="\r")




