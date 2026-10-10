"""
SRP (Single Responsibility Principle)
    * A class should have only one reason to change
    * Separation of concerns — different classes handle different,
      independent tasks and problems

Idea: if you have a class, that class should have its own primary
      responsibility. It should not take on other responsibilities.

PS: Do not overload your objects with too many duties.

Anti-pattern: god object (all-powerful object) — cramming everything
              into a single class
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))


def main():
    j = Journal()
    j.add_entry("I cried today")
    j.add_entry("I ate a bug")
    print(f"Journal entries: \n{j}")

    file = b"C:/Users/Mike/PycharmProjects/designPatterns/temp/journal.txt"
    PersistenceManager.save_to_file(j, file)

    with open(file) as fh:
        print(fh.read())


if __name__ == "__main__":
    main()
