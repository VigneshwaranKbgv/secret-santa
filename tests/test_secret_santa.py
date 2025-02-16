import unittest
import sys
import os

# Add src to the system path before importing modules from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.secret_santa import SecretSanta
from src.employee import Employee

class TestSecretSanta(unittest.TestCase):
    def setUp(self):
        self.employees = [
            Employee('Hamish Murray', 'hamish.murray@acme.com'),
            Employee('Layla Graham', 'layla.graham@acme.com'),
            Employee('Matthew King', 'matthew.king@acme.com'),
            Employee('Benjamin Collins', 'benjamin.collins@acme.com'),
            Employee('Isabella Scott', 'isabella.scott@acme.com'),
            Employee('Charlie Ross', 'charlie.ross@acme.com'),
            Employee('Hamish Murray Sr.', 'hamish.murray.sr@acme.com'),
            Employee('Piper Stewart', 'piper.stewart@acme.com'),
            Employee('Spencer Allen', 'spencer.allen@acme.com'),
            Employee('Charlie Wright', 'charlie.wright@acme.com'),
            Employee('Hamish Murray Jr.', 'hamish.murray.jr@acme.com'),
            Employee('Charlie Ross Jr.', 'charlie.ross.jr@acme.com'),
            Employee('Ethan Murray', 'ethan.murray@acme.com'),
            Employee('Matthew King Jr.', 'matthew.king.jr@acme.com'),
            Employee('Mark Lawrence', 'mark.lawrence@acme.com'),
        ]
        self.previous_assignments = {
            'hamish.murray@acme.com': 'layla.graham@acme.com',
            'layla.graham@acme.com': 'matthew.king@acme.com',
            # Add other previous assignments as needed
        }
        self.secret_santa = SecretSanta(self.employees, self.previous_assignments)

    def test_no_self_assignment(self):
        assignments = self.secret_santa.assign()
        for santa, child in assignments.items():
            self.assertNotEqual(santa.email, child.email, f"{santa.name} was assigned themselves.")

    def test_no_repeated_assignment(self):
        assignments = self.secret_santa.assign()
        for santa, child in assignments.items():
            if santa.email in self.previous_assignments:
                self.assertNotEqual(child.email, self.previous_assignments[santa.email],
                                     f"{santa.name} was assigned the same secret child as last year.")

    def test_unique_assignments(self):
        assignments = self.secret_santa.assign()
        assigned_children = [child.email for child in assignments.values()]
        self.assertEqual(len(assigned_children), len(set(assigned_children)),
                         "A secret child was assigned to multiple employees.")

if __name__ == '__main__':
    unittest.main() 