import turtle

def draw_square(length):
    """Rysuje kwadrat o boku length."""
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(length):
    """
    Rysuje trójkąt równoboczny (który jest też równoramienny).
    Przyjmuje tylko jeden parametr, więc zakładamy równe boki.
    """
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)  # Kąt zewnętrzny dla trójkąta to 120 stopni

def draw_rectangle(length_a, length_b):
    """Rysuje prostokąt o bokach a i b."""
    for _ in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)