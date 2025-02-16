from .secret_santa import SecretSanta

def main():
    secret_santa = SecretSanta([])
    employees = secret_santa.load_employees('data/employees.csv')
    previous_assignments = secret_santa.load_previous_assignments('data/previous_assignments.csv')
    secret_santa.employees = employees
    secret_santa.previous_assignments = previous_assignments

    assignments = secret_santa.assign()
    secret_santa.save_assignments(assignments, 'data/secret_santa_assignments.csv')
    print("Secret Santa assignments have been generated successfully.")

if __name__ == '__main__':
    main() 