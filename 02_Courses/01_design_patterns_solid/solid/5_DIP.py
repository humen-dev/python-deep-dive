"""
DIP (Dependency Inversion Principle)
    * High-level modules should not depend on low-level modules;
      use abstractions instead.

Idea: high-level classes in your code should not depend directly on
      low-level classes. Instead, they should depend on abstractions.
      You want to depend on interfaces, not concrete implementations,
      because that allows you to swap one for another.
"""

from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high-level module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


parent = Person("John")
child = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
