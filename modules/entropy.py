import math


def calculate_entropy():

    password = input("\nEnter Password: ")

    charset = 0

    if any(c.islower() for c in password):
        charset += 26

    if any(c.isupper() for c in password):
        charset += 26

    if any(c.isdigit() for c in password):
        charset += 10

    if any(not c.isalnum() for c in password):
        charset += 32

    entropy = len(password) * math.log2(charset)

    print("\n" + "=" * 60)

    print("PASSWORD ENTROPY")

    print("=" * 60)

    print(f"Character Set : {charset}")

    print(f"Length        : {len(password)}")

    print(f"Entropy       : {entropy:.2f} bits")

    print("=" * 60)

    input("\nPress Enter to continue...")