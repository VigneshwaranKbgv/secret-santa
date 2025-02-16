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


- **`src/`**: Contains the main application code.
  - `employee.py`: Defines the `Employee` class.
  - `secret_santa.py`: Contains the `SecretSanta` class handling the assignment logic.
  - `main.py`: Orchestrates the loading of data, assignment process, and saving of results.
  - `__init__.py`: Makes `src/` a Python package.

- **`tests/`**: Contains unit tests to ensure the correctness of the assignment logic.
  - `test_secret_santa.py`: Unit tests for the `SecretSanta` class.
  - `__init__.py`: Makes `tests/` a Python package.

- **`data/`**: Stores input and output CSV files.
  - `employees.csv`: Lists all employees participating in Secret Santa.
  - `previous_assignments.csv`: (Optional) Contains last year's Secret Santa pairings.
  - `secret_santa_assignments.csv`: Generated output with the new Secret Santa pairings.

- **`README.md`**: Provides comprehensive documentation for the project.
- **`requirements.txt`**: Lists the project's dependencies.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Version 3.6 or higher is installed on your machine. [Download Python](https://www.python.org/downloads/)
- **Git**: For version control and cloning the repository. [Download Git](https://git-scm.com/downloads)
- **Virtual Environment (Optional but Recommended)**: To create an isolated Python environment.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**

   Use Git to clone the repository to your local machine:

   ```bash
   git clone https://github.com/vigneshwaranKbgv/secret-santa.git
   cd secret-santa
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: For this project, `requirements.txt` is empty as only standard libraries are used. However, it's included for future extensibility.*

## Usage

### Preparing Input Files

1. **Employees File (`employees.csv`)**

   Ensure that `employees.csv` is placed inside the `data/` directory with the following headers:

   ```csv
   Employee_Name,Employee_EmailID
   Hamish Murray,hamish.murray@acme.com
   Layla Graham,layla.graham@acme.com
   Matthew King,matthew.king@acme.com
   ...
   ```

2. **Previous Assignments File (`previous_assignments.csv`)** *(Optional)*

   If you have last year's Secret Santa pairings, place `previous_assignments.csv` in the `data/` directory with the following headers:

   ```csv
   Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
   Hamish Murray,hamish.murray@acme.com,Layla Graham,layla.graham@acme.com
   Layla Graham,layla.graham@acme.com,Matthew King,matthew.king@acme.com
   ...
   ```

   *If this file is not provided, the program will skip the check for previous assignments.*

### Running the Program

Execute the main script to generate Secret Santa assignments:

bash
python -m src.main


Upon successful execution, a new file `secret_santa_assignments.csv` will be created in the `data/` directory with the following structure:

```csv
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Hamish Murray,hamish.murray@acme.com,Ethan Murray,ethan.murray@acme.com
Layla Graham,layla.graham@acme.com,Charlie Ross,charlie.ross@acme.com
Matthew King,matthew.king@acme.com,Mark Lawrence,mark.lawrence@acme.com
...
```

### Example Output

Here is a sample of what the `secret_santa_assignments.csv` might look like:

csv
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Hamish Murray,hamish.murray@acme.com,Ethan Murray,ethan.murray@acme.com
Layla Graham,layla.graham@acme.com,Charlie Ross,charlie.ross@acme.com
Matthew King,matthew.king@acme.com,Mark Lawrence,mark.lawrence@acme.com
...


## Running Tests

Unit tests are provided to ensure the correctness and reliability of the assignment logic.

### Steps to Run Unit Tests

1. **Navigate to the Project Directory**

   Ensure you're in the project's root directory:

   ```bash
   cd secret-santa
   ```

2. **Activate the Virtual Environment** *(if not already activated)*

   ```bash
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Run the Tests Using `unittest`**

   Execute the following command to run all tests in the `tests/` directory:

   ```bash
   python -m unittest discover tests
   ```

   **Alternatively**, to run a specific test file:

   ```bash
   python -m unittest tests/test_secret_santa.py
   ```

### Interpreting Test Results

- **All Tests Pass**

  ```
  ...
  ----------------------------------------------------------------------
  Ran 3 tests in 0.001s

  OK
  ```

  **Meaning**: Your assignment logic is working as expected.

- **Tests Fail**

  ```
  .E.
  ======================================================================
  ERROR: test_no_self_assignment (tests.test_secret_santa.TestSecretSanta)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests/test_secret_santa.py", line XX, in test_no_self_assignment
      self.assertNotEqual(santa.email, child.email, f"{santa.name} was assigned themselves.")
  AssertionError: 'john.doe@example.com' == 'john.doe@example.com' : John Doe was assigned themselves.

  ----------------------------------------------------------------------
  Ran 3 tests in 0.002s

  FAILED (errors=1)
  ```

  **Meaning**: One or more tests encountered an error or failed an assertion. Review the traceback to identify and fix the issue.

## Error Handling

The program includes mechanisms to handle various potential errors gracefully:

1. **File Not Found**

   - **Scenario**: If `employees.csv` or `previous_assignments.csv` is missing.

   - **Response**: The program raises an exception with a clear message.

     ```bash
     Exception: File data/employees.csv not found.
     ```

2. **Invalid CSV Format**

   - **Scenario**: If required columns are missing from the CSV files.

   - **Response**: The program raises an exception indicating the missing column.

     ```bash
     Exception: Missing column in employees CSV: 'Employee_EmailID'
     ```

3. **No Possible Assignments**

   - **Scenario**: If it's impossible to assign Secret Santas without violating constraints (e.g., only one employee).

   - **Response**: The program may enter a recursive loop. To handle this, consider implementing a maximum number of retries or alternative assignment strategies.

4. **General Exceptions**

   - **Scenario**: Other unexpected errors during file writing or processing.

   - **Response**: The program raises an exception with a descriptive message.

     ```bash
     Exception: Failed to write to data/secret_santa_assignments.csv: [Error Details]
     ```

## Contributing

Contributions are welcome! Follow these steps to contribute to the project:

1. **Fork the Repository**

   Click the "Fork" button on the repository page to create your own copy.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/VigneshwaranKbgv/secret-santa.git
   cd secret-santa
   ```

3. **Create a Branch**

   Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature/add-enhancement
   ```

4. **Make Your Changes**

   Commit your changes with clear and descriptive messages:

   ```bash
   git add src/new_feature.py
   git commit -m "Add new feature to enhance assignment logic"
   ```

5. **Push to Your Fork**

   ```bash
   git push origin feature/add-enhancement
   ```

6. **Submit a Pull Request**

   Go to the original repository on GitHub and click "New Pull Request." Provide a clear description of your changes and submit.

### Guidelines for Contributions

- **Code Quality**: Follow PEP 8 style guidelines for Python code.
- **Documentation**: Update the README and any relevant documentation with your changes.
- **Testing**: Add or update unit tests to cover your changes.
- **Commit Messages**: Write clear and concise commit messages describing the purpose of the changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

## Additional Information

- **Contact**: If you encounter any issues or have questions, feel free to open an issue on the GitHub repository.
- **Acknowledgments**: Special thanks to all contributors and the OpenAI team for providing guidance and support.

---


