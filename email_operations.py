# email_operations.py
from auth import gmail_authenticate


def search_messages(service, query):
    result = service.users().messages().list(userId="me", q=query).execute()
    messages = []
    if "messages" in result:
        messages.extend(result["messages"])
        print(f"Found {len(messages)} matching emails for query: {query}")
    else:
        print(f"No matching emails found for query: {query}")
    while "nextPageToken" in result:
        page_token = result["nextPageToken"]
        result = (
            service.users()
            .messages()
            .list(userId="me", q=query, pageToken=page_token)
            .execute()
        )
        if "messages" in result:
            messages.extend(result["messages"])
            print(f"Found {len(messages)} matching emails for query: {query}")
    return messages


def delete_messages(service, messages):
    for message in messages:
        service.users().messages().delete(userId="me", id=message["id"]).execute()


def clean_inbox(
    sender=None,
    subject=None,
    keywords=None,
    labels=["INBOX", "CATEGORY_PERSONAL", "CATEGORY_PROMOTIONS", "CATEGORY_SOCIAL"],
):
    service = gmail_authenticate()
    queries = []
    if sender:
        if isinstance(sender, list):
            for s in sender:
                queries.append(f"from:{s}")
        else:
            queries.append(f"from:{sender}")
    if subject:
        queries.append(f'subject:"{subject}"')
    if keywords:
        for keyword in keywords:
            queries.append(f'"{keyword}"')
    query = " OR ".join(queries)
    for label in labels:
        messages_to_delete = search_messages(service, f"{query} label:{label}")
        delete_messages(service, messages_to_delete)


def delete_emails(
    sender=None,
    subject=None,
    keywords=None,
    labels=["INBOX", "CATEGORY_PERSONAL", "CATEGORY_PROMOTIONS", "CATEGORY_SOCIAL"],
):
    clean_inbox(sender=sender, subject=subject, keywords=keywords, labels=labels)
