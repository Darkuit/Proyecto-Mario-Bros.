from tkinter import *
import time
def Crear_Ventana():
    ventan=Tk()
    ventan.title('Game')
    return ventan

x= Crear_Ventana()
def moveupm():
    global coords1m
    global coords2m
    global estado
    global coords3m
    coords1m=int(canvas.coords(mario)[1])
    coordsmariox1= int(canvas.coords(mario)[0])
    if coords1m == coordsplat1y2 and coordsmariox1 <= coordsplat1x2:
        time.sleep(0.01)
        movedownm()
        return None
    elif coords1m<=coords2m:
        time.sleep(0.01)
        movedownm()
        return None
    else:
        x.after(1, moveupm)
        canvas.move(mario, 0, -2)
def movedownm():
    print('pene')
    global coords1m
    global coords3m
    global estado
    coords1m=int(canvas.coords(mario)[1])
    coordsmarioy2=int(canvas.coords(mario)[3])
    coordsmariox1= int(canvas.coords(mario)[0])
    if coordsmarioy2== coordsplat1y1 and coordsmariox1 <= coordsplat1x2:
        return None
    elif coords1m>= coords3m:
        estado='Suelo'
        return None
    else:
        x.after(1,movedownm)
        canvas.move(mario, 0, 2)
def jumpm(event):
    canvas.bind('<x>', ignore)
    global coords1m #coordenadas que van a cambiar
    global coords2m #coordenadas de referencia hacia arriba
    global coords3m #coordenadas originales
    global estado
    coords1m=int(canvas.coords(mario)[1])
    coords2m=coords1m-200
    coords3m=coords1m
    moveupm()
    x.after(30,bindit)

def bindit():
    canvas.bind('<x>', jumpm)
def ignore(event):
    return 'break'

def fallmplat1():
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2 <720 and coordsmarioy2 >717:
        return None
    else:
        x.after(1,fallmplat1)
        canvas.move(mario, 0, 2)
        

def keym(event):
    overlaps = canvas.find_overlapping(1281,0,1279,721)
    overlaps2=canvas.find_overlapping(-10,0,-1,721)
    print(overlaps)
    print(overlaps2)
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if event.char=='a':
        if coordsmariox1==coordsplat1x2 and (not((coordsmarioy1>coordsplat1y2 and coordsmarioy2 >coordsplat1y2) or (coordsmarioy1< coordsplat1y1 and coordsmarioy2< coordsplat1y1))):
            return None
        if 2 in overlaps2:
            canvas.move(mario, 1230, 0)   
        canvas.move(mario, -10, 0)
    elif event.char== 'd':
        if coordsmarioy2==coordsplat1y1 and coordsmariox1 > coordsplat1x2:
            fallmplat1()
        if len(overlaps)>0:
            canvas.move(mario,-1230,0) 
        canvas.move(mario, 10, 0)

canvas= Canvas(x, width=1280, height=720)
estado= 'Suelo'
if estado =='Suelo':
    print('holi')
canvas.bind('<a>', keym)
canvas.bind('<d>', keym)
canvas.bind('<x>', jumpm)
canvas.focus_set()
canvas.pack()
plat1= canvas.create_rectangle(1,595, 400, 620, fill= 'blue')
mario= canvas.create_rectangle(0,670,51,720, fill='red')
coordsplat1x1=int(canvas.coords(plat1)[0])
coordsplat1y1=int(canvas.coords(plat1)[1])+1
coordsplat1x2=int(canvas.coords(plat1)[2])-2
coordsplat1y2=int(canvas.coords(plat1)[3])



x.mainloop()
