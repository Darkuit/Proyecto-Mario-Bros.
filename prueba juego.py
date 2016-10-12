from tkinter import *
import time
import random
def Crear_Ventana():
    ventan=Tk()
    ventan.title('Game')
    return ventan


def moveupm():
    global coords1m
    global coords2m
    global estadokoopa1
    global coords3m
    global spritemario
    global mseconds
    
    coords1m=int(canvas.coords(mario)[1])
    coordsmariox1= int(canvas.coords(mario)[0])
    coordsmariox2= int(canvas.coords(mario)[2])
    if coords1m == coordsplat1y2 and coordsmariox1 <= coordsplat1x2:
        if estadokoopa1=='creado':
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1=int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if coordskoopa1y2==coordsplat1y1 and coordskoopa1x1<coordsplat1x2:
                overlaps=canvas.find_overlapping(coordskoopa1x1, coordskoopa1y2, coordskoopa1x2, coordsplat1y2+5)
                if len(overlaps)>4:
                    Koopa1_flip()
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m == coordsplat2y2 and coordsmariox2 >= coordsplat2x1:
        if estadokoopa1=='creado':
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1=int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if coordskoopa1y2==coordsplat2y1 and coordskoopa1x2>coordsplat2x1:
                overlaps=canvas.find_overlapping(coordskoopa1x1, coordskoopa1y2, coordskoopa1x2, coordsplat2y2+5)
                if len(overlaps)>4:
                    Koopa1_flip()
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m==coordsplat3y2 and coordsmariox1<=coordsplat3x2:
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m== coordsplat4y2 and coordsmariox2>=coordsplat4x1:
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m==coordsplatcentroy2 and (coordsmariox1<=coordsplatcentrox2 and coordsmariox2>=coordsplatcentrox1):
        if estadokoopa1=='creado':
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1=int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if coordskoopa1y2==coordsplatcentroy1 and coordskoopa1x1<coordsplatcentrox2 and coordskoopa1x2>coordsplatcentrox1:
                overlaps=canvas.find_overlapping(coordskoopa1x1, coordskoopa1y2, coordskoopa1x2, coordsplatcentroy2+5)
                if len(overlaps)>4:
                    Koopa1_flip()
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m==coordsplat5y2 and coordsmariox1<=coordsplat5x2:
      time.sleep(0.01)
      mseconds=100
      movedownm()
      return None
    elif coords1m==coordsplat6y2 and coordsmariox2>=coordsplat6x1:
      time.sleep(0.01)
      mseconds=100
      movedownm()
      return None
    elif coords1m<=coords2m:
        time.sleep(0.01)
        movedownm()
        return None
    else:
        x.after(2, moveupm)
        canvas.move(mario, 0, -2)
        canvas.move(spritemario, 0, -2)
def movedownm():
    global coords1m
    global coords3m
    global estadomario
    global spritemario
    global estadokoopa1
    coords1m=int(canvas.coords(mario)[1])
    coordsmarioy2=int(canvas.coords(mario)[3])
    coordsmariox1= int(canvas.coords(mario)[0])
    coordsmariox2= int(canvas.coords(mario)[2])
    
    if estadokoopa1=='creado':
       coordskoopa1x1=int(canvas.coords(koopa1)[0])
       coordskoopa1y1=int(canvas.coords(koopa1)[1])
       coordskoopa1x2=int(canvas.coords(koopa1)[2])
       coordskoopa1y2=int(canvas.coords(koopa1)[3])
       overlaps=canvas.find_overlapping(coordskoopa1x1,coordskoopa1y1,coordskoopa1x2,coordskoopa1y2)
       if coordskoopa1y2>537 and coordskoopa1y2<=540:
           if ((coordsmarioy2-1>=coordskoopa1y1-5 and coordsmarioy2<=coordskoopa1y1)) and len(overlaps)>=3:
               print('splat')
               Koopa1_flip()
               mbounce()
               return None
       if coordskoopa1y2<537:
           if ((coordsmarioy2-1>=coordskoopa1y1-5 and coordsmarioy2<=coordskoopa1y1)) and len(overlaps)>4:
               print('splat')
               Koopa1_flip()
               mbounce()
               return None
        
    if coordsmarioy2== coordsplat1y1 and coordsmariox1 <= coordsplat1x2:
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    elif coordsmarioy2==coordsplat2y1 and coordsmariox2>= coordsplat2x1:
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    elif coordsmarioy2==coordsplat3y1 and coordsmariox1<= coordsplat3x2:
        
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    elif coordsmarioy2==coordsplat4y1 and coordsmariox2>=coordsplat4x1:
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    elif coordsmarioy2==coordsplatcentroy1 and (coordsmariox2>=coordsplatcentrox1 and coordsmariox1<=coordsplatcentrox2):
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    elif coordsmarioy2==coordsplat5y1 and coordsmariox1<=coordsplat5x2:
      if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
      elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
      return None
    elif coordsmarioy2==coordsplat6y1 and coordsmariox2>=coordsplat6x1:
      if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
      elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
      return None
    elif coords1m>= coords3m:
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        
        return None
    else:
        x.after(2,movedownm)
        canvas.move(mario, 0, 2)
        canvas.move(spritemario, 0, 2)
