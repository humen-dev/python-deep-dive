from dataclasses import InitVar, dataclass, field


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)


@dataclass
class HackerClubMember(ClubMember):
    all_handles: set = field(default_factory=set)
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__

        if self.handle == "":
            self.handle = self.name.split()[0]

        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)

        cls.all_handles.add(self.handle)


# Initialization Variables That Are Not Fields
class DatabaseType:
    def __init__(self):
        self._data = {}

    def lookup(self, key):
        return self._data[key]


@dataclass
class C:
    i: int = None
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup("j")


my_database = DatabaseType()
c = C(10, database=my_database)
