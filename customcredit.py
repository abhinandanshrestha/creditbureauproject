import csv
import random
from datetime import datetime, timedelta

def generate_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        user_id = i
        credit_score = random.randint(500, 850)
        name = f"User {i}"
        date_of_birth = generate_random_date_of_birth()
        address = f"{i} Main St"
        ssn = generate_random_ssn()
        credit_card_number = generate_random_credit_card_number()
        report_date = generate_random_report_date()
        open_accounts = random.randint(1, 10)
        closed_accounts = random.randint(0, open_accounts)
        total_accounts = open_accounts + closed_accounts
        oldest_account_type = generate_random_account_type()
        oldest_account_date = generate_random_account_date(report_date)
        recent_account_type = generate_random_account_type()
        recent_account_date = generate_random_account_date(report_date)
        active_accounts = random.randint(0, open_accounts)
        credit_utilization = round(random.uniform(0.1, 0.9), 2)
        payment_history = round(random.uniform(0.5, 1.0), 2)

        record = [
            user_id, credit_score, name, date_of_birth, address, ssn, credit_card_number,
            report_date, open_accounts, closed_accounts, total_accounts, oldest_account_type,
            oldest_account_date, recent_account_type, recent_account_date, active_accounts,
            closed_accounts, credit_utilization, payment_history
        ]
        data.append(record)
    return data

def generate_random_date_of_birth():
    # Generate a random date of birth between 1950 and 2000
    start_date = datetime.strptime('01/01/1950', '%m/%d/%Y')
    end_date = datetime.strptime('01/01/2000', '%m/%d/%Y')
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%m/%d/%Y')

def generate_random_ssn():
    # Generate a random SSN in the format XXX-XX-XXXX
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def generate_random_credit_card_number():
    # Generate a random credit card number in the format XXXX-XXXX-XXXX-XXXX
    return f"{'XXXX-' * 3}{random.randint(1000, 9999):04d}"

def generate_random_report_date():
    # Generate a random report date within the last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%m/%d/%Y')

def generate_random_account_type():
    # Generate a random account type from a list of options
    account_types = ["Credit Card", "Mortgage", "Auto Loan", "Personal Loan", "Home Loan"]
    return random.choice(account_types)

def generate_random_account_date(report_date):
    # Generate a random account date within the last 10 years from the report date
    report_date = datetime.strptime(report_date, '%m/%d/%Y')
    start_date = report_date - timedelta(days=365 * 10)
    random_date = start_date + timedelta(days=random.randint(0, (report_date - start_date).days))
    return random_date.strftime('%m/%d/%Y')

# Generate 10 records of data with variations
data = generate_data(10)

# Define the CSV file path
csv_file = 'credit_scores.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['user_id', 'credit_score', 'name', 'date_of_birth', 'address', 'ssn',
                     'credit_card_number', 'report_date', 'open_accounts', 'closed_accounts',
                     'total_accounts', 'oldest_account_type', 'oldest_account_date',
                     'recent_account_type', 'recent_account_date', 'active_accounts',
                     'closed_accounts', 'credit_utilization', 'payment_history'])
    writer.writerows(data)

print(f"Data saved to {csv_file}")
