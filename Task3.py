import re

def assess_password_strength(password):
    """
    Evaluates the strength of the given password and provides feedback.
    
    Criteria:
    - Length (>=8)
    - Contains lowercase letters
    - Contains uppercase letters
    - Contains digits
    - Contains special characters
    """

    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")
    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")
    # Check digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add digits (0-9).")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (e.g. @, #, $, %).")

    # Determine strength label
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength, suggestions = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("Your password is very strong! Good job.")

if __name__ == "__main__":
    main()
