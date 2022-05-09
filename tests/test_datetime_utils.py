import pytest
from pytest import raises
from datetime import datetime, date, time
from rocore.exceptions import EmptyArgumentException
from rocore.typesutils import dateutils


def test_parse_with_rx_raises_for_empty_value():
    with raises(EmptyArgumentException):
        dateutils.parse_time('')


@pytest.mark.parametrize('value,expected_result', [
    ('2008-09-03', datetime(2008, 9, 3)),
    ('2018-09-03', datetime(2018, 9, 3)),
    ('2008-09-03 20:56:35.450686', datetime(2008, 9, 3, 20, 56, 35, 450686)),
    ('2008-09-03T20:56:35.450686', datetime(2008, 9, 3, 20, 56, 35, 450686)),
    ('2008-09-03T20:56:35.450686Z', datetime(2008, 9, 3, 20, 56, 35, 450686)),
])
def test_parse_datetime(value, expected_result):
    parsed = dateutils.parse_datetime(value)
    assert expected_result == parsed


@pytest.mark.parametrize('value,expected_result', [
    ('2008-09-03', date(2008, 9, 3)),
    ('2018-09-03', date(2018, 9, 3)),
    ('2018/09/03', date(2018, 9, 3)),
])
def test_parse_datetime(value, expected_result):
    parsed = dateutils.parse_date(value)
    assert expected_result == parsed


@pytest.mark.parametrize('value,expected_result', [
    ('10:20:15', time(10, 20, 15)),
    ('03:00:00', time(3, 0, 0)),
    ('23:15:59', time(23, 15, 59)),
])
def test_parse_datetime(value, expected_result):
    parsed = dateutils.parse_time(value)
    assert expected_result == parsed
