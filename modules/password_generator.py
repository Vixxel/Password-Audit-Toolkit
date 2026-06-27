import random
import string


def generate_password():

    length = int(input("\nPassword Length: "))

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(

        random.choice(characters)

        for _ in range(length)

    )

    print("\nGenerated Password\n")

    print(password)

    input("\nPress Enter to continue...")