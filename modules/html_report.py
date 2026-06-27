from datetime import datetime
import os


def create_html(results):

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
        f"password_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    )
    html = """
<html>
<head>
<title>Password Audit Report</title>
<style>

body{

font-family:Arial;
background:#f5f5f5;

}

table{

border-collapse:collapse;
width:100%;

}

th,td{

border:1px solid black;
padding:8px;

}

th{

background:#222;
color:white;

}

</style>
</head>

<body>

<h1>Password Audit Report</h1>

<table>

<tr>

<th>Password</th>
<th>Length</th>
<th>Score</th>
<th>Strength</th>

</tr>

"""

    for row in results:

        html += f"""

<tr>

<td>{row['Password']}</td>

<td>{row['Length']}</td>

<td>{row['Score']}</td>

<td>{row['Strength']}</td>

</tr>

"""

    html += """

</table>

</body>

</html>

"""

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    print(f"\nHTML report created:\n{filename}")

    input("\nPress Enter...")