# Alarm Clock CLI

## Overview

This project is a command-line alarm clock application built in Python.

The assignment intentionally provided minimal requirements, so the first step was to define a practical scope and focus on delivering a complete, maintainable solution within the available time.

The goal was not to maximize features, but to demonstrate problem definition, engineering decision-making, AI-assisted development, validation, and clean implementation.

---

## Problem Definition

Build a command-line application that allows users to:

* Create alarms
* View configured alarms
* Delete alarms
* Trigger alarms when the scheduled time is reached
* Persist alarms between application restarts

---

## Requirements

### Functional Requirements

* Create an alarm with a scheduled time and message
* List all configured alarms
* Delete an existing alarm
* Continuously monitor alarms
* Trigger alarms when the scheduled time is reached
* Persist alarms locally

### Non-Functional Requirements

* CLI-only application
* No web interface
* No external database
* Minimal dependencies
* Readable and maintainable code
* Easy to extend

---

## Assumptions

* Alarm precision is at the minute level (`HH:MM`)
* Local system time is used
* Single-user application
* Multiple alarms can exist for the same time
* Triggered alarms are automatically removed after execution

---

## AI-Assisted Development Process

AI was used as an engineering assistant throughout the exercise.

### Areas Where AI Was Used

* Requirement refinement
* Scope definition
* Architecture discussions
* Edge case identification
* Test case generation
* Code review and validation

### Example Prompts Used

#### Requirements Refinement

> Design requirements for a Python CLI alarm clock application intended for a coding exercise. Focus on practical functionality, maintainability, and simplicity.

#### Architecture Discussion

> Suggest a simple and maintainable folder structure for a Python CLI application that stores alarms in a JSON file.

#### Test Planning

> Suggest meaningful test cases for validating an alarm clock CLI application.

#### Code Review

> Review this Python code and identify potential bugs, edge cases, and opportunities for improvement.

All AI-generated suggestions and code were reviewed before implementation.

---

## Design Decisions

### Storage Strategy

Alarms are stored in a local JSON file.

Example:

```json
[
  {
    "id": 1,
    "time": "08:30",
    "message": "Morning workout"
  }
]
```

#### Why JSON?

* No database setup required
* Human-readable format
* Simple persistence mechanism
* Appropriate for the scale of this application

---

### Application Structure

```text
alarm-clock-cli/
│
├── main.py
├── storage.py
├── alarms.json
├── test_main.py
├── requirements.txt
└── README.md
```

#### Responsibilities

##### main.py

* CLI command parsing
* Alarm validation
* Alarm creation
* Alarm deletion
* Alarm monitoring

##### storage.py

* Reading alarms from storage
* Writing alarms to storage

##### alarms.json

* Persistent alarm storage

##### test_main.py

* Automated test cases

---

## Tradeoffs

### Included

* Alarm creation
* Alarm deletion
* Alarm listing
* Time validation
* Alarm monitoring
* JSON persistence
* Automated tests

### Excluded

* GUI
* Database integration
* Recurring alarms
* Snooze functionality
* Desktop notifications
* Timezone management
* Multi-user support

These features were intentionally excluded to keep the solution focused on core functionality while maintaining simplicity and reliability.

---

## Validation & Testing

The following scenarios were validated manually:

### Alarm Creation

Command:

```bash
python main.py add 21:30 "Workout"
```

Expected Result:

* Alarm is stored in `alarms.json`

### Invalid Time Validation

Command:

```bash
python main.py add 25:99 "Invalid Alarm"
```

Expected Result:

* Validation error is displayed

### Alarm Listing

Command:

```bash
python main.py list
```

Expected Result:

* Configured alarms are displayed

### Alarm Deletion

Command:

```bash
python main.py delete 1
```

Expected Result:

* Alarm is removed from storage

### Alarm Triggering

Command:

```bash
python main.py run
```

Expected Result:

* Alarm is triggered when the scheduled time is reached
* Triggered alarm is removed from storage

---

## Automated Tests

The project includes automated tests covering:

* Valid time validation
* Invalid hour validation
* Invalid minute validation
* Invalid format validation
* Alarm persistence
* Empty alarm list handling
* Multiple alarm scenarios

Run tests using:

```bash
pytest -v
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd alarm-clock-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Create an Alarm

```bash
python main.py add 08:30 "Morning workout"
```

### List Alarms

```bash
python main.py list
```

### Delete an Alarm

```bash
python main.py delete 1
```

### Start Alarm Monitoring

```bash
python main.py run
```

---

## Future Improvements

Given additional time, the following enhancements could be considered:

* Recurring daily alarms
* Snooze functionality
* Desktop notifications
* Timezone support
* Additional automated tests
* More sophisticated scheduling mechanism
* Logging and monitoring support

---

## Conclusion

This solution focuses on delivering a complete, maintainable command-line alarm clock while demonstrating engineering decision-making, AI-assisted development, validation, and testing. The implementation prioritizes simplicity, readability, and correctness over feature count.
