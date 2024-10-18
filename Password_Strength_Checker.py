import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    strength_score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "criteria": {
            "length": length_criteria,
            "uppercase": upper_criteria,
            "lowercase": lower_criteria,
            "digits": digit_criteria,
            "special_characters": special_criteria
        }
    }

def main():
    password = input("Enter a password to assess its strength: ")
    result = assess_password_strength(password)

    print(f"\nPassword Strength: {result['strength']}")
    print("Criteria Check:")
    print(f"  - Length (>=8): {'✔' if result['criteria']['length'] else '✖'}")
    print(f"  - Uppercase Letters: {'✔' if result['criteria']['uppercase'] else '✖'}")
    print(f"  - Lowercase Letters: {'✔' if result['criteria']['lowercase'] else '✖'}")
    print(f"  - Digits: {'✔' if result['criteria']['digits'] else '✖'}")
    print(f"  - Special Characters: {'✔' if result['criteria']['special_characters'] else '✖'}")

if __name__ == "__main__":
    main()
