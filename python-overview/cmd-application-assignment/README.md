Command-Line Application 

A simple console program that lets users choose operations from a menu, enter input, and get results. The program repeats until the user chooses to exit.

Features

Palindrome Check – Checks if the input reads the same backward and forward.

Lowercase Check – Verifies all characters are lowercase.

Digit Check – Validates that all characters are digits.

Length Check – Checks if the input length is above a threshold.

Empty Check – Detects if the string is empty.

Exit – Closes the program.

How It Works

The program displays a menu.

The user selects an operation (1–6).

The user enters text to analyze.

The program prints the result.

The menu repeats until “Exit” is chosen.

Error Handling

Invalid menu choices

Basic try/except around user input

Run the Program
python main.py

Structure
cmd-application-assignment/
│── README.md
└── main.py