def jumpm(event):
    global spritemario
    global canvas
    canvas.bind('<w>', ignore)
    global coords1m #coordenadas que van a cambiar
    global coords2m #coordenadas de referencia hacia arriba
    global coords3m #coordenadas originales
    global estadomario
    global mseconds
    mseconds=550
    coordsmarioy2=int(canvas.coords(mario)[3])
    coordsmariox1= int(canvas.coords(mario)[0])
    coordsmariox2= int(canvas.coords(mario)[2])
    if estadomario== 'izquierda':
        estadomario= 'saltoizquierda'
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmariosaltoizquierda)
        
        
    elif estadomario=='derecha':
        estadomario='saltoderecha'
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmariosaltoderecha)
        
    coords1m=int(canvas.coords(mario)[1])
    coords2m=coords1m-200
    coords3m=coords1m
    moveupm()
    x.after(mseconds,bindit)



def bindit():
    canvas.bind('<w>', jumpm)
def ignore(event):
    return 'break'

def fallmplat1():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2 <540 and coordsmarioy2 >537:
        if estadomario=='saltoizquierda':
            estadomario= 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        
        return None
    else:
        x.after(2,fallmplat1)
        canvas.move(mario, 0, 2)
        canvas.move(spritemario,0,2)
def fallmplat2():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2<540 and coordsmarioy2>537:
        if estadomario=='saltoizquierda':
            estadomario='izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)  
        return None
    else:
        x.after(2,fallmplat2)
        canvas.move(mario,0,2)
        canvas.move(spritemario,0,2)
def fallmplat3():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2==coordsplat1y1:
        if estadomario=='saltoizquierda':
            estadomario='izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    else:
        x.after(2, fallmplat3)
        canvas.move(mario,0,2)
        canvas.move(spritemario,0,2)

def fallmplat4():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2==coordsplat2y1:
        if estadomario=='saltoizquierda':
            estadomario='izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    else:
        x.after(2,fallmplat3)
        canvas.move(mario, 0, 2)
        canvas.move(spritemario, 0, 2)
def fallmplatcentroizquierda():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2==coordsplat1y1:
      if estadomario=='saltoizquierda':
        estadomario='izquierda'
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
      elif estadomario =='saltoderecha':
        estadomario='derecha'
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    else:
      x.after(2,fallmplatcentroizquierda)
      canvas.move(mario,0,2)
      canvas.move(spritemario,0,2)
        
def fallmplatcentroderecha():
  global estadomario
  global spritemario
  coordsmariox1=int(canvas.coords(mario)[0])
  coordsmarioy1= int(canvas.coords(mario)[1])
  coordsmariox2=int(canvas.coords(mario)[2])
  coordsmarioy2=int(canvas.coords(mario)[3])
  if coordsmarioy2==coordsplat2y1:
    if estadomario=='saltoizquierda':
      estadomario='izquierda'
      canvas.delete(spritemario)
      spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
    elif estadomario =='saltoderecha':
      estadomario='derecha'
      canvas.delete(spritemario)
      spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
    return None
  else:
    x.after(2, fallmplatcentroderecha)
    canvas.move(mario,0,2)
    canvas.move(spritemario,0,2)
      
        
def fallmplat5():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2==coordsplatcentroy1:
        if estadomario=='saltoizquierda':
            estadomario='izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    else:
        x.after(2, fallmplat5)
        canvas.move(mario,0,2)
        canvas.move(spritemario,0,2)
