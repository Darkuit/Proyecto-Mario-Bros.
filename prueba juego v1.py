from tkinter import *
import time
def Crear_Ventana():
    ventan=Tk()
    ventan.title('Game')
    return ventan

x= Crear_Ventana()
def key(event):
    overlaps = canvas.find_overlapping(1281,0,1279,721)
    overlaps2=canvas.find_overlapping(-1,0,1,721)
    print(overlaps)
    print(overlaps2)
    if event.char=='a':
        if 1 in overlaps2:
            canvas.move(mario, 1230, 0)
        canvas.move(mario, -10, 0)
    elif event.char== 'd':
        if len(overlaps)>0:
            canvas.move(mario,-1230,0) 
        canvas.move(mario, 10, 0)
    elif event.char=='x':
        estado='saltando'
        coords1=canvas.coords(mario)[1]
        coordsor=coords1
        print(coords1)
        coords2=coords1-500
        while coords1>coords2:    #Bucle donde empieza el salto
            time.sleep(0.1)
            canvas.move(mario,0,-50)
            print(canvas.coords(mario)[1])
            coords1-=50
        estado='en caída'
        time.sleep(1)
        while coords1<coordsor:   #Bucle de la caída
            time.sleep(0.1)
            canvas.move(mario, 0, 10)
            print(canvas.coords(mario)[1])
            coords1+=10
        
canvas= Canvas(x, width=1280, height=720)
canvas.bind('<Key>', key)
estado = None
canvas.focus_set()
canvas.pack()
mario= canvas.create_rectangle(0,620,101,720, fill='red')




x.mainloop()
