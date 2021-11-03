import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

with open("potential-contacts.txt" ,"r") as f:
    file_content = f.read()

all_emails = re.findall(email_regex , file_content)

all_emails.sort()
emails = []
for email in all_emails:
    if email not in emails:
        emails.append(email)

with open("phone_numbers.txt","w") as file:
    for email in emails:
        file.writelines(f"{email}\n")
    print("done")
        