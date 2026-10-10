def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")

food = {"category": 'ice cream', "flavor": 'vanilla', "cost": 199}
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')
