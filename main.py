from email_operations import delete_emails
from senders import senders

if __name__ == "__main__":
    # Set your desired filters
    subject = None
    keywords = []

    delete_emails(sender=senders, subject=subject, keywords=keywords)
