from pathlib import Path
import sys


class Aocutils:
    def __init__(self, filename) -> None:
        self.filename = filename

    def read_file_to_list(self):
        lines = []
        with open(self.filename) as f:
            for line in f:
                line.strip()
                lines.append(line)
        return lines
