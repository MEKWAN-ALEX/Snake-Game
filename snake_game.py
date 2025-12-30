import tkinter
import random

ROWS=25
COLS=25
TILE_SIZE=25

WINDOW_WIDTH=TILE_SIZE*COLS
WINDOW_HEIGHT=TILE_SIZE*ROWS

class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        


#Game Window
window=tkinter.Tk()
window.title("Snake Game")
window.resizable(False,False)

canvas=tkinter.Canvas(window,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,bg="Black",borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()

#Center Window
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x= int((screen_width/2)-(window_width/2))
window_y= int((screen_height/2)-(window_height/2))
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

#initialize game
Snake=Tile(5*TILE_SIZE,5*TILE_SIZE)#single head , and also the position of head
Food=Tile(15*TILE_SIZE,15*TILE_SIZE)
snake_body=[]
velocityX=0
velocityY=0
game_over=False
Score=0

def change_Direction(e):
    global velocityX,velocityY,game_over
    if game_over:
        return

    if e.keysym=="Left" and velocityX!=1:
        velocityX=-1
        velocityY=0
    elif e.keysym=="Right" and velocityX!=-1:
        velocityX=1
        velocityY=0
    elif e.keysym=="Up" and velocityY!=1:
        velocityX=0
        velocityY=-1
    elif e.keysym=="Down" and velocityY!=-1:
        velocityX=0
        velocityY=1

def move():
    global snake_body,Snake,Food,game_over,Score

    if game_over:
        return
    if Snake.x<0 or Snake.x >= WINDOW_WIDTH or Snake.y <0 or Snake.y>=WINDOW_HEIGHT:
        game_over=True
        return
    for tile in snake_body:
        if tile.x==Snake.x and tile.y==Snake.y:
            game_over=True
            return

    if (Snake.x==Food.x and Snake.y==Food.y):
        snake_body.append(Tile(Food.x,Food.y))
        Food.x=random.randint(0,COLS-1)*TILE_SIZE
        Food.y=random.randint(0,ROWS-1)*TILE_SIZE
        Score+=1

    for i in range(len(snake_body)-1,-1,-1):
        tile=snake_body[i]
        if i==0:
            tile.x=Snake.x
            tile.y=Snake.y
        else:
            prev_tile=snake_body[i-1]
            tile.x=prev_tile.x
            tile.y=prev_tile.y



    Snake.x+=velocityX*TILE_SIZE
    Snake.y+=velocityY*TILE_SIZE
def Draw():
    global Snake,Food,snake_body,game_over,Score
    move()
    canvas.delete("all")
    #Draw Food
    canvas.create_rectangle(Food.x,Food.y,Food.x+TILE_SIZE,Food.y+TILE_SIZE,fill='Red')

    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x+TILE_SIZE,tile.y+TILE_SIZE,fill='lime green')
    #Draw Snake
    canvas.create_rectangle(Snake.x,Snake.y,Snake.x+TILE_SIZE,Snake.y+TILE_SIZE,fill='lime green')
    window.after(120,Draw) 

    if game_over:
        canvas.create_text(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,fill='white',font='Arial 20',text=f'Game Over: {Score}')
    else:
        canvas.create_text(30,20,text=f"Score :{Score}",fill='white',font='Arial 10')

Draw()

window.bind("<KeyRelease>",change_Direction)
window.mainloop()