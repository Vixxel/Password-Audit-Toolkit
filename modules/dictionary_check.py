import os

WORDLIST_FOLDER = "wordlists"


def dictionary_check():

    password = input("\nEnter Password: ")

    if not os.path.exists(WORDLIST_FOLDER):

        print("\nWordlists folder not found.")

        input("\nPress Enter...")
        return

    wordlists = [

        file

        for file in os.listdir(WORDLIST_FOLDER)

        if file.endswith(".txt")

    ]

    if not wordlists:

        print("\nNo wordlists found.")

        input("\nPress Enter...")
        return

    print("\n" + "=" * 60)

    print("AVAILABLE WORDLISTS")

    print("=" * 60)

    for index, wordlist in enumerate(wordlists, start=1):

        print(f"[{index}] {wordlist}")

    print(f"[{len(wordlists)+1}] Search ALL Wordlists")

    try:

        choice = int(input("\nSelect Option: "))

    except ValueError:

        print("\nInvalid selection.")

        input("\nPress Enter...")
        return

    found = []

    if choice == len(wordlists) + 1:

        selected = wordlists

    elif 1 <= choice <= len(wordlists):

        selected = [wordlists[choice - 1]]

    else:

        print("\nInvalid selection.")

        input("\nPress Enter...")
        return

    for wordlist in selected:

        filepath = os.path.join(
            WORDLIST_FOLDER,
            wordlist
        )

        with open(
            filepath,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            passwords = {

                line.strip().lower()

                for line in file

            }

        if password.lower() in passwords:

            found.append(wordlist)

    print("\n" + "=" * 60)

    print("DICTIONARY CHECK")

    print("=" * 60)

    if found:

        print("\nPASSWORD FOUND\n")

        for wordlist in found:

            print(f"✓ {wordlist}")

    else:

        print("\nPassword was NOT found in the selected wordlist(s).")

    print("\n" + "=" * 60)

    input("\nPress Enter...")