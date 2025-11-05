specialChars = ["!", "@", "#", "$", "%", "^","&"]


while True:
    password = input("Enter a password: ")

    if password == "quit":
        break
    
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.islower() for char in password):
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    for char in password:
        if char in specialChars:
            strength += 1
            break

    if strength == 5:
        print("Very Strong")
    elif strength == 4:
        print("Strong")
    else:
        print("Weak")





