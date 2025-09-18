
mail = input("Enter th email: ").strip()
at_index = mail.find("@")
name = mail[:at_index]
mail_provider = mail[at_index + 1 :]
print(f"Name: {name}")
print(f"Mail Provider: {mail_provider}")
