import uuid


def uuid_to_str(uuid_: uuid.UUID) -> str:
    return str(uuid_)


def str_to_uuid(uuid_: str) -> uuid.UUID:
    return uuid.UUID(uuid_)
