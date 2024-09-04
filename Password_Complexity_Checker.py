import re

def check_password_strength(password):
    # Criteria for password complexity
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Counting the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback to user
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    # Output strength and feedback
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for advice in feedback:
            print(f"- {advice}")
    else:
        print("Your password is very strong!")

# Example usage
if __name__ == "__main__":
    # Developed by Sworup Kumar Sahu
    password = input("Enter your password to check its strength: ")
    check_password_strength(password)