def fallmplat6():
    global estadomario
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if coordsmarioy2>=coordsplatcentroy1:
        if estadomario=='saltoizquierda':
            estadomario='izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario =='saltoderecha':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        return None
    else:
        x.after(2, fallmplat6)
        canvas.move(mario,0,2)
        canvas.move(spritemario,0,2)



    
def keym(event):
    global estadomario
    global spritemario
    global canvas
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmarioy2=int(canvas.coords(mario)[3])
    coordsmariox2=int(canvas.coords(mario)[2])
    
    if event.char=='a':
        if estadomario== 'derecha':
            estadomario = 'izquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioizquierda)
        elif estadomario=='saltoderecha':
            estadomario= 'saltoizquierda'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmariosaltoizquierda)
            
        if coordsmariox1==coordsplat1x2 and (not((coordsmarioy1>coordsplat1y2 and coordsmarioy2 >coordsplat1y2) or (coordsmarioy1< coordsplat1y1 and coordsmarioy2< coordsplat1y1))):
            return None
        if coordsmariox1==coordsplat3x1 and (not((coordsmarioy1>coordsplat3y2 and coordsmarioy2 > coordsplat3y2) or (coordsmarioy1< coordsplat3y1 and coordsmarioy2< coordsplat3y1))):
            return None
        if coordsmarioy2==coordsplat2y1 and coordsmariox2<coordsplat2x1:
            if coordsmariox1>coordsplat1x2:
                estadomario='saltoizquierda'
                canvas.delete(spritemario)
                spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoizquierda)
                
                fallmplat2()
        elif coordsmarioy2==coordsplatcentroy1 and coordsmariox2<coordsplatcentrox1 and coordsmariox1>coordsplat3x2:
          
          estadomario='saltoizquierda'
          canvas.delete(spritemario)
          spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoizquierda)
          
          fallmplatcentroizquierda()
        elif coordsmarioy2==coordsplat4y1 and coordsmariox2<coordsplat4x1:
            if coordsmariox1>coordsplatcentrox2:
                estadomario='saltoizquierda'
                canvas.delete(spritemario)
                spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoizquierda)
                
                fallmplat4()
        elif coordsmarioy2==coordsplat6y1 and coordsmariox2<coordsplat6x1 and coordsmariox1>coordsplat5x2:
                estadomario='saltoizquierda'
                canvas.delete(spritemario)
                spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoizquierda)
                
                fallmplat6()
        
        if coordsmariox1<0:
            canvas.move(mario, 1250, 0)
            canvas.move(spritemario, 1250, 0)
        canvas.move(mario, -20, 0)
        canvas.move(spritemario, -20, 0)

    elif event.char== 'd':
        orient='derecha'
        if estadomario== 'izquierda':
            estadomario='derecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioderecha)
        elif estadomario=='saltoizquierda':
            estadomario= 'saltoderecha'
            canvas.delete(spritemario)
            spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmariosaltoderecha)
        if coordsmariox1== coordsplat2x1 and (not((coordsmarioy1>=coordsplat2y2 and coordsmarioy2>=coordsplat2y2) or (coordsmarioy1<=coordsplat2y1 and coordsmarioy2<= coordsplat2y1))):
            return None
        if coordsmariox1== coordsplat4x1 and (not((coordsmarioy1>=coordsplat4y2 and coordsmarioy2>=coordsplat4y2) or (coordsmarioy1<=coordsplat4y1 and coordsmarioy2 <= coordsplat4y1))):
            return None
        if coordsmarioy2==coordsplat1y1 and coordsmariox1 > coordsplat1x2:
            if coordsmariox2 < coordsplat2x1:
                estadomario='saltoderecha'
                canvas.delete(spritemario)
                spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
                print(estadomario)
                fallmplat1()
        elif coordsmarioy2==coordsplatcentroy1 and coordsmariox1>coordsplatcentrox2 and coordsmariox2<coordsplat4x1:
          estadomario='saltoderecha'
          canvas.delete(spritemario)
          spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
          print(estadomario)
          fallmplatcentroderecha()
        elif coordsmarioy2==coordsplat3y1 and coordsmariox1 > coordsplat3x2:
            if coordsmariox2< coordsplatcentrox1:
                estadomario='saltoderecha'
                canvas.delete(spritemario)
                spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
                print(estadomario)
                fallmplat3()

        elif coordsmarioy2==coordsplat5y1 and coordsmariox1>coordsplat5x2 and coordsmariox2< coordsplat6x1:
          estadomario='saltoderecha'
          canvas.delete(spritemario)
          spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
          print(estadomario)
          fallmplat5()
        
        if coordsmariox2>1280:
          canvas.move(mario,-1250,0)
          canvas.move(spritemario,-1250,0)
            
        canvas.move(mario, 20, 0)
        canvas.move(spritemario, 20, 0)


