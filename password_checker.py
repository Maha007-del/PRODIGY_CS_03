import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter")

    # Digit check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character")

    # Strength rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, feedback


if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    strength, score, feedback = check_password_strength(pwd)

    print(f"\nPassword Strength: {strength} ({score}/6)")
    if feedback:
        print("\nSuggestions to improve:")
        for f in feedback:
            print(f)
    else:
        print("✅ Great password!")