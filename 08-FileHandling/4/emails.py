import re

def email_sender(email_text):
    for line in email_text.splitlines():
        if line.startswith("From:"):
            match = re.search(r'<([^>]+)', line)
            if match:
                return match.group(1)
    return None

def email_recipient(email_text):
    for line in email_text.splitlines():
        if line.startswith("To:"):
            match = re.search(r'<([^>]+)', line)
            if match:
                return match.group(1)
    return None

def email_subject(email_text):
    for line in email_text.splitlines():
        if line.startswith("Subject:"):
            return line[len("Subject:"):].strip()
    return None

def email_body(email_text):
    """
    Zwraca treść wiadomości.
    Zakładamy, że treść zaczyna się po pustej linii po nagłówkach.
    """
    parts = email_text.split("\n\n", 1)  # dzielimy tekst na nagłówki i resztę
    if len(parts) > 1:
        return parts[1].strip()  # zwracamy część po nagłówkach
    return None