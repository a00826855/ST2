from turtle import *
import random
from random import randrange
from freegames import square, vector

# parametros iniciales
food = vector(0, 0)
snake = [vector(10, 0)] # snake es una lista de vectores (direcciones)
aim = vector(0, -10)
# lista de colores
colores = ['green', 'pink', 'yellow', 'blue', 'orange']
# escoje color aleatorio
c1 = random.choice(colores)
c2 = random.choice(colores)        

def change(x, y):
    # cambia direccion del snake
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    # asegura que el jugador se quede dentro del area del juego
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    # mueve al snake 1 segmento en la direccion que esta apuntando 
    "Move snake forward one segment."
    head = snake[-1].copy() # regresa copia del vector
    head.move(aim)

    if not inside(head) or head in snake:
        # primer cuadro del snake se pone rojo se sale del area del juego 
        square(head.x, head.y, 9, 'red')
        update()
        return

     # agrega un cuadro al snake cada vez que come uno
    snake.append(head)

    if head == food:
        print('Snake:', len(snake)) # imprime longitud del snake
        
        # determina posicion nueva del nuevo food, aleatoria dentro del rango
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)
        

    clear()
        
    for body in snake:
        # color del snake es aleatorio
        square(body.x, body.y, 9, c1) 

    #color de la comida del snake es aleatorio
    square(food.x, food.y, 9, c2)
    update()
    
    # velocidad del snake, entre mas grande mas lento
    ontimer(move, 100) 
    
        
# determina el tamano del area del juego
setup(420, 420, 370, 0)

#esconde el turtle 
hideturtle()

tracer(False)

#lee lo que teclea el usuario
listen()

# uso de las arrowkeys por el usuario
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
