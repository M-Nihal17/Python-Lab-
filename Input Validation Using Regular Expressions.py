import re

# Email validation
email = input("Enter email: ")
print("Valid" if re.match(r'^[\w.+-]+@[\w-]+(\.[\w-]+)+$', email) else "Invalid")

# Phone validation
phone = input("Enter phone: ")
print("Valid" if re.match(r'^(\+91[- ]?)?[6-9]\d{9}$', phone) else "Invalid")

# Transaction ID extraction
log = input("Enter log: ")
ids = re.findall(r'TXN\d{6,10}', log)

print("Transaction IDs:", ids)
print("Total IDs:", len(ids))