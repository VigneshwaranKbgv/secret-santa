import csv
import random
from typing import List, Dict
from .employee import Employee

class SecretSanta:
    def __init__(self, employees: List[Employee], previous_assignments: Dict[str, str] = None):
        self.employees = employees
        self.previous_assignments = previous_assignments or {}

    def assign(self) -> Dict[Employee, Employee]:
        assignments = {}
        available = self.employees.copy()
        random.shuffle(available)

        for santa in self.employees:
            possible = [e for e in available if e != santa and self.previous_assignments.get(santa.email) != e.email]
            if not possible:
                # Restart assignment if no valid options
                return self.assign()
            secret_child = random.choice(possible)
            assignments[santa] = secret_child
            available.remove(secret_child)

        return assignments

    def load_employees(self, file_path: str) -> List[Employee]:
        employees = []
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    employees.append(Employee(name=row['Employee_Name'], email=row['Employee_EmailID']))
        except FileNotFoundError:
            raise Exception(f"File {file_path} not found.")
        except KeyError as e:
            raise Exception(f"Missing column in employees CSV: {e}")
        return employees

    def load_previous_assignments(self, file_path: str) -> Dict[str, str]:
        assignments = {}
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']
        except FileNotFoundError:
            # It's okay if there's no previous assignment
            pass
        except KeyError as e:
            raise Exception(f"Missing column in previous assignments CSV: {e}")
        return assignments

    def save_assignments(self, assignments: Dict[Employee, Employee], output_file: str):
        try:
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for santa, child in assignments.items():
                    writer.writerow({
                        'Employee_Name': santa.name,
                        'Employee_EmailID': santa.email,
                        'Secret_Child_Name': child.name,
                        'Secret_Child_EmailID': child.email
                    })
        except Exception as e:
            raise Exception(f"Failed to write to {output_file}: {e}") 