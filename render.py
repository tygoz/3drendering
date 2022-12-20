import tkinter,time,threading
from sympy import symbols, solve, Eq
gravity = tkinter.Tk()
canvas = tkinter.Canvas(gravity, width=320,height=320)
canvas.pack()
def create_circle(classy,scale,pos,color):
    pos[0] += scale
    pos[1] -= scale
    return classy.create_oval(pos,pos[::-1],width=1,fill=color)

cord = [{'x':200,'y':200},{'x':300,'y':300}]
cord_inside = [{'x':cord[0]['x']+2,'y':cord[0]['y']+2}, {'x':cord[1]['x']-2, 'y':cord[1]['y']-2}]

square = canvas.create_rectangle(cord[0]['x'],cord[0]['y'], cord[1]['x'], cord[1]['y'], outline = 'black',width=2)
ins_square = canvas.create_rectangle(cord_inside[0]['x']+10,cord_inside[0]['y']+10, cord_inside[1]['x']-10, cord_inside[1]['y']-10, outline = 'black',width=2)
gopos = {'x':320,'y':320}


#draw 3d lines
#above-left
if gopos['x'] < (cord[0]['x'] + cord[1]['x']) / 2 and gopos['y'] < (cord[0]['y'] + cord[1]['y'])/2:
    line5 = canvas.create_line(cord[0]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line6 = canvas.create_line(cord[0]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line8 = canvas.create_line(cord[1]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')

#above-right
elif gopos['x'] > (cord[0]['x'] + cord[1]['x']) / 2 and gopos['y'] < (cord[0]['y'] + cord[1]['y'])/2:
    line6 = canvas.create_line(cord[0]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line7 = canvas.create_line(cord[1]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line8 = canvas.create_line(cord[1]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')

#under-left
elif gopos['x'] < (cord[0]['x'] + cord[1]['x']) / 2 and gopos['y'] > (cord[0]['y'] + cord[1]['y'])/2:
    line5 = canvas.create_line(cord[0]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line6 = canvas.create_line(cord[0]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line7 = canvas.create_line(cord[1]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')

#under-right
elif gopos['x'] > (cord[0]['x'] + cord[1]['x']) / 2 and gopos['y'] > (cord[0]['y'] + cord[1]['y'])/2:
    line5 = canvas.create_line(cord[0]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line7 = canvas.create_line(cord[1]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')
    line8 = canvas.create_line(cord[1]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')


    
#line5 = canvas.create_line(cord[0]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='black')
#line6 = canvas.create_line(cord[0]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=5,fill='black')
#line7 = canvas.create_line(cord[1]['x'],cord[1]['y'],gopos['x'],gopos['y'],width=1,fill='green')
#line8 = canvas.create_line(cord[1]['x'],cord[0]['y'],gopos['x'],gopos['y'],width=1,fill='black')
#test = create_circle(canvas,10,[10,20],'red')
gravity.mainloop()
