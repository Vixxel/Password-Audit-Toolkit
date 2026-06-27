import re
from modules.session import analysis_results



# NEW FUNCTION
def analyze_password_data(password):

    score = 0

    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    repeated = bool(
        re.search(
            r"(.)\1{2,}",
            password
        )
    )

    sequential = False

    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "0123456789"
    ]

    for sequence in sequences:
        for i in range(len(sequence) - 3):
            if sequence[i:i + 4] in password:
                sequential = True

    if length >= 8:
        score += 15

    if length >= 12:
        score += 20

    if length >= 16:
        score += 15

    if has_upper:
        score += 10

    if has_lower:
        score += 10

    if has_number:
        score += 10

    if has_special:
        score += 15

    if not repeated:
        score += 5

    if not sequential:
        score += 10

    if score >= 90:
        strength = "VERY STRONG"

    elif score >= 75:
        strength = "STRONG"

    elif score >= 60:
        strength = "MEDIUM"

    elif score >= 40:
        strength = "WEAK"

    else:
        strength = "VERY WEAK"

    return score, strength


# YOUR EXISTING FUNCTION
def analyze_password():

    password = input("\nEnter Password: ")

    score, strength = analyze_password_data(password)

    analysis_results.append(
        {
            "Password": password,
            "Length": len(password),
            "Score": score,
            "Strength": strength
        }
    )

    print("\n" + "=" * 60)

    print("PASSWORD ANALYSIS")

    print("=" * 60)

    print(f"Length             : {len(password)}")
    print(f"Score              : {score}/100")
    print(f"Strength           : {strength}")

    print("=" * 60)

    input("\nPress Enter to continue...")

    # Everything below here stays exactly like it already is.

