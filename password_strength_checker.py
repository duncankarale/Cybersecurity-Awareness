# password_strength_checker.py
# A simple cybersecurity awareness tool

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in "!@#$%^&*()" for char in password):
        score += 1

    if score == 4:
        return "Strong password ✅"
    elif score == 3:
        return "Moderate password ⚠️"
    else:
        return "Weak password ❌"

if __name__ == "__main__":
    user_pass = input("Enter a password to test: ")
    print(check_strength(user_pass))
