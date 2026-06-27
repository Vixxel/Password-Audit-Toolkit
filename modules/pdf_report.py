from datetime import datetime
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors


def create_pdf(results):

    if not results:

        print("\nNothing to export.")

        input("\nPress Enter...")
        return

    os.makedirs(
        "exports",
        exist_ok=True
    )

    filename = os.path.join(
        "exports",
        f"password_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )
    pdf = SimpleDocTemplate(filename)

    data = [

        [

            "Password",

            "Length",

            "Score",

            "Strength"

        ]

    ]

    for row in results:

        data.append(

            [

                row["Password"],

                row["Length"],

                row["Score"],

                row["Strength"]

            ]

        )

    table = Table(data)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND",(0,0),(-1,0),colors.grey),

                ("TEXTCOLOR",(0,0),(-1,0),colors.whitesmoke),

                ("GRID",(0,0),(-1,-1),1,colors.black),

                ("BACKGROUND",(0,1),(-1,-1),colors.beige)

            ]

        )

    )

    pdf.build([table])

    print(f"\nPDF report created:\n{filename}")

    input("\nPress Enter...")