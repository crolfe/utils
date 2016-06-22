import arrow

from utils import dates


def test_utc_returns_arrow():
    date = dates.utc()
    assert isinstance(date, arrow.Arrow)


def test_assert_false():
    assert False
