# Plik email.txt zawiera surową treść e-maila. Napisz program, który używa wyrażeń regularnych, aby wyciągnąć i wypisać:
# adres email nadawcy
# adres email odbiorcy
# temat wiadomości
# treść wiadomości

# Dla każdego z powyższych poleceń zdefiniuj oddzielną funkcję (patrz niżej), która zwraca wartość odczytaną z maila. Umieść funkcje w osobnym module o nazwie emails.
# email_sender()
# email_recipient()
# email_subject()
# email_body()

from emails import email_sender, email_recipient, email_subject, email_body

with open('email.txt', 'r', encoding='utf-8') as f:
    email_text = f.read()

print("Nadawca:", email_sender(email_text))
print("Odbiorca:", email_recipient(email_text))
print("Temat:", email_subject(email_text))
print("Treść:\n", email_body(email_text))
