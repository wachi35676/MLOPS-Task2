# MLOps Class Activity

This repository contains the code and test suite for the MLOps class activity.

## Description

The  `StudentsInMLOps` class encapsulates methods for managing student enrollment in an MLOps course:

* `enrollStudents(int)`:  Enrolls a specified number of students.
* `dropStudents(int)`: Drops a specified number of students.
* `getTotalStrength()`: Returns the total number of enrolled students.
* `getClassName()`:  Returns the class name.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repository-name>.git
   ```
2. **Install dependencies:**
   ```bash
   cd mlops-class-activity
   make install 
   ```

## Testing

To run the test suite:
```bash
make test
```

## GitHub Actions

A GitHub Actions workflow is included in this repository to automatically run tests on every push to the repository. This ensures code quality and prevents regressions.

