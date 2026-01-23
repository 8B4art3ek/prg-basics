# Klasa zawarta w socialmedia.py modeluje profil w mediach społecznościowych, pozwalając użytkownikom dodawać posty i wyświetlać ich oś czasu. Dodaj do klasy metodę display_timeline(self), która wypisuje imię użytkownika wraz z listą postów. Ponumeruj elementy listy. Następnie napisz program, który tworzy użytkownika 'johndoe'. Dodaj następujące posty. Wypisz imię użytkownika i posty.

# Hello, world!
# Had a great day at the park!
# What's up, Natalie? How are you?


class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"Użytkownik {self.username}:")
        for i, post in enumerate(self.posts):
            print(f"{i+1}. {post}")

def main():
    profile1 = SocialMediaProfile("johndoe")
    profile1.add_post("Hello, world!")
    profile1.add_post("Had a great day at the park!")
    profile1.add_post("What's up, Natalie? How are you?")
    profile1.display_timeline()

if __name__ == "__main__":
    main()
