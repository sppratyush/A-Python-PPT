def check_password_strength(password):
    length_ok = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    if len(password) >= 8:
        length_ok = True
    else:
        print("Password should be at least 8 characters long.")
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_characters:
            has_special = True

    if not has_upper:
        print("Add at least one uppercase letter.")
    if not has_lower:
        print("Add at least one lowercase letter.")
    if not has_digit:
        print("Add at least one digit.")
    if not has_special:
        print("Add at least one special character.")

    strength = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    print("\nPassword Strength:", end=" ")
    if strength == 5:
        print("💪 Very Strong")
    elif strength >= 3:
        print("🙂 Medium")
    else:
        print("⚠️ Weak")


password = input("Enter your password: ")
check_password_strength(password)