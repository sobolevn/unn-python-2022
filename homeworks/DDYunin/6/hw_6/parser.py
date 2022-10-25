import csv

def start_parsing():
    all_emails_not_flatten = parse_emails_from_csv_file()
    # Вытягиваю list of lists в простой list
    emails = flatten(all_emails_not_flatten)

def parse_emails_from_csv_file():
    emails = []
    with open('hw_6/emails.csv') as f:
        reader = csv.reader(f)
        # Можно ли возвращать значение прямо из контекстного менеджера, не будет ли это плохо?
        emails = list(reader)
    return emails

def flatten(list_of_emails):
    return [item for sublist in list_of_emails for item in sublist]