from TerminalPrinter import TerminalPrinter
from FilePrinter import FilePrinter
from Logger import Logger


def main():
    logger = Logger()
    logger.log('Starting the program . . . . ', TerminalPrinter)
    logger.log('Starting the program . . . . ', FilePrinter)


main()

