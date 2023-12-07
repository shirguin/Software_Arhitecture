import sys


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")