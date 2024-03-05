# fair_billing

Log Parser Script
This script is designed to parse log files and calculate session durations for each user.

Usage
Clone the Repository

bash
git clone https://github.com/your-username/log-parser.git
Navigate to the Directory

bash
cd log-parser
Run the Script

Run the script by providing the path to the log file as a command-line argument:

php
Copy code
python script.py <file_path>
Replace <file_path> with the path to your log file.

View Results

The script will output the session durations for each user.

Requirements
Python 3.x
Notes
The log file should follow a specific format for the script to work correctly. Each line in the log file should contain timestamp, username, and action (e.g., Start or End).
Invalid lines or lines with repeated characters in the username are skipped during parsing.
