emails = [
    "abc@gmail.com",
    "xyz@gmail.com",
    "abc@gmail.com",
    "test@gmail.com",
    "xyz@gmail.com"
]

seen = set()
unique_email = []

for email in emails:
    if email not in seen:
        seen.add(email)
        unique_email.append(email)

print(unique_email)