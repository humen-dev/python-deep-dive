"""
ISP (Interface Segregation Principle)
    * Don't put too much into an interface; split it into separate interfaces
    * "You Ain't Gonna Need It" (YAGNI)
    * Split large interfaces into smaller ones

Idea: avoid adding too many members (e.g. methods) to a single interface.

It may seem like a good idea to implement one large interface and let
clients implement it however they like — but it forces implementors to
stub out methods they don't need.
"""

from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass  # noop

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError("Printer cannot scan!")


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultifunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
