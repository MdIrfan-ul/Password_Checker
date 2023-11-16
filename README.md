# PasswordChecker
## Overview
The PasswordChecker project is a Python script that allows users to check the security of their passwords by leveraging the Pwned Passwords API. This tool utilizes the `request` module for making HTTP requests, `hashlib` for hashing passwords, and the Pwned Passwords database to determine if a password has been previously leaked or compromised.
## Features
* **Password Security Check:** The script allows users to input a password and checks its security against the Pwned Passwords database.

* **Hashing:** Passwords are securely hashed using the SHA-1 hashing algorithm before being sent to the Pwned Passwords API. This ensures that the actual password is never transmitted over the network.

* **Pwned Passwords API Integration:** The script queries the Pwned Passwords API to determine if the provided password has been exposed in any known data breaches.
## Prerequisites
* Python 3.x

* `requests` module: Install using `pip install requests`
## How to Use
* Clone the repository:```https://github.com/MdIrfan-ul/PasswordChecker.git```
* Navigate to the project directory:```cd Password_Checker```
* Run the script: ```python password_checker.py```
## Acknowledgments
* This project makes use of the Pwned Passwords API. For more information, visit [haveibeenpwned](https://haveibeenpwned.com/Passwords.)
## Disclaimer
This tool is meant for educational purposes only. Use it responsibly and avoid using it with sensitive passwords.
## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.