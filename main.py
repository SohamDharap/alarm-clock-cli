import argparse
import time

from datetime import datetime

from storage import load_alarms, save_alarms


def validate_time(time_str):
    """
    Validate HH:MM format.
    """

    try:
        datetime.strptime(time_str, "%H:%M")
        return True

    except ValueError:
        return False


def add_alarm(alarm_time, message):
    """
    Add a new alarm.
    """

    if not validate_time(alarm_time):
        print("Invalid time format. Use HH:MM")
        return

    alarms = load_alarms()

    next_id = 1

    if alarms:
        next_id = max(alarm["id"] for alarm in alarms) + 1

    alarm = {
        "id": next_id,
        "time": alarm_time,
        "message": message
    }

    alarms.append(alarm)

    save_alarms(alarms)

    print(f"Alarm created with ID {next_id}")


def list_alarms():
    """
    Display all alarms.
    """

    alarms = load_alarms()

    if not alarms:
        print("No alarms found.")
        return

    print("\nConfigured Alarms")
    print("-" * 50)

    for alarm in alarms:
        print(
            f'ID: {alarm["id"]} | '
            f'Time: {alarm["time"]} | '
            f'Message: {alarm["message"]}'
        )


def delete_alarm(alarm_id):
    """
    Delete an alarm by ID.
    """

    alarms = load_alarms()

    updated_alarms = [
        alarm
        for alarm in alarms
        if alarm["id"] != alarm_id
    ]

    if len(updated_alarms) == len(alarms):
        print("Alarm not found.")
        return

    save_alarms(updated_alarms)

    print(f"Alarm {alarm_id} deleted.")


def run_alarm_monitor():
    """
    Monitor alarms continuously.
    Trigger and remove alarms when executed.
    """

    print("Alarm monitor started...")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:

            alarms = load_alarms()

            current_time = datetime.now().strftime("%H:%M")

            alarms_to_keep = []

            for alarm in alarms:

                if alarm["time"] == current_time:

                    print("\n" + "=" * 50)
                    print("ALARM!")
                    print(f'Time: {alarm["time"]}')
                    print(f'Message: {alarm["message"]}')
                    print("=" * 50 + "\n")

                    print("\a")

                else:
                    alarms_to_keep.append(alarm)

            if len(alarms_to_keep) != len(alarms):
                save_alarms(alarms_to_keep)

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nAlarm monitor stopped.")


def main():
    parser = argparse.ArgumentParser(
        description="Alarm Clock CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # Add Alarm
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new alarm"
    )

    add_parser.add_argument(
        "time",
        help="Alarm time in HH:MM format"
    )

    add_parser.add_argument(
        "message",
        nargs="?",
        default="Alarm!",
        help="Alarm message"
    )

    # List Alarms
    subparsers.add_parser(
        "list",
        help="List all alarms"
    )

    # Delete Alarm
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete an alarm"
    )

    delete_parser.add_argument(
        "id",
        type=int,
        help="Alarm ID"
    )

    # Run Monitor
    subparsers.add_parser(
        "run",
        help="Start alarm monitoring"
    )

    args = parser.parse_args()

    if args.command == "add":
        add_alarm(
            args.time,
            args.message
        )

    elif args.command == "list":
        list_alarms()

    elif args.command == "delete":
        delete_alarm(
            args.id
        )

    elif args.command == "run":
        run_alarm_monitor()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()