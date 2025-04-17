"""
Inbox Zero Bot

This script simulates an intelligent email organizer. It processes a list of 
email subject lines, detects key terms, and categorizes each subject into folders 
such as Finance, Meetings, Security, or General.

It uses keyword matching to group related messages and outputs a clean inbox summary 
to help users prioritize and sort emails.

Author: Wilson Villon
"""


# Assigns a category to an email subject based on keywords
def get_category(subject_line):
    subject_cat = {
        "invoice": "Finance",
        "payment": "Finance",
        "meeting": "Meetings",
        "schedule": "Meetings",
        "password": "Security",
        "login": "Security",
        "announcement": "General",
        "follow-up": "General",
        "report": "Finance",
        "deadline": "General"
        }

    # Normalize subject line to lowercase for case-insensitive matching
    subject_line_lower = subject_line.lower()

    # Search for a keyword match
        if keyword in subject_line_lower:
            return subject_cat[keyword]

    # Fallback category if no keywords are found
    return "General"


# Simulated inbox: list of email subject lines
email_subjects = [
    "Invoice for April 2025",
    "Schedule update for project",
    "Meeting recap: Q2 Goals",
    "Password reset request",
    "Final payment reminder",
    "Client follow-up needed",
    "Login attempt alert",
    "Weekly team meeting",
    "Expense report submission",
    "Upcoming project deadline"
]


# Dictionary to group subjects by category
grouped_emails = {}

# Loop through each subject and categorize it
for subject in email_subjects:
    category = get_category(subject)

    # Create the category list if it doesn't exist
    if category not in grouped_emails:
        grouped_emails[category] = []

    # Add the subject to the appropriate category
    grouped_emails[category].append(subject)


# Display the organized summary
print("\nInbox Summary:")
for category, subjects in grouped_emails.items():
    print(f"{category}:")
    for subject in subjects:
        print(f" - {subject}")
