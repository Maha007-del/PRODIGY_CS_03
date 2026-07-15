# PRODIGY_CS_03
A Python and Tkinter-based GUI application that checks password strength in real time using factors like length, uppercase, lowercase, numbers, and special characters. It provides instant feedback and suggestions to help users create stronger and more secure passwords.
GUI-Based Password Complexity Checker

Key Features

- 🔐 Verifies password length (minimum 8 characters, 12+ for enhanced security)
- 🔠 Detects uppercase letters (A–Z)
- 🔡 Detects lowercase letters (a–z)
- 🔢 Identifies numeric digits (0–9)
- ✨ Checks for special characters (e.g., !@#$%^&*)
- 🎨 Displays password strength using color indicators:
  - 🔴 Weak
  - 🟠 Medium
  - 🟢 Strong
- 💡 Provides real-time suggestions to improve password security

Working Process

1. The user enters a password into the input field.
2. The application validates the password against multiple security rules using regular expressions.
3. A strength score is generated based on the satisfied conditions.
4. The strength label updates instantly with an appropriate color.
5. Suggestions are displayed for any missing security requirements.

Code Overview

- "re.search()" – Uses regular expressions to validate password criteria.
- "check_strength()" – Calculates the password strength score and updates the interface.
- "entry.bind("<KeyRelease>")" – Refreshes the analysis whenever the user types.
- "result_label" – Displays the current password strength.
- "tips_label" – Shows recommendations to create a stronger password.

Technologies Used

- Python 3
- Tkinter (GUI Framework)
- Regular Expressions ("re" module)

Getting Started

1. Install Python 3 on your system.
2. Download or clone the project repository.
3. Run the Python file to launch the Password Complexity Checker.

Sample Results

🔴 Weak Password

Input: "hello"

Missing: Minimum length, number, and special character.

Result: Weak

🟠 Medium Password

Input: "Welcome@"

Missing: Number and recommended password length.

Result: Medium

🟢 Strong Password

Input: "P@ssKey2026"

Missing: None

Result: Strong
