import hashlib


def hash_password():

    password = input("\nEnter Password: ")

    print("\nSelect Hash Algorithm\n")

    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[4] SHA512")

    choice = input("\nChoice: ")

    if choice == "1":

        hashed = hashlib.md5(
            password.encode()
        ).hexdigest()

        algorithm = "MD5"

    elif choice == "2":

        hashed = hashlib.sha1(
            password.encode()
        ).hexdigest()

        algorithm = "SHA1"

    elif choice == "3":

        hashed = hashlib.sha256(
            password.encode()
        ).hexdigest()

        algorithm = "SHA256"

    elif choice == "4":

        hashed = hashlib.sha512(
            password.encode()
        ).hexdigest()

        algorithm = "SHA512"

    else:

        print("\nInvalid Selection.")

        input("\nPress Enter...")
        return

    print("\n" + "=" * 60)

    print("PASSWORD HASH")

    print("=" * 60)

    print(f"Algorithm : {algorithm}")

    print()

    print(hashed)

    print("=" * 60)

    input("\nPress Enter...")

def identify_hash():

    hash_value = input(
        "\nEnter Hash: "
    ).strip()

    length = len(hash_value)

    print("\n" + "=" * 60)

    print("HASH IDENTIFICATION")

    print("=" * 60)

    if length == 32:

        print("Likely MD5")

    elif length == 40:

        print("Likely SHA1")

    elif length == 64:

        print("Likely SHA256")

    elif length == 128:

        print("Likely SHA512")

    else:

        print("Unknown Hash Type")

    print("=" * 60)

    input("\nPress Enter...")