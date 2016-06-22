import arrow


def utc():
    return arrow.get()


def to_string(dt):
    return dt.isoformat()
