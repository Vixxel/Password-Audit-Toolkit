import os

from modules.password_strength import analyze_password_data


def password_statistics():

    filename = input(
        "\nEnter password file: "
    )

    if not os.path.exists(filename):

        print("\nFile not found.")

        input("\nPress Enter...")
        return

    with open(
        filename,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        passwords = [

            line.strip()

            for line in file

            if line.strip()

        ]

    if len(passwords) == 0:

        print("\nNo passwords found.")

        input("\nPress Enter...")
        return

    total = len(passwords)

    total_length = 0

    longest = 0

    shortest = 999999

    categories = {

        "VERY WEAK": 0,
        "WEAK": 0,
        "MEDIUM": 0,
        "STRONG": 0,
        "VERY STRONG": 0

    }

    duplicates = len(passwords) - len(set(passwords))

    for password in passwords:

        score, strength = analyze_password_data(password)

        categories[strength] += 1

        length = len(password)

        total_length += length

        longest = max(
            longest,
            length
        )

        shortest = min(
            shortest,
            length
        )

    average = total_length / total

    print("\n" + "=" * 60)

    print("PASSWORD STATISTICS")

    print("=" * 60)

    print(f"Passwords Checked : {total}")

    print()

    print(f"Very Weak         : {categories['VERY WEAK']}")
    print(f"Weak              : {categories['WEAK']}")
    print(f"Medium            : {categories['MEDIUM']}")
    print(f"Strong            : {categories['STRONG']}")
    print(f"Very Strong       : {categories['VERY STRONG']}")

    print()

    print(f"Average Length    : {average:.2f}")

    print(f"Longest Password  : {longest}")

    print(f"Shortest Password : {shortest}")

    print(f"Duplicate Entries : {duplicates}")

    print("=" * 60)

    input("\nPress Enter...")