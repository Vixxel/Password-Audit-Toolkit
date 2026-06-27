import csv
import os
from datetime import datetime


def export_csv(results):

    if not results:

        print("\nNo password analysis available.")

        input("\nPress Enter...")
        return

    os.makedirs(
        "exports",
        exist_ok=True
    )

    filename = os.path.join(
        "exports",
        f"password_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Password",
                "Length",
                "Score",
                "Strength"
            ]
        )

        writer.writeheader()

        for row in results:

            writer.writerow(row)

    print(f"\nCSV exported:\n{filename}")

    input("\nPress Enter...")

import json


def export_json(results):

    if not results:

        print("\nNo password analysis available.")

        input("\nPress Enter...")
        return

    os.makedirs(
        "exports",
        exist_ok=True
   )

    filename = os.path.join(
        "exports",
        f"password_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print(f"\nJSON exported:\n{filename}")

    input("\nPress Enter...")