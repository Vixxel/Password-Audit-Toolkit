import os
from modules.export_utils import export_csv, export_json
from modules.html_report import create_html
from modules.password_strength import analyze_password
from modules.entropy import calculate_entropy
from modules.password_generator import generate_password
from modules.dictionary_check import dictionary_check
from modules.pdf_report import create_pdf
from modules.statistics import password_statistics
from modules.session import analysis_results
from modules.hash_utils import (
    hash_password,
    identify_hash
)


def clear():

    os.system("cls" if os.name == "nt" else "clear")


def banner():

    clear()

    print("=" * 60)
    print("VEXA PASSWORD AUDIT TOOLKIT")
    print("=" * 60)
    print()


while True:

    banner()

    print("[1] Analyze Password")
    print("[2] Calculate Entropy")
    print("[3] Generate Password")
    print("[4] Dictionary Check")
    print("[5] Password Statistics")
    print("[6] Export CSV")
    print("[7] Export JSON")
    print("[8] HTML Report")
    print("[9] PDF Report")
    print("[10] Hash Password")
    print("[11] Identify Hashes")
    print("[12] Exit")

    choice = input("\nSelect Option: ")

    if choice == "1":

        analyze_password()

    elif choice == "2":

        calculate_entropy()

    elif choice == "3":

        generate_password()

    elif choice == "4":

        dictionary_check()

    elif choice == "5":

        password_statistics()

    elif choice == "6":

         export_csv(analysis_results)

    elif choice == "7":

        export_json(analysis_results)

    elif choice == "8":

        create_html(analysis_results)

    elif choice == "9":

        create_pdf(analysis_results)

    elif choice == "10":

        hash_password()

    elif choice == "11":

        identify_hash()

    elif choice == "12":

        print("\nGoodbye.\n")

        break

    else:

        print("\nInvalid selection.\n")
        input("Press Enter...")