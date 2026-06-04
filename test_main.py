import os

from main import validate_time
from storage import save_alarms, load_alarms


TEST_FILE = "alarms.json"


def setup_function():
    """
    Reset alarms.json before every test.
    """

    save_alarms([])


def test_valid_time():
    """
    Valid HH:MM should return True.
    """

    assert validate_time("09:30") is True


def test_invalid_hour():
    """
    Invalid hour should return False.
    """

    assert validate_time("25:30") is False


def test_invalid_minute():
    """
    Invalid minute should return False.
    """

    assert validate_time("10:99") is False


def test_invalid_format():
    """
    Invalid format should return False.
    """

    assert validate_time("abcd") is False


def test_save_and_load_alarms():
    """
    Alarms should persist correctly.
    """

    alarms = [
        {
            "id": 1,
            "time": "08:30",
            "message": "Workout"
        }
    ]

    save_alarms(alarms)

    loaded_alarms = load_alarms()

    assert loaded_alarms == alarms


def test_empty_alarm_list():
    """
    Empty alarm list should load correctly.
    """

    save_alarms([])

    alarms = load_alarms()

    assert alarms == []


def test_multiple_alarms():
    """
    Multiple alarms should persist correctly.
    """

    alarms = [
        {
            "id": 1,
            "time": "08:30",
            "message": "Workout"
        },
        {
            "id": 2,
            "time": "09:00",
            "message": "Meeting"
        }
    ]

    save_alarms(alarms)

    loaded_alarms = load_alarms()

    assert len(loaded_alarms) == 2