def mbounce():
    global coords1m
    global coords2m
    global coords3m
    coords2m+=50
    moveupm()
    return None
###########################ENEMIGOS################################
def spawn_koopa1():
    global estadokoopa1
    if estadokoopa1== None:
        global koopa1
        global koopastale
        global koopastep
        global spritekoopa
        global koopaanim
        koopa1=canvas.create_rectangle(100, 75, 140, coordsplat6y1, fill=None,width=1) #30x60->40x50
        estadokoopa1='creado'
        koopaanim=1
        coordskoopa1x1=int(canvas.coords(koopa1)[0])
        coordskoopa1y1=int(canvas.coords(koopa1)[1])
        coordskoopa1x2=int(canvas.coords(koopa1)[2])
        coordskoopa1y2=int(canvas.coords(koopa1)[3])
        spritekoopa=canvas.create_image(coordskoopa1x1+24,coordskoopa1y1+25,image=koopastale)
        canvas.tag_lower(koopa1)
        
        x.after(5000, spawn_koopa1)
        x.after(2,koopa1_behaviour)
    else:
        x.after(5000,spawn_koopa1)

def koopa1_behaviour():
    global koopa1
    global estadokoopa1
    global spritekoopa
    global koopastale
    global koopastep
    global koopaanim
    if estadokoopa1=='creado':
        coordskoopa1x1=int(canvas.coords(koopa1)[0])
        coordskoopa1y1=int(canvas.coords(koopa1)[1])
        coordskoopa1x2=int(canvas.coords(koopa1)[2])
        coordskoopa1y2=int(canvas.coords(koopa1)[3])
        canvas.move(koopa1,5,0)
        canvas.move(spritekoopa, 5, 0)
        if koopaanim==1:
            canvas.delete(spritekoopa)
            spritekoopa=canvas.create_image(coordskoopa1x1+24, coordskoopa1y1+25, image=koopastep)
            koopaanim-=1
        elif koopaanim==0:
            canvas.delete(spritekoopa)
            spritekoopa=canvas.create_image(coordskoopa1x1+24, coordskoopa1y1+25, image=koopastale)
            koopaanim+=1
        if coordskoopa1x2>=1280:
            canvas.move(koopa1,-1280,0)
            canvas.move(spritekoopa, -1280, 0)
        elif coordskoopa1x1<0:
            canvas.move(koopa1,1280,0)
            canvas.move(spritekoopa, 1280, 0)
        if coordskoopa1x1>coordsplat5x2 and coordskoopa1y2<=coordsplat5y1:
            fallkoopaplat5()
        elif coordskoopa1x1>coordsplatcentrox2 and coordskoopa1y2<=coordsplatcentroy1:
            fallkoopaplatcentro()
        elif coordskoopa1x1>coordsplat1x2 and coordskoopa1x2<coordsplat2x1  and coordskoopa1y2==coordsplat1y1:
            fallkoopaplat1()
    elif estadokoopa1=='volteado':
        return None
    x.after(100,koopa1_behaviour)

def Koopa1_flip():
    global koopa1
    global estadokoopa1
    global spritekoopa
    global koopaflipped
    global koopaflippedanim
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    estadokoopa1='volteado'
    canvas.delete(koopa1)
    canvas.delete(spritekoopa)
    koopa1=canvas.create_rectangle(coordskoopa1x1-5,coordskoopa1y1+10,coordskoopa1x2+5,coordskoopa1y2)
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    spritekoopa=canvas.create_image(coordskoopa1x1+26, coordskoopa1y1+20, image=koopaflipped)
    koopaflippedanim=1
    x.after(500, changeflipkoopa)
    x.after(15000, unflipkoopa)
