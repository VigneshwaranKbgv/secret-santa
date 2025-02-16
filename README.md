# Secret Santa Assignment Program

This project automates the assignment of Secret Santa pairings among employees of the "Acme" company. It ensures that each employee is anonymously assigned another employee as their Secret Santa, adhering to specific constraints to maintain fairness and confidentiality.

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Running Tests](#running-tests)
7. [Error Handling](#error-handling)
8. [Version Control](#version-control)
9. [Contributing](#contributing)
10. [License](#license)

---

## Overview

The Secret Santa Assignment Program is designed to streamline the process of assigning Secret Santa pairings among employees. It ensures that:

- **No Self-Assignments**: An employee cannot be assigned themselves.
- **No Repeated Assignments**: Employees are not assigned the same Secret Santa as in the previous year.
- **Unique Assignments**: Each Secret Santa assignment is unique, meaning each Secret Santa is assigned to exactly one employee.
- **Complete Assignments**: Every employee is assigned exactly one Secret Santa.

The program reads employee data and previous year's assignments from CSV files, processes the assignments based on the defined constraints, and outputs the new Secret Santa pairings to a CSV file.

## Project Structure 

secret-santa/
├── src/
│ ├── init.py
│ ├── employee.py
│ ├── main.py
│ └── secret_santa.py
├── tests/
│ ├── init.py
│ └── test_secret_santa.py
├── data/
│ ├── employees.csv
│ ├── previous_assignments.csv
│ └── secret_santa_assignments.csv
├── README.md
├── requirements.txt
└── .gitignore

