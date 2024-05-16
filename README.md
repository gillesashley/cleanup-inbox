# Email Cleanup Tool

This Python project provides a tool to clean up your Gmail inbox by deleting emails based on specific filters such as sender, subject, and keywords.

## Prerequisites

Before running this project, you need to have the following:

- Python 3.x installed on your system
- Google API Client Library for Python (`google-api-python-client`)
- Google Authentication Library for Python (`google-auth-oauthlib`)
- A Google Cloud Platform project with the Gmail API enabled
- A client secret file (`client_secret_*.json`) downloaded from the Google Cloud Console

## Installation

1. Clone the repository or download the project files.
2. Install the required Python packages by running: "pip install -r requirements.txt"
3. Download the client secret file from the Google Cloud Console and place it in the project directory.

## Usage

1. Open the `auth.py` file and replace the line:

````python
"client_secret_*****************************************.apps.googleusercontent.com.json"

with the path to your client secret file.

2. In the senders.py file, modify the senders list to include the email addresses from which you want to delete emails.
3. Run the main.py script:
    python main.py

4. The first time you run the script, it will prompt you to authenticate with your Google account and grant the required permissions.
5. After successful authentication, the script will delete emails from your Gmail inbox based on the senders specified in the senders list. You can also filter emails by subject and keywords by modifying the main.py script.


Here's the README content that you can copy and paste into your project's README file:
Copy code# Email Cleanup Tool

This Python project provides a tool to clean up your Gmail inbox by deleting emails based on specific filters such as sender, subject, and keywords.

## Prerequisites

Before running this project, you need to have the following:

- Python 3.x installed on your system
- Google API Client Library for Python (`google-api-python-client`)
- Google Authentication Library for Python (`google-auth-oauthlib`)
- A Google Cloud Platform project with the Gmail API enabled
- A client secret file (`client_secret_*.json`) downloaded from the Google Cloud Console

## Installation

1. Clone the repository or download the project files.
2. Install the required Python packages by running:
pip install google-api-python-client google-auth-oauthlib
Copy code
3. Download the client secret file from the Google Cloud Console and place it in the project directory.

## Usage

1. Open the `auth.py` file and replace the line:

```python
"client_secret_785515207647-5urus64tfih8cqpk8sa12l6jb3vai0vb.apps.googleusercontent.com.json"
with the path to your client secret file.

In the senders.py file, modify the senders list to include the email addresses from which you want to delete emails.
Run the main.py script:

Copy codepython main.py

The first time you run the script, it will prompt you to authenticate with your Google account and grant the required permissions.
After successful authentication, the script will delete emails from your Gmail inbox based on the senders specified in the senders list. You can also filter emails by subject and keywords by modifying the main.py script.

File Structure

```auth.py```: Contains the gmail_authenticate() function for authenticating with the Gmail API.
```email_operations.py```: Defines functions for searching, deleting, and cleaning up emails in the Gmail inbox.
```senders.py```: Stores the list of email addresses (senders) from which you want to delete emails.
```main.py```: The main script that calls the delete_emails function with the specified filters.

Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
````