def changeflipkoopa():
    global estadokoopa1
    global spritekoopa
    global koopaflipped
    global koopaflipped2
    global koopaflippedanim
    global estadokoopa1
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    if estadokoopa1!='volteado':
        return None
    else:
        if koopaflippedanim==1:
            canvas.delete(spritekoopa)
            spritekoopa= canvas.create_image(coordskoopa1x1+26, coordskoopa1y1+20, image=koopaflipped2)
            koopaflippedanim-=1
        elif koopaflippedanim==0:
            canvas.delete(spritekoopa)
            spritekoopa= canvas.create_image(coordskoopa1x1+26, coordskoopa1y1+20, image=koopaflipped)
            koopaflippedanim+=1
        x.after(500, changeflipkoopa)
        
def unflipkoopa():
    global estadokoopa1
    global spritekoopa
    global koopastale
    global koopa1
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    estadokoopa1='creado'
    canvas.delete(koopa1)
    canvas.delete(spritekoopa)
    koopa1=canvas.create_rectangle(coordskoopa1x1+5, coordskoopa1y1-10, coordskoopa1x2-5, coordskoopa1y2)
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    spritekoopa=canvas.create_image(coordskoopa1x1+24,coordskoopa1y1+25, image=koopastale)
    x.after(2, koopa1_behaviour)
    
    
def fallkoopaplat5():
    global koopa1
    global spritemario
    canvas.tag_raise(koopa1)
    canvas.tag_raise(spritemario)
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    if coordskoopa1y2==coordsplatcentroy1:
        return None
    else:
        x.after(2, fallkoopaplat5)
        canvas.move(koopa1,0,2)
        #canvas.move(spritemario,0,2)

def fallkoopaplatcentro():
    global koopa1
    global spritemario
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    if coordskoopa1y2==coordsplat2y1:
        return None
    else:
        x.after(2, fallkoopaplatcentro)
        canvas.move(koopa1,0,2)
        #canvas.move(spritemario,0,2)


def fallkoopaplat1():
    global koopa1
    global spritemario
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    if coordskoopa1y2>537:
        return None
    else:
        x.after(2, fallkoopaplat1)
        canvas.move(koopa1,0,2)
        #canvas.move(spritemario,0,2)




        

