# Password Audit Toolkit

A Python-based cybersecurity toolkit that analyzes password strength, calculates password entropy, detects dictionary passwords, generates secure passwords, identifies password hashes, and produces professional audit reports.

## Features

* Password Strength Analysis
* Password Entropy Calculator
* Secure Password Generator
* Dictionary Password Detection
* Password Statistics Analyzer
* MD5 Hash Generator
* SHA-1 Hash Generator
* SHA-256 Hash Generator
* SHA-512 Hash Generator
* Hash Identification
* CSV Export
* JSON Export
* HTML Report Generation
* PDF Report Generation
* Colorized Terminal Interface

## Requirements

* Python 3.10+
* Windows

## Installation

```bash
git clone https://github.com/Vixxel/Password-Audit-Toolkit.git

cd Password-Audit-Toolkit

pip install -r requirements.txt

python main.py
```

## requirements.txt

```text
reportlab>=4.0.0
colorama>=0.4.6
```

## Project Structure

```text
Password-Audit-Toolkit/

main.py

modules/
├── password_strength.py
├── entropy.py
├── password_generator.py
├── dictionary_check.py
├── statistics.py
├── hash_utils.py
├── export_utils.py
├── html_report.py
├── pdf_report.py
└── session.py

wordlists/
├── common_passwords.txt
├── passwords.txt

exports/

requirements.txt
README.md
LICENSE
CHANGELOG.md
```

## Future Features

* Excel (.xlsx) Export
* Password Policy Auditor
* Password Reuse Detection
* Password Breach Checker
* Organization Password Security Score
* Interactive Dashboard
* Password Audit Sessions
* Password History Tracking
* Password Compliance Reports
* Automatic Wordlist Detection
* Charts & Graphs
* NIST Password Compliance Checks

## Author

Vladimir Acosta
Cybersecurity & Digital Forensics
