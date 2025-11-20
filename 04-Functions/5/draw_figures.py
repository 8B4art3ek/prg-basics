import turtle
import figures

# Setup ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# TRIK: Przypisujemy moduł turtle do zmiennej pen.
# Dzięki temu 'pen.forward' to to samo co 'turtle.forward'.
# To rozwiązuje problem rozdzielenia sterowania między plikami.
pen = turtle
pen.speed(8)  # Żeby nie zasnąć przy rysowaniu

# --- 1. KWADRATY ---
# Pierwszy kwadrat
pen.penup()
pen.goto(-150, 150)
pen.pendown()
figures.draw_square(50)

# Drugi kwadrat (inne miejsce)
pen.penup()
pen.goto(-50, 150)
pen.pendown()
figures.draw_square(50)

# --- 2. TRÓJKĄTY ---
# Pierwszy trójkąt
pen.penup()
pen.goto(-150, 0)
pen.pendown()
figures.draw_triangle(60)

# Drugi trójkąt
pen.penup()
pen.goto(-50, 0)
pen.pendown()
figures.draw_triangle(60)

# --- 3. PROSTOKĄTY ---
# Pierwszy prostokąt
pen.penup()
pen.goto(-150, -150)
pen.pendown()
figures.draw_rectangle(80, 40)

# Drugi prostokąt
pen.penup()
pen.goto(-50, -150)
pen.pendown()
figures.draw_rectangle(80, 40)

# Ukrycie żółwia i pętla kończąca
pen.hideturtle()
window.mainloop()