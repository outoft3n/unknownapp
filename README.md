# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
![Use Case Diagram](UCD.png)

### Flowchart of the main workflow
```mermaid
flowchart TD
    Start([Start]) --> Menu[Display Menu]

    Menu --> Choice{Select Option}

    Choice -->|1| ViewCourses
    Choice -->|2| ViewStudent
    Choice -->|3| Enroll
    Choice -->|4| Drop
    Choice -->|5| ViewSchedule
    Choice -->|6| ViewRoster
    Choice -->|7| Tuition
    Choice -->|0| Exit

    ViewCourses --> Menu
    ViewStudent --> Menu

    Enroll --> Check1{Student exists?}
    Check1 -->|No| Error1
    Check1 -->|Yes| Check2{Course exists?}

    Check2 -->|No| Error2
    Check2 -->|Yes| Check3{Already enrolled?}

    Check3 -->|Yes| Error3
    Check3 -->|No| Check4{Course full?}

    Check4 -->|Yes| Error4
    Check4 -->|No| Check5{Prerequisites met?}

    Check5 -->|No| Error5
    Check5 -->|Yes| Check6{Time conflict?}

    Check6 -->|Yes| Error6
    Check6 -->|No| Success[Enroll Success]

    Success --> Menu

    Drop --> Menu
    ViewSchedule --> Menu
    ViewRoster --> Menu
    Tuition --> Menu
```

### Prompts
for python code
```
You are a senior software developer.

Convert the course enrollment logic from Java into Python.

Requirements:
- preserve the original logic exactly
- include:
  - prerequisite checking
  - capacity validation
  - time conflict detection
- use clean and readable Python code
- avoid adding new features not present in the original code

Output only the Python function.
```