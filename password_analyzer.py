import re

# Load weak passwords from external file
def load_weak_passwords(file_path="weak_passwords.txt"):
    try:
        with open(file_path, "r") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        return ["password", "123456", "admin", "qwerty", "letmein"]

# Function to check repeated characters or simple sequences
def has_repeated_or_sequential(password):
    patterns = [
        r"(.)\1{2,}",            # repeated characters like "aaa"
        r"0123", r"1234", r"2345", r"3456", r"4567",
        r"abcd", r"bcde", r"cdef", r"defg", r"abcd1234"
    ]
    for pattern in patterns:
        if re.search(pattern, password.lower()):
            return True
    return False

# Function to check the strength of a password
def check_password_strength(password, weak_passwords):
    score = 0
    feedback = []

    # Check if the password is long enough
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!, @, #, etc.).")

    # Check against weak password list
    if password.lower() in weak_passwords:
        feedback.append("This is a very common and weak password. Avoid using it.")

    # Check for repeated or sequential patterns
    if has_repeated_or_sequential(password):
        feedback.append("Avoid repeated patterns or simple sequences like 'aaa' or '1234'.")

    # Determine password strength
    if score == 4 and password.lower() not in weak_passwords and not has_repeated_or_sequential(password):
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Main function
if __name__ == "__main__":
    weak_passwords = load_weak_passwords()
    print("=== Password Strength Analyzer ===")
    user_password = input("Enter a password to check: ")
    strength, tips = check_password_strength(user_password, weak_passwords)

    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Suggestions to improve your password:")
        for tip in tips:
            print(f"- {tip}")
    else:
        print("Great job! Your password looks strong.")