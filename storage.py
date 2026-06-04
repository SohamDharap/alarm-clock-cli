import json
import os

ALARM_FILE = "alarms.json"


def load_alarms():
    """
    Load alarms from JSON file.
    Returns empty list if file doesn't exist.
    """

    if not os.path.exists(ALARM_FILE):
        return []

    try:
        with open(ALARM_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: alarms.json contains invalid JSON.")
        return []


def save_alarms(alarms):
    """
    Save alarms to JSON file.
    """

    with open(ALARM_FILE, "w") as file:
        json.dump(alarms, file, indent=4)