def destruirprueba():
    ventanprueb.destroy()
    global estadokoopa1
    global canvas
    global estado
    global plat1
    global plat2
    global plat3
    global plat4
    global plat5
    global plat6
    global mario
    global coordsplat2x1
    global coordsplat2y1
    global coordsplat2x2
    global coordsplat2y2
    global coordsmarioy2glob
    global coordsmariox1glob
    global coordsmariox2glob
    global coordsmarioy1glob
    global coordsplat1x1
    global coordsplat1y1
    global coordsplat1x2
    global coordsplat1y2


    global coordsplat3x1
    global coordsplat3y1
    global coordsplat3x2
    global coordsplat3y2
    global coordsplat4x1
    global coordsplat4y1
    global coordsplat4x2
    global coordsplat4y2
    global coordsplatcentrox1
    global coordsplatcentroy1
    global coordsplatcentrox2
    global coordsplatcentroy2

    global coordsplat5x1
    global coordsplat5y1
    global coordsplat5x2
    global coordsplat5y2
    global coordsplat6x1
    global coordsplat6y1
    global coordsplat6x2
    global coordsplat6y2

    global pipe1
    global pipe1coordsx1
    global pipe1coordsx2
    global pipe1coordsy1
    global pipe1coordsy2
    global pipesprite1

    global koopastale
    global koopastep
    global koopaflipped
    global koopaflipped2
    
    global x
    global imagenmarioderecha
    global spritemario
    global estadomario
    global imagenmarioizquierda
    global imagenmariosaltoizquierda
    global imagenmariosaltoderecha
    x= Crear_Ventana()
    x.after(5000, spawn_koopa1)
    estadokoopa1=None
    canvas= Canvas(x, width=1280, height=720)
    canvas.focus_set()
    estadomario='derecha'
    canvas.bind('<a>', keym)
    canvas.bind('<d>', keym)
    canvas.bind('<w>', jumpm)
    
    canvas.pack()
    plat1= canvas.create_rectangle(1,415, 400, 440, fill= 'blue')
    plat2= canvas.create_rectangle(820, 415, 1280, 440, fill='blue')
    plat3= canvas.create_rectangle(1,275, 150, 300, fill='blue')
    plat4= canvas.create_rectangle(1130,275,1280,300, fill='blue')
    platcentro= canvas.create_rectangle(380,275,840,300,fill='blue')
    plat5= canvas.create_rectangle(1,125, 550, 150, fill='blue')
    plat6= canvas.create_rectangle(730, 125, 1280, 150, fill='blue')
    mario= canvas.create_rectangle(0,490,51,540,fill=None,width=0 )
    imagenmarioderecha= PhotoImage(file='staleright.gif')
    imagenmarioizquierda= PhotoImage(file='staleleft.gif')
    imagenmariosaltoizquierda= PhotoImage(file='jumpleft.gif')
    imagenmariosaltoderecha=PhotoImage(file='jumpright.gif')
    texturaladrillo=PhotoImage(file='bricks.gif')
    pipeleft=PhotoImage(file='pipeleft.gif')
    piperight=PhotoImage(file='piperight.gif')
    ladrillos=canvas.create_image(0,720,image=texturaladrillo, anchor= SW)


    koopastale=PhotoImage(file='koopastale.gif')
    koopastep=PhotoImage(file='koopastep.gif')
    koopaflipped=PhotoImage(file='koopaflipped.gif')
    koopaflipped2=PhotoImage(file='koopaflipped2.gif')
    

    coordsplat2x1=int(canvas.coords(plat2)[0])
    coordsplat2y1=int(canvas.coords(plat2)[1])+1
    coordsplat2x2=int(canvas.coords(plat2)[2])-2
    coordsplat2y2=int(canvas.coords(plat2)[3])

    coordsmarioy2glob=(canvas.coords(mario)[3])
    coordsmariox1glob=(canvas.coords(mario)[0])
    coordsmariox2glob=(canvas.coords(mario)[2])
    coordsmarioy1glob= canvas.coords(mario)[1]

    coordsplat1x1=int(canvas.coords(plat1)[0])
    coordsplat1y1=int(canvas.coords(plat1)[1])+1
    coordsplat1x2=int(canvas.coords(plat1)[2])-2
    coordsplat1y2=int(canvas.coords(plat1)[3])

    


    coordsplat3x1=int(canvas.coords(plat3)[0])
    coordsplat3y1=int(canvas.coords(plat3)[1])+1
    coordsplat3x2=int(canvas.coords(plat3)[2])-2
    coordsplat3y2=int(canvas.coords(plat3)[3])

    coordsplat4x1=int(canvas.coords(plat4)[0])+2
    coordsplat4y1=int(canvas.coords(plat4)[1])+1
    coordsplat4x2=int(canvas.coords(plat4)[2])-2
    coordsplat4y2=int(canvas.coords(plat4)[3])

    coordsplatcentrox1=int(canvas.coords(platcentro)[0])
    coordsplatcentroy1=int(canvas.coords(platcentro)[1])+1
    coordsplatcentrox2=int(canvas.coords(platcentro)[2])-2
    coordsplatcentroy2=int(canvas.coords(platcentro)[3])

    coordsplat5x1=int(canvas.coords(plat5)[0])+2
    coordsplat5y1=int(canvas.coords(plat5)[1])+1
    coordsplat5x2=int(canvas.coords(plat5)[2])-2
    coordsplat5y2=int(canvas.coords(plat5)[3])
    coordsplat6x1=int(canvas.coords(plat6)[0])+2
    coordsplat6y1=int(canvas.coords(plat6)[1])+1
    coordsplat6x2=int(canvas.coords(plat6)[2])-2
    coordsplat6y2=int(canvas.coords(plat6)[3])

    pipe1=canvas.create_rectangle(0, 20, 136, coordsplat6y1, fill=None, width=0)
    pipe1coordsx1= int(canvas.coords(pipe1)[0])
    pipe1coordsx2= int(canvas.coords(pipe1)[2])
    pipe1coordsy1= int(canvas.coords(pipe1)[1])
    pipe1coordsy2= int(canvas.coords(pipe1)[3])
    pipesprite1=canvas.create_image(pipe1coordsx1+65,pipe1coordsy1+53, image=piperight)
    
    
    spritemario=canvas.create_image(coordsmariox1glob+25,coordsmarioy2glob-27, image=imagenmarioderecha)
    
    
    

    x.mainloop()


ventanprueb=Tk()
ventanprueb.geometry('200x300')
Bot21= Button(ventanprueb,text='holi', command=destruirprueba)
Bot21.pack(side=TOP)
ventanprueb.mainloop()


