# Password Strength Analyzer

This is a Python project developed for the CYB333 Security Automation course. It analyzes the strength of user-provided passwords and gives suggestions for improvement.

## Project Objectives

- Evaluate password strength based on standard security criteria.
- Detect weak or commonly used passwords from a customizable list.
- Identify repeated characters and simple sequences (e.g., "aaaa", "1234").
- Help users create stronger passwords by providing clear feedback.

## Features

- Length check (minimum 8 characters).
- Checks for uppercase and lowercase letters.
- Checks for numerical digits.
- Checks for special characters.
- Detection of repeated patterns or simple sequences.
- Validation against a list of weak passwords (loaded from `weak_passwords.txt`).
- Feedback for each failed condition.

## How to Run

1. Make sure you have Python installed (version 3.6 or higher).
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code or any terminal.
4. Make sure the `weak_passwords.txt` file is in the same folder as the script.
5. Run the script using this command:

```bash
python password_analyzer.py
```

6. When prompted, enter a password to analyze.

## Requirements

- No external libraries required (only Python's built-in `re` module).

## Example Output

```
=== Password Strength Analyzer ===
Enter a password to check: abc123

Password Strength: Weak
Suggestions to improve your password:
- Use at least 8 characters.
- Use a mix of uppercase and lowercase letters.
- Include at least one special character (!, @, #, etc.).
- This is a very common and weak password. Avoid using it.
- Avoid repeated patterns or simple sequences like 'aaa' or '1234'.
```

## Notes

- You can expand the list of weak passwords by editing the `weak_passwords.txt` file.
- Avoid using easily guessable passwords or repeating patterns.
- Passwords that meet all criteria and avoid known patterns are marked as "Strong".

## Author

This project was developed by Fernanda O. for the final project in the CYB333 Security Automation course.