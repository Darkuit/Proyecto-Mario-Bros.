from tkinter import *
import time
import random
import winsound
import threading
import sys
import ast
def Crear_Ventana():
    ventan=Tk()
    ventan.title('Game')
    return ventan


def moveupm():
##'''
##primera parte del salto, movimiento hacia arriba. Detecta si se choca por debajo a los enemigos
##
##'''
    global coords1m
    global coords2m
    global estadokoopa1
    global coords3m
    global spritemario
    global mseconds
    global estadoshadow
    global shadowlife
    global shadowhitanim
    global shyhitanim
    global rempow



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
        if estadoparatroopa=='creado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if coordsparatroopay2==coordsplat2y1 and coordsparatroopax1<coordsplat1x2:
                overlapsp=canvas.find_overlapping(coordsparatroopax1, coordsparatroopay2, coordsparatroopax2, coordsplat2y2+5)
                if len(overlapsp)>4:
                    flipparatroopa()
        if estadoshadow=='creado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsshadowy2==coordsplat2y1 and coordsshadowx1<coordsplat1x2:
                overlapss=canvas.find_overlapping(coordsshadowx1, coordsshadowy2, coordsshadowx2, coordsplat2y2+5)
                if len(overlapss)>4:
                    if shadowlife==2:

                        shadowhitanim=4
                        shadowhitfun()
                    elif shadowlife==1:
                        flipshadow()
        if estadoshy!=None and estadoshy!='atacado':
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1=int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])
            if coordsshyy2==coordsplat2y1 and coordsshyx1<coordsplat1x2:
                overlapss=canvas.find_overlapping(coordsshyx1, coordsshyy2, coordsshyx2, coordsplat2y2+5)
                if len(overlapss)>4:
                    shyhitanim=4
                    shydie()
                    
            
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m == coordspowy2 and coordsmariox2>=coordspowx1 and coordsmariox1<=coordspowx2:
        powpress()
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
                print('koopa')
                overlaps=canvas.find_overlapping(coordskoopa1x1, coordskoopa1y2, coordskoopa1x2, coordsplat2y2+5)
                if len(overlaps)>4:
                    Koopa1_flip()
        if estadoparatroopa=='creado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if coordsparatroopay2==coordsplat2y1 and coordsparatroopax2>coordsplat2x1:
                overlapsp=canvas.find_overlapping(coordsparatroopax1, coordsparatroopay2, coordsparatroopax2, coordsplat2y2+5)
                if len(overlapsp)>4:
                    flipparatroopa()
        if estadoshadow=='creado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsshadowy2==coordsplat2y1 and coordsshadowx2>coordsplat2x1:
                overlapss=canvas.find_overlapping(coordsshadowx1, coordsshadowy2, coordsshadowx2, coordsplat2y2+5)
                if len(overlapss)>4:
                    if shadowlife==2:

                        shadowhitanim=4
                        shadowhitfun()
                    elif shadowlife==1:
                        flipshadow()
        if estadoshy!=None and estadoshy!='atacado':
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1=int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])
            if coordsshyy2==coordsplat2y1 and coordsshyx1>coordsplat2x1:
                overlapss=canvas.find_overlapping(coordsshyx1, coordsshyy2, coordsshyx2, coordsplat2y2+5)
                if len(overlapss)>3:
                    shyhitanim=4
                    shydie()
                    

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
        if estadoparatroopa=='creado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if coordsparatroopay2==coordsplatcentroy1 and coordsparatroopax1<coordsplatcentrox2 and coordsparatroopax2>coordsplatcentrox1:
                overlapsp=canvas.find_overlapping(coordsparatroopax1, coordsparatroopay2, coordsparatroopax2, coordsplatcentroy2+5)
                if len(overlapsp)>4:
                    flipparatroopa()
        if estadoshadow=='creado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsshadowy2==coordsplatcentroy1 and coordsshadowx1<coordsplatcentrox2 and coordsshadowx2>coordsplatcentrox1:
                overlapss=canvas.find_overlapping(coordsshadowx1, coordsshadowy2, coordsshadowx2, coordsplat2y2+5)
                if len(overlapss)>4:
                    if shadowlife==2:
                        
                        shadowhitanim=4
                        shadowhitfun()
                    elif shadowlife==1:
                        flipshadow()
        if estadoshy!=None and estadoshy!='atacado':
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1=int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])
            if coordsshyy2==coordsplatcentroy1 and coordsshyx1<coordsplatcentrox2 and coordsshyx2>coordsplatcentrox1:
                overlapss=canvas.find_overlapping(coordsshyx1, coordsshyy2, coordsshyx2, coordsplat2y2+5)
                if len(overlapss)>3:
                    shyhitanim=4
                    shydie()
                    
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m==coordsplat5y2 and coordsmariox1<=coordsplat5x2:
        if estadokoopa1=='creado':
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1=int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if coordskoopa1y2==coordsplat5y1 and coordskoopa1x1<coordsplat5x2:
                overlaps=canvas.find_overlapping(coordskoopa1x1, coordskoopa1y2, coordskoopa1x2, coordsplat5y2+5)
                if len(overlaps)>4:
                    Koopa1_flip()
        if estadoshy!=None and estadoshy!='atacado':
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1=int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])
            
            if coordsshyy2==coordsplat6y1 and coordsshyx1<coordsplat6x1:
                overlapss=canvas.find_overlapping(coordsshyx1, coordsshyy2, coordsshyx2, coordsplat2y2+5)
                if len(overlapss)>3:
                    shyhitanim=4
                    shydie()
        time.sleep(0.01)
        mseconds=100
        movedownm()
        return None
    elif coords1m==coordsplat6y2 and coordsmariox2>=coordsplat6x1:
        
        if estadoparatroopa=='creado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if coordsparatroopay2==coordsplat6y1 and coordsparatroopax1>coordsplat6x1:
                overlapsp=canvas.find_overlapping(coordsparatroopax1, coordsparatroopay2, coordsparatroopax2, coordsplat6y2+5)
                if len(overlapsp)>4:
                    flipparatroopa()
        if estadoshadow=='creado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsshadowy2==coordsplat6y1 and coordsshadowx1>coordsplat6x1:
                overlapss=canvas.find_overlapping(coordsshadowx1, coordsshadowy2, coordsshadowx2, coordsplat2y2+5)
                if len(overlapss)>4:
                    if shadowlife==2:

                        shadowhitanim=4
                        shadowhitfun()
                    elif shadowlife==1:
                        flipshadow()

                    
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

##'''
##segunda parte del salto, movimiento hacia abajo
##'''
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
           if ((coordsmarioy2-1>=coordskoopa1y1-5 and coordsmarioy2<=coordskoopa1y1)) and len(overlaps)>=4:
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
##'''
##función que no hace nada, usada para ignorar los bindings
##'''
    return 'break'

def fallmplat1():
##'''
##todas las que respeten este código de nombre se refieren a las funciones que hacen que Mario caiga de alguna de las plataformas
##'''
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
##'''
##función principal del movimiento de Mario
##'''
    global estadomario
    global spritemario
    global canvas
    global estadokoopa1
    global estadoparatroopa
    global estadoshadow
    global power
    global estadopower

    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmarioy2=int(canvas.coords(mario)[3])
    coordsmariox2=int(canvas.coords(mario)[2])
    
    
    
    if event.char=='a':
        if estadokoopa1=='volteado':
            
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1= int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if (coordsmarioy2==coordskoopa1y2 or ((coordsmarioy2>537 and coordsmarioy2<=540) and (coordskoopa1y2>537 and coordskoopa1y2<=540))) and (coordsmariox1>=coordskoopa1x1 and coordsmariox1<=coordskoopa1x2):
                mhitkoopa('izquierda', 'koopa')
        if estadoparatroopa=='volteado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if coordsmarioy2==coordsparatroopay2 or (((coordsmarioy2>537 and coordsmarioy2<=540) and (coordsparatroopay2>537 and coordsparatroopay2<=540)) and (coordsmariox1>=coordsparatroopax1 and coordsmariox1<=coordsparatroopax2)):
                mhitkoopa('izquierda', 'paratroopa')
        if estadoshadow=='volteado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsmarioy2==coordsshadowy2 or (((coordsmarioy2>537 and coordsmarioy2<=540) and (coordsshadowy2>537 and coordsshadowy2<=540)) and (coordsmariox1>=coordsshadowx1 and coordsmariox1<=coordsshadowx2)):
                mhitkoopa('izquierda', 'shadow')
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
        if estadopower=='creado':
            coordspower=canvas.coords(power)
            if coordsmarioy1>=coordsplatcentroy2 and coordsmarioy1<=coordsplat1y1 and(coordsmariox1<=coordspower[2] and coordsmariox1>=coordspower[0]) :
                pickpowerm()
                
        if coordsmariox1<0:
            canvas.move(mario, 1250, 0)
            canvas.move(spritemario, 1250, 0)
        canvas.move(mario, -20, 0)
        canvas.move(spritemario, -20, 0)

    elif event.char== 'd':
        if estadokoopa1=='volteado':
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1= int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if (coordsmarioy2==coordskoopa1y2 or ((coordsmarioy2>537 and coordsmarioy2<=540) and (coordskoopa1y2>537 and coordskoopa1y2<=540))) and (coordsmariox2>=coordskoopa1x1 and coordsmariox2<=coordskoopa1x2):
                mhitkoopa('derecha', 'koopa')
        if estadoparatroopa=='volteado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if (coordsmarioy2==coordsparatroopay2 or ((coordsmarioy2>537 and coordsmarioy2<=540) and (coordsparatroopay2>537 and coordsparatroopay2<=549))) and (coordsmariox2>=coordsparatroopax1 and coordsmariox2<=coordsparatroopax2):
                mhitkoopa('derecha', 'paratroopa')
        if estadoshadow=='volteado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsmarioy2==coordsshadowy2 or (((coordsmarioy2>537 and coordsmarioy2<=540) and (coordsshadowy2>537 and coordsshadowy2<=540)) and (coordsmariox1>=coordsshadowx1 and coordsmariox1<=coordsshadowx2)):
                mhitkoopa('derecha', 'shadow')
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
                fallmplat1()
        elif coordsmarioy2==coordsplatcentroy1 and coordsmariox1>coordsplatcentrox2 and coordsmariox2<coordsplat4x1:
          estadomario='saltoderecha'
          canvas.delete(spritemario)
          spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
          fallmplatcentroderecha()
        elif coordsmarioy2==coordsplat3y1 and coordsmariox1 > coordsplat3x2:
            if coordsmariox2< coordsplatcentrox1:
                estadomario='saltoderecha'
                canvas.delete(spritemario)
                spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
                fallmplat3()

        elif coordsmarioy2==coordsplat5y1 and coordsmariox1>coordsplat5x2 and coordsmariox2< coordsplat6x1:
          estadomario='saltoderecha'
          canvas.delete(spritemario)
          spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27,image=imagenmariosaltoderecha)
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

def mhitkoopa(orient, enem):
##'''
##Función que hace que Mario 'golpee' a un enemigo volteado. Recibe la orientación hacia la que Mario está mirando y el enemigo a golpear
##'''
    global spritemario
    global estadomario
    global imagenmarioholdizquierda
    global imagenmarioholdderecha
    global imagenmarioderecha
    global imagenmarioizquierda
    global coordsreferencekoopa
    global refkoopa
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if enem=='koopa':
        coordskoopa1y2=int(canvas.coords(koopa1)[3])
        coordsreferencekoopa=coordskoopa1y2-150
        refkoopa=0
    elif enem=='paratroopa':
        coordsparatroopay2=int(canvas.coords(paratroopa)[3])
    elif enem=='shadow':
        coordsshadowy2=int(canvas.coords(shadow)[3])
    if orient=='izquierda':
        print('ataqueizquierda')
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioholdizquierda)
        x.after(200, mariohitleft)
        if enem=='koopa':
            x.after(200, koopadie)
        elif enem=='paratroopa':
            x.after(200, paratroopadie)
        elif enem=='shadow':
            x.after(200,shadowdie)
    elif orient=='derecha':
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmarioholdderecha)
        x.after(200, mariohitright)
        if enem=='koopa':
            x.after(200, koopadie)
        elif enem=='paratroopa':
            x.after(200, paratroopadie)
        elif enem=='shadow':
            x.after(200,shadowdie)
def mariohitleft():
    ''' Cambia la imagen para el efecto de animación y cambia la puntuación
    '''
    global imagenmariohitizquierda, estadomario, spritemario, score1p, vidas1, addscore
    
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if estadomario=='izquierda':

        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmariohitizquierda)
        score1p.set(score1p.get()+100)
        if score1p.get() == 900:
            vidas+=1
            score1p.set(0)
        
        
        
def mariohitright():
    global imagenmariohitderecha
    global estadomario
    global spritemario
    global score1p
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    if estadomario=='derecha':
        canvas.delete(spritemario)
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=imagenmariohitderecha)
        score1p.set(score1p.get()+100)
        if score1p.get() == 900:
            vidas+=1
            score1p.set(0)
        
def mariodie():
    '''
Primera parte de la muerte de Mario
    '''
    global estadomario
    global spritemario
    global mariodieright
    global mariodieleft
    global beforedead

    canvas.bind('<w>',ignore)
    canvas.bind('<a>', ignore)
    canvas.bind('<d>',ignore)
    beforedead=estadomario
    estadomario='muriendo'
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    canvas.delete(spritemario)
    if beforedead=='izquierda' or beforedead=='saltoizquierda':
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=mariodieleft)
    elif beforedead=='derecha' or beforedead=='saltoderecha':
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-27, image=mariodieright)
    x.after(500, mariodead)

def mariodead():
    global mariodeadright
    global mariodeadleft
    global mariodeadright
    global mariodeadleft
    global estadomario
    global beforedead
    global spritemario
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy1= int(canvas.coords(mario)[1])
    coordsmariox2=int(canvas.coords(mario)[2])
    coordsmarioy2=int(canvas.coords(mario)[3])
    canvas.delete(spritemario)
    if beforedead == 'izquierda' or beforedead=='saltoizquierda':
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-20, image=mariodeadleft)
    elif beforedead =='derecha' or beforedead=='derecha':
        spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-20, image=mariodeadright)
    x.after(1000, despawnmario)
def despawnmario():
##'''
##desaparece a Mario y descuenta una vida. Inicia Game Over si quedan cero vidas
##'''
    global mario
    global spritemario
    global vidas1
    global mainm
    global letters
    global gover
    global z
    global screen
    vidas1.set(vidas1.get()-1)
    canvas.delete(mario)
    canvas.delete(spritemario)
    if vidas1.get()==0:
        x.destroy()
        z=Tk()
        z.title(':c')
        gover=Canvas(z, width=1280, height=720)
        gover.pack()
        letters=PhotoImage(file='gameover.gif')
        screen=gover.create_image(0,0,image=letters, anchor=NW)


        mainm=threading.Thread(target=gameovermusic)
        mainm.start()
        return None
        
    
    x.after(3000, respawnmario)
def respawnmario():
##'''
##Si quedan vidas, respawnea a Mario
##'''
    global mario
    global estadomario
    global spritemario
    global imagenmarioderecha
    mario= canvas.create_rectangle(0,490,51,540,fill=None,width=0 )
    spritemario=canvas.create_image(coordsmariox1glob+25,coordsmarioy2glob-27, image=imagenmarioderecha)
    estadomario='derecha'
    bindings()

def freezemario():
##'''
##Congelado y descongelado de Mario. Efecto del Shy Guy
##'''
    global estadomario
    global spritemario
    global frozenmario
    canvas.bind('<w>',ignore)
    canvas.bind('<a>', ignore)
    canvas.bind('<d>',ignore)
    estadomario='congelado'
    coordsmariox1=int(canvas.coords(mario)[0])
    coordsmarioy2=int(canvas.coords(mario)[3])
    canvas.delete(spritemario)
    spritemario=canvas.create_image(coordsmariox1+25, coordsmarioy2-40, image=frozenmario)
    x.after(7000, unfreezemario)
def unfreezemario():
    global estadomario
    global spritemario
    global imagenmarioderecha
    if estadomario=='congelado':
        bindings()
        canvas.delete(spritemario)
        coordsmariox1=int(canvas.coords(mario)[0])
        coordsmarioy2=int(canvas.coords(mario)[3])
        spritemario=canvas.create_image(coordsmariox1+25,coordsmarioy2-27, image=imagenmarioderecha)
        estadomario='derecha'
###########################ENEMIGOS################################

def spawn_monster():
##'''
##Función que spawnea monstruos si quedan monstruos disponibles
##'''
    global estadokoopa1
    global monstruos
    global estadoparatroopa
    global difficulty
    global estadoshadow
    print(difficulty)

    tipo=random.randint(1,4)
    if difficulty==1:
        d=0
    elif difficulty==2:
        d=1000
    elif difficulty==3:
        d=2000
    elif difficulty==4:
        d=3500
    elif difficulty==5:
        d=6000
    if tipo==1:
        if estadokoopa1== None and monstruos>0:
            global koopa1
            global koopastale
            global koopastep
            global spritekoopa
            global koopaanim
            koopa1=canvas.create_rectangle(100, 75, 140, coordsplat6y1, fill=None,width=0) #30x60->40x50
            estadokoopa1='creado'
            koopaanim=1
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1=int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            spritekoopa=canvas.create_image(coordskoopa1x1+24,coordskoopa1y1+25,image=koopastale)
            canvas.tag_lower(koopa1)

            monstruos-=1
            
            x.after(15000-d, spawn_monster)
            x.after(2,koopa1_behaviour)
        else:
            x.after(15000-d,spawn_monster)
    elif tipo == 2:
        if estadoparatroopa==None and monstruos>0:
            global paratroopa
            global paratroopastale
            global spriteparatroopa
            global paratroopaanim
            paratroopa=canvas.create_rectangle(1140, 75, 1180, coordsplat6y1, fill=None, width=0)
            estadoparatroopa='creado'
            paratroopaanim=1
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            spriteparatroopa=canvas.create_image(coordsparatroopax1+24, coordsparatroopay1+25, image=paratroopastale)

            canvas.tag_lower(paratroopa)
            monstruos-=1
            x.after(15000-d,spawn_monster)
            x.after(5, paratroopabehaviour)
        else:
            x.after(15000-d, spawn_monster)

    elif tipo == 3:
        if estadoshadow==None and monstruos>0:
            global shadow
            global shadowstale
            global spriteshadow
            global shadowanim
            global shadowlife
            global shadowhitanim
            shadowhitanim=4
            shadow=canvas.create_rectangle(1140, 75, 1180, coordsplat6y1, fill=None, width=0)
            estadoshadow='creado'
            shadowlife=2
            shadowanim=1
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])
            spriteshadow=canvas.create_image(coordsshadowx1+24, coordsshadowy1+25, image=shadowstale)

            canvas.tag_lower(shadow)
            monstruos-=1
            x.after(15000-d,spawn_monster)
            x.after(5, shadow_behaviour)
        else:
            x.after(15000-d, spawn_monster)
    elif tipo == 4:
        if estadoshy==None and monstruos>0:
            global shy
            global shystale
            global spriteshy
            global shyanim
            global shyhitanim
            global estadoshy
            shyhitanim=4
            shy=canvas.create_rectangle(100, 75, 140, coordsplat6y1, fill=None,width=0)
            estadoshy='creado'
            shylife=2
            shyanim=1
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1=int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])
            spriteshy=canvas.create_image(coordsshyx1+24, coordsshyy1+25, image=shystale)

            canvas.tag_lower(shy)
            monstruos-=1
            x.after(15000-d,spawn_monster)
            x.after(5, shybehaviour)
            x.after(1000-d, fireshy)
        else:
            x.after(15000-d, spawn_monster)


            



########Kooopa Paratroopa########

def paratroopabehaviour():
##'''
##Comportamiento de la paratroopa. Lanza la función de la parabola de esta
##'''
    global paratroopa
    global estadoparatroopa
    global spriteparatroopa
    global paratroopastale
    global paratroopaflap
    global estadomario
    global difficulty
    global referenceparat
    global referenceparat2
    global parabolestate
    global vidas
    global paused

    if paused:
        x.after(2, paratroopabehaviour)
    else:
        

        if estadoparatroopa=='creado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            referenceparat=coordsparatroopay1-50
            referenceparat2=coordsparatroopay1
            parabolestate=True
            x.after(5, paratroopamovement)

def paratroopamovement():
##'''
##Movimiento de la Paratroopa. Se mueve en parábola
##'''
    global paratroopa
    global estadoparatroopa
    global spriteparatroopa
    global referenceparat
    global referenceparat2
    global paratroopaflap
    global paratroopastale
    global paratroopaanim
    global parabolestate
    global difficulty
    global score1p
    global powerupm
    global paused

    if paused:
        x.after(100, paratroopamovement)
    else:
        


        if estadoparatroopa=='creado':
            coordsparatroopax1=int(canvas.coords(paratroopa)[0])
            coordsparatroopay1=int(canvas.coords(paratroopa)[1])
            coordsparatroopax2=int(canvas.coords(paratroopa)[2])
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if paratroopaanim==1:
                canvas.delete(spriteparatroopa)
                spriteparatroopa=canvas.create_image(coordsparatroopax1+24, coordsparatroopay1+25, image=paratroopaflap)
                paratroopaanim -=1
            elif paratroopaanim==0:
                canvas.delete(spriteparatroopa)
                spriteparatroopa=canvas.create_image(coordsparatroopax1+24, coordsparatroopay1+25, image=paratroopastale)
                paratroopaanim+=1
            if difficulty==1:
                d=200
            elif difficulty==2:
                d=150
            elif difficulty==3:
                d=100
            elif difficulty==4:
                d=50
            elif difficulty==5:
                d=0
            
            if estadomario!='muriendo':
                coordsmariox1=int(canvas.coords(mario)[0])
                coordsmarioy1= int(canvas.coords(mario)[1])
                coordsmariox2=int(canvas.coords(mario)[2])
                coordsmarioy2=int(canvas.coords(mario)[3])
                overlapsp=canvas.find_overlapping(coordsparatroopax1,coordsparatroopay1,coordsparatroopax2,coordsparatroopay2)
                if coordsparatroopay2>537 and coordsparatroopay2<=540 and coordsmarioy2>537 and coordsmarioy2<=540 and len(overlapsp)>=4 and coordsparatroopax1>pipe1coordsx2+20 and coordsparatroopax2<pipe2coordsx1 and ((coordsmariox1<= coordsparatroopax2+5) or (coordsmariox2>=coordsparatroopax1-5)):
                    if not(powerupm):
                        mariodie()
                    else:
                        flipparatroopa()
                        paratroopadie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
                        
                elif coordsparatroopay2<537 and coordsmarioy2<=coordsparatroopay2 and coordsmarioy2> coordsparatroopay1 and len(overlapsp)>5 and ((coordsmariox1<= coordsparatroopax2+5 and coordsmariox1 >=coordsparatroopax1) or (coordsmariox2>=coordsparatroopax1-5 and coordsmariox2<=coordsparatroopax2)):
                    if not(powerupm):
                        mariodie()
                    else:
                        flipparatroopa()
                        paratroopadie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)

            if coordsparatroopax1<pipe1coordsx2 and coordsparatroopay2>537:
                canvas.delete(paratroopa)
                canvas.delete(spriteparatroopa)
                paratroopa=canvas.create_rectangle(1140, 75, 1180, coordsplat6y1, fill=None, width=0)
                estadoparatroopa='creado'
                paratroopaanim=1
                coordsparatroopax1=int(canvas.coords(paratroopa)[0])
                coordsparatroopay1=int(canvas.coords(paratroopa)[1])
                coordsparatroopax2=int(canvas.coords(paratroopa)[2])
                coordsparatroopay2=int(canvas.coords(paratroopa)[3])
                spriteparatroopa=canvas.create_image(coordsparatroopax1+24, coordsparatroopay1+25, image=paratroopastale)
                x.after(1500+d, paratroopabehaviour)
                

                score1p.set(score1p.get()-100)
                return None
            if coordsparatroopay1>referenceparat and parabolestate:
                if coordsparatroopax1<0:
                    canvas.move(paratroopa, 1280, 0)
                canvas.move(paratroopa, -5,-5)
                canvas.move(spriteparatroopa, -5, -5)
                x.after(100+d, paratroopamovement)
            else:
                if coordsparatroopax1<0:
                    canvas.move(paratroopa, 1280, 0)
                if coordsparatroopay1==referenceparat2:
                    parabolestate=True
                    if coordsparatroopax1<coordsplat6x1 and coordsparatroopay2==coordsplat6y1:
                        fallparatroopaplat6()
                    elif coordsparatroopax1<coordsplatcentrox1 and coordsparatroopay2==coordsplatcentroy1:
                        fallparatroopaplatcentro()
                    elif coordsparatroopax2<coordsplat2x1 and coordsparatroopax1>coordsplat1x2 and coordsparatroopay2==coordsplat2y1:
                        fallparatroopaplat2()
                    x.after(1500+d, paratroopabehaviour)
                    return None
                elif coordsparatroopay1==referenceparat:
                    canvas.move(paratroopa, -5, 5)
                    parabolestate=False
                    x.after(100+d, paratroopamovement)
                elif coordsparatroopay1<referenceparat2:
                    canvas.move(paratroopa, -5, 5)
                    canvas.move(spriteparatroopa, -5, 5)
                    x.after(100+d, paratroopamovement)
                
def flipparatroopa():
##'''
##Función que voltea a la paratroopa. A partir de aquí, las funciones que se titulen 'flip...' harán lo mismo con  el monstruo que indiquen
##'''
    global paratroopa
    global estadoparatroopa
    global spriteparatroopa
    global paratroopaflipped
    global background
    global paratroopaflippedanim
    
    coordsparatroopax1=int(canvas.coords(paratroopa)[0])
    coordsparatroopay1=int(canvas.coords(paratroopa)[1])
    coordsparatroopax2=int(canvas.coords(paratroopa)[2])
    coordsparatroopay2=int(canvas.coords(paratroopa)[3])
    estadoparatroopa='volteado'
    canvas.delete(paratroopa)
    canvas.delete(spriteparatroopa)
    paratroopa=canvas.create_rectangle(coordsparatroopax1-5,coordsparatroopay1+10,coordsparatroopax2+5,coordsparatroopay2,width=0)
    coordsparatroopa1x1=int(canvas.coords(paratroopa)[0])
    coordsparatroopa1y1= int(canvas.coords(paratroopa)[1])
    coordsparatroopa1x2=int(canvas.coords(paratroopa)[2])
    coordsparatroopa1y2=int(canvas.coords(paratroopa)[3])
    spriteparatroopa=canvas.create_image(coordsparatroopax1+26, coordsparatroopay1+20, image=paratroopaflipped)
    paratroopaflippedanim=1
    canvas.tag_lower(spriteparatroopa)
    canvas.tag_lower(background)
    x.after(500, changeflipparatroopa)
    x.after(15000, unflipparatroopa)

def changeflipparatroopa():
##'''
##Función que crea la 'animación' cuando esta volteada cambiando los sprites. A partir de aquí, todas las funciones que se llamen 'changeflip...' harán lo mismo con el monstruo que indiquen
##'''
    global estadoparatroopa
    global spriteparatroopa
    global paratroopaflipped
    global paratroopaflipped2
    global paratroopaflippedanim
    global estadoparatroopa
    global background
    coordsparatroopax1=int(canvas.coords(paratroopa)[0])
    coordsparatroopay1= int(canvas.coords(paratroopa)[1])
    coordsparatroopax2=int(canvas.coords(paratroopa)[2])
    coordsparatroopay2=int(canvas.coords(paratroopa)[3])
    if paused:
        x.after(100, changeflipparatroopa)
    else:

        if estadoparatroopa!='volteado':
            return None

        
        else:
            if paratroopaflippedanim==1:
                canvas.delete(spriteparatroopa)
                spriteparatroopa= canvas.create_image(coordsparatroopax1+26, coordsparatroopay1+20, image=paratroopaflipped2)
                canvas.tag_lower(spriteparatroopa)
                canvas.tag_lower(background)
                paratroopaflippedanim-=1
            elif paratroopaflippedanim==0:
                canvas.delete(spriteparatroopa)
                spriteparatroopa= canvas.create_image(coordsparatroopax1+26, coordsparatroopay1+20, image=paratroopaflipped)
                canvas.tag_lower(spriteparatroopa)
                canvas.tag_lower(background)
                paratroopaflippedanim+=1
            x.after(500, changeflipparatroopa)
def unflipparatroopa():
##'''
##Desvoltea a la Paratroopa después de un rato. De nuevo, todas las funciones que sigan este código de nombre haran lo mismo para su monstruo respectivo.
##'''
    global estadoparatroopa
    global spriteparatroopa
    global paratroopastale
    global paratroopa
    global paused
    if estadoparatroopa!='volteado':
        return None

    coordsparatroopax1=int(canvas.coords(paratroopa)[0])
    coordsparatroopay1= int(canvas.coords(paratroopa)[1])
    coordsparatroopax2=int(canvas.coords(paratroopa)[2])
    coordsparatroopay2=int(canvas.coords(paratroopa)[3])

    if paused:
        x.after(5000, unflipparatroopa)
    else:
        
    
        canvas.delete(paratroopa)
        canvas.delete(spriteparatroopa)
        paratroopa=canvas.create_rectangle(coordsparatroopax1+5, coordsparatroopay1-10, coordsparatroopax2-5, coordsparatroopay2, width=0)
        coordsparatroopax1=int(canvas.coords(paratroopa)[0])
        coordsparatroopay1= int(canvas.coords(paratroopa)[1])
        coordsparatroopax2=int(canvas.coords(paratroopa)[2])
        coordsparatroopay2=int(canvas.coords(paratroopa)[3])
        spriteparatroopa=canvas.create_image(coordsparatroopax1+24,coordsparatroopay1+25, image=paratroopastale)
        estadoparatroopa='creado'
        x.after(2, paratroopabehaviour)

##def paratroopadie():
##    global estadoparatroopa
##    global spriteparatroopa
##    global paratroopa
##    global estadoparatroopa
##    if estadoparatroopa==None:
##        return None
##    else:
##        coordsparatroopay1= int(canvas.coords(paratroopa)[1])
##        if coordsparatroopay1>720:
##            canvas.delete(spriteparatroopa)
##            canvas.delete(paratroopa)
##            estadoparatroopa=None
##        else:
##
##            canvas.move(paratroopa,0,2)
##            canvas.move(spriteparatroopa,0,2)
##            x.after(4, paratroopadie)

        
def fallparatroopaplat6():
##'''
##Función que hace caer a la Paratroopa de las plataformas. Todas las que se llamen 'fall...' de aquí en adelante indicarán la caida de la plataforma indicada para el monstruo indicado
##'''
    global paratroopa
    global spriteparatroopa
    canvas.tag_raise(paratroopa)
    canvas.tag_raise(spritemario)
    coordsparatroopax1=int(canvas.coords(paratroopa)[0])
    coordsparatroopay1= int(canvas.coords(paratroopa)[1])
    coordsparatroopax2=int(canvas.coords(paratroopa)[2])
    coordsparatroopay2=int(canvas.coords(paratroopa)[3])
    if coordsparatroopay2==coordsplatcentroy1:
        return None
    else:
        x.after(3, fallparatroopaplat6)
        canvas.move(paratroopa,0,2)
        canvas.move(spriteparatroopa,0,2)

def fallparatroopaplatcentro():
    global paratroopa
    global spriteparatroopa
    coordsparatroopax1=int(canvas.coords(paratroopa)[0])
    coordsparatroopay1= int(canvas.coords(paratroopa)[1])
    coordsparatroopax2=int(canvas.coords(paratroopa)[2])
    coordsparatroopay2=int(canvas.coords(paratroopa)[3])
    if coordsparatroopay2==coordsplat1y1:
        return None
    else:
        x.after(3, fallparatroopaplatcentro)
        canvas.move(paratroopa,0,2)
        canvas.move(spriteparatroopa,0,2)


def fallparatroopaplat2():
    global paratroopa
    global spriteparatroopa
    coordsparatroopax1=int(canvas.coords(paratroopa)[0])
    coordsparatroopay1= int(canvas.coords(paratroopa)[1])
    coordsparatroopax2=int(canvas.coords(paratroopa)[2])
    coordsparatroopay2=int(canvas.coords(paratroopa)[3])
    if coordsparatroopay2>537:
        return None
    else:
        x.after(3, fallparatroopaplat2)
        canvas.move(paratroopa,0,2)
        canvas.move(spriteparatroopa,0,2)
def paratroopadie():
##'''
##Función que mata a la Paratroopa. De nuevo, la convención para el título se respeta para los otros monstruos.
##'''
    global estadoparatroopa
    global spriteparatroopa
    global koopa1
    if estadoparatroopa==None:
        return None
    else:
        estadoparatroopa='atacado'
        coordsparatroopax1=int(canvas.coords(paratroopa)[0])
        coordsparatroopay1= int(canvas.coords(paratroopa)[1])
        coordsparatroopax2=int(canvas.coords(paratroopa)[2])
        coordsparatroopay2=int(canvas.coords(paratroopa)[3])
        if coordsparatroopay1>720:

        
            canvas.delete(spriteparatroopa)
            canvas.delete(paratroopa)
            estadoparatroopa=None
        else:


            canvas.move(paratroopa,0,2)
            canvas.move(spriteparatroopa,0,2)
            x.after(4, paratroopadie)



#########################SHADOW KOOPA##############################

def shadow_behaviour():
##'''
##Función encargada del movimiento de la Shadow Koopa, también accionara la función para matar a Mario si este esta en el radio.
##'''
    global shadow
    global estadoshadow
    global spriteshadow
    global shadowstale
    global shadowstep
    global shadowanim
    global estadomario
    global difficulty
    global powerupm
    global score1p
    global vidas
    global paused

    if paused:
        x.after(100, shadow_behaviour)
    else:

        if difficulty==1:
            d=200
        elif difficulty==2:
            d=150
        elif difficulty==3:
            d=100
        elif difficulty==4:
            d=50
        elif difficulty==5:
            d=0
        if estadoshadow=='creado':
            coordsshadowx1=int(canvas.coords(shadow)[0])
            coordsshadowy1=int(canvas.coords(shadow)[1])
            coordsshadowx2=int(canvas.coords(shadow)[2])
            coordsshadowy2=int(canvas.coords(shadow)[3])

            

            canvas.move(shadow,-5,0)
            canvas.move(spriteshadow, -5, 0)
            if estadomario!='muriendo':
                coordsmariox1=int(canvas.coords(mario)[0])
                coordsmarioy1= int(canvas.coords(mario)[1])
                coordsmariox2=int(canvas.coords(mario)[2])
                coordsmarioy2=int(canvas.coords(mario)[3])
                overlaps=canvas.find_overlapping(coordsshadowx1,coordsshadowy1,coordsshadowx2,coordsshadowy2)
                if coordsshadowy2>537 and coordsshadowy2<=540 and coordsmarioy2>537 and coordsmarioy2<=540 and len(overlaps)>=4 and coordsshadowx1<pipe2coordsx2-20 and ((coordsmariox1<= coordsshadowx2+5 and coordsmariox1 >=coordsshadowx1) or (coordsmariox2>=coordsshadowx1-5 and coordsmariox2<=coordsshadowx2)):
                    if not(powerupm):
                        mariodie()
                    else:
                        flipshadow()
                        shadowdie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
                elif coordsshadowy2<537 and coordsmarioy2<=coordsshadowy2 and coordsmarioy2> coordsshadowy1 and len(overlaps)>5 and ((coordsmariox1<= coordsshadowx2+5 and coordsmariox1 >=coordsshadowx1) or (coordsmariox2>=coordsshadowx1-5 and coordsmariox2<=coordsshadowx2)):
                    if not(powerupm):
                        mariodie()
                    else:
                        flipshadow()
                        shadowdie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
            if coordsshadowx1<pipe1coordsx2 and coordsshadowy2>537:
                canvas.delete(shadow)
                canvas.delete(spriteshadow)
                shadow=canvas.create_rectangle(1140, 75, 1180, coordsplat6y1, fill=None, width=0)
                estadoshadow='creado'
                shadowanim=1
                coordsshadowx1=int(canvas.coords(shadow)[0])
                coordsshadowy1=int(canvas.coords(shadow)[1])
                coordsshadowx2=int(canvas.coords(shadow)[2])
                coordsshadowy2=int(canvas.coords(shadow)[3])
                spriteshadow=canvas.create_image(coordsshadowx1+24, coordsshadowy1+25, image=shadowstale)

                score1p.set(score1p.get()-100)
                                                                                                                                   
            if shadowanim==1:
                canvas.delete(spriteshadow)
                spriteshadow=canvas.create_image(coordsshadowx1+24, coordsshadowy1+25, image=shadowstep)
                shadowanim-=1
            elif shadowanim==0:
                canvas.delete(spriteshadow)
                spriteshadow=canvas.create_image(coordsshadowx1+24, coordsshadowy1+25, image=shadowstale)
                shadowanim+=1
            if coordsshadowx2<0:
                canvas.move(shadow,1280,0)
            if coordsshadowx1<coordsplat6x1 and coordsshadowy2==coordsplat6y1:
                fallshadowplat6()
            elif coordsshadowx1<coordsplatcentrox1 and coordsshadowy2==coordsplatcentroy1:
                fallshadowplatcentro()
            elif coordsshadowx2<coordsplat2x1 and coordsshadowx1>coordsplat1x2 and coordsshadowy2==coordsplat2y1:
                fallshadowplat2()
        elif estadoshadow=='volteado':
            return None
        x.after(100+d,shadow_behaviour)
def fallshadowplat6():
    global shadow
    global spriteshadow
    canvas.tag_raise(shadow)
    canvas.tag_raise(spritemario)
    coordsshadowx1=int(canvas.coords(shadow)[0])
    coordsshadowy1=int(canvas.coords(shadow)[1])
    coordsshadowx2=int(canvas.coords(shadow)[2])
    coordsshadowy2=int(canvas.coords(shadow)[3])
    if coordsshadowy2==coordsplatcentroy1:
        return None
    else:
        x.after(3, fallshadowplat6)
        canvas.move(shadow,0,2)
        canvas.move(spriteshadow,0,2)

def fallshadowplatcentro():
    global shadow
    global spriteshadow
    coordsshadowx1=int(canvas.coords(shadow)[0])
    coordsshadowy1=int(canvas.coords(shadow)[1])
    coordsshadowx2=int(canvas.coords(shadow)[2])
    coordsshadowy2=int(canvas.coords(shadow)[3])
    if coordsshadowy2==coordsplat1y1:
        return None
    else:
        x.after(3, fallshadowplatcentro)
        canvas.move(shadow,0,2)
        canvas.move(spriteshadow,0,2)


def fallshadowplat2():
    global shadow
    global spriteshadow
    coordsshadowx1=int(canvas.coords(shadow)[0])
    coordsshadowy1=int(canvas.coords(shadow)[1])
    coordsshadowx2=int(canvas.coords(shadow)[2])
    coordsshadowy2=int(canvas.coords(shadow)[3])
    if coordsshadowy2>537:
        return None
    else:
        x.after(3, fallshadowplat2)
        canvas.move(shadow,0,2)
        canvas.move(spriteshadow,0,2)
def shadowdie():
    
    global estadoshadow
    global spriteshadow
    global shadow
    if estadoshadow==None:
        return None
    else:
        estadoshadow='atacado'
        coordsshadowy1=int(canvas.coords(shadow)[1])
        if coordsshadowy1>720:

        
            canvas.delete(spriteshadow)
            canvas.delete(shadow)
            estadoshadow=None
        else:


            canvas.move(shadow,0,2)
            canvas.move(spriteshadow,0,2)
            x.after(4, shadowdie)


def flipshadow():
    global shadow
    global estadoshadow
    global spriteshadow
    global shadowflipped
    global background
    global shadowflippedanim
    
    coordsshadowx1=int(canvas.coords(shadow)[0])
    coordsshadowy1=int(canvas.coords(shadow)[1])
    coordsshadowx2=int(canvas.coords(shadow)[2])
    coordsshadowy2=int(canvas.coords(shadow)[3])
    estadoshadow='volteado'
    canvas.delete(shadow)
    canvas.delete(spriteshadow)
    shadow=canvas.create_rectangle(coordsshadowx1-5,coordsshadowy1+10,coordsshadowx2+5,coordsshadowy2,width=0)
    coordsshadowx1=int(canvas.coords(shadow)[0])
    coordsshadowy1=int(canvas.coords(shadow)[1])
    coordsshadowx2=int(canvas.coords(shadow)[2])
    coordsshadowy2=int(canvas.coords(shadow)[3])
    spriteshadow=canvas.create_image(coordsshadowx1+26, coordsshadowy1+20, image=shadowflipped)
    shadowflippedanim=1
    canvas.tag_lower(spriteshadow)
    canvas.tag_lower(background)
    x.after(500, changeflipshadow)
    x.after(15000, unflipshadow)

def changeflipshadow():
    global estadoshadow
    global spriteshadow
    global shadowflipped
    global shadowflipped2
    global shadowflippedanim
    global estadoshadow
    global background
    global paused

    if paused:
        x.after(500, changeflipshadow)
    else:
        
        coordsshadowx1=int(canvas.coords(shadow)[0])
        coordsshadowy1=int(canvas.coords(shadow)[1])
        coordsshadowx2=int(canvas.coords(shadow)[2])
        coordsshadowy2=int(canvas.coords(shadow)[3])
        if estadoshadow!='volteado':
            return None
        else:
            if shadowflippedanim==1:
                canvas.delete(spriteshadow)
                spriteshadow= canvas.create_image(coordsshadowx1+26, coordsshadowy1+20, image=shadowflipped2)
                canvas.tag_lower(spriteshadow)
                canvas.tag_lower(background)
                shadowflippedanim-=1
            elif shadowflippedanim==0:
                canvas.delete(spriteshadow)
                spriteshadow= canvas.create_image(coordsshadowx1+26, coordsshadowy1+20, image=shadowflipped)
                canvas.tag_lower(spriteshadow)
                canvas.tag_lower(background)
                shadowflippedanim+=1
            x.after(500, changeflipshadow)
def unflipshadow():
    global estadoshadow
    global spriteshadow
    global shadowstale
    global shadow
    global shadowlife
    global paused

    if not paused:
        
        coordsshadowx1=int(canvas.coords(shadow)[0])
        coordsshadowy1=int(canvas.coords(shadow)[1])
        coordsshadowx2=int(canvas.coords(shadow)[2])
        coordsshadowy2=int(canvas.coords(shadow)[3])
        if estadoshadow!='volteado':
            return None
        
        canvas.delete(shadow)
        canvas.delete(spriteshadow)
        shadow=canvas.create_rectangle(coordsshadowx1+5, coordsshadowy1-10, coordsshadowx2-5, coordsshadowy2, width=0)
        coordsshadowx1=int(canvas.coords(shadow)[0])
        coordsshadowy1=int(canvas.coords(shadow)[1])
        coordsshadowx2=int(canvas.coords(shadow)[2])
        coordsshadowy2=int(canvas.coords(shadow)[3])
        spriteshadow=canvas.create_image(coordsshadowx1+24,coordsshadowy1+25, image=shadowstale)
        estadoshadow='creado'
        shadowlife=2
    x.after(2, shadow_behaviour)
def shadowhitfun():
##'''
##Función única para la Shadow Koopa. Crea una animación al golpearla por primera vez (puesto que esta resiste dos golpes)
##'''
    global estadoshadow
    global spriteshadow
    global shadowhit
    global shadowhit2
    global shadowlife
    global shadowhitanim
    global shadowanim
    estadoshadow='atacado'
    canvas.delete(spriteshadow)
    coordsshadowx1=int(canvas.coords(shadow)[0])
    coordsshadowy1=int(canvas.coords(shadow)[1])
    coordsshadowx2=int(canvas.coords(shadow)[2])
    coordsshadowy2=int(canvas.coords(shadow)[3])
    if shadowhitanim==4 or shadowhitanim==2:
        spriteshadow=canvas.create_image(coordsshadowx1+24,coordsshadowy1+25, image=shadowhit)
        shadowhitanim-=1
    elif shadowhitanim==3 or shadowhitanim==1:
        spriteshadow=canvas.create_image(coordsshadowx1+24,coordsshadowy1+25, image=shadowhit2)
        shadowhitanim-=1
    elif shadowhitanim==0:
        shadowlife-=1
        estadoshadow='creado'
        shadowanim=1
        spriteshadow=canvas.create_image(coordsshadowx1+24, coordsshadowy1+25, image=shadowstep)
        return None
    x.after(100,shadowhitfun)


############################SHY GUY################################
def shybehaviour():
    global shy
    global estadoshy
    global spriteshy
    global shystale
    global shystep
    global shyanim
    global shyhitanim
    global estadomario
    global difficulty
    global paused

    if paused:
        x.after(100, shybehaviour)
    else:
        


        if difficulty==1:
            d=200
        elif difficulty==2:
            d=150
        elif difficulty==3:
            d=100
        elif difficulty==4:
            d=50
        elif difficulty==5:
            d=0
        if estadoshy=='creado':
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1=int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])

            

            canvas.move(shy,5,0)
            canvas.move(spriteshy, 5, 0)
            if estadomario!='muriendo' and estadomario!='congelado':
                coordsmariox1=int(canvas.coords(mario)[0])
                coordsmarioy1= int(canvas.coords(mario)[1])
                coordsmariox2=int(canvas.coords(mario)[2])
                coordsmarioy2=int(canvas.coords(mario)[3])
                overlaps=canvas.find_overlapping(coordsshyx1,coordsshyy1,coordsshyx2,coordsshyy2)
                if coordsshyy2>537 and coordsshyy2<=540 and coordsmarioy2>537 and coordsmarioy2<=540 and len(overlaps)>=4 and coordsshyx1>pipe1coordsx2+20 and ((coordsmariox1<= coordsshyx2+5 and coordsmariox1>=coordsshyx1) or (coordsmariox2>=coordsshyx1-5 and coordsmariox2<=coordsshyx2)):
                    if not(powerupm):
                        freezemario()
                    else:
                        shyhitanim=4
                        shydie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
                elif coordsshyy2<537 and coordsmarioy2<=coordsshyy2 and coordsmarioy2> coordsshyy1 and len(overlaps)>5 and ((coordsmariox1<= coordsshyx2+5 and coordsmariox1 >=coordsshyx1) or (coordsmariox2>=coordsshyx1-5 and coordsmariox2<=coordsshyx2)):
                    if not(powerupm):
                        freezemario()
                    else:
                        shyhitanim=4
                        shydie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
            if coordsshyx1>pipe2coordsx1 and coordsshyy2>537:
                canvas.delete(shy)
                canvas.delete(spriteshy)
                shy=canvas.create_rectangle(100, 75, 140, coordsplat6y1, fill=None,width=0)
                estadoshy='creado'
                shyanim=1
                coordsshyx1=int(canvas.coords(shy)[0])
                coordsshyy1=int(canvas.coords(shy)[1])
                coordsshyx2=int(canvas.coords(shy)[2])
                coordsshyy2=int(canvas.coords(shy)[3])
                spriteshy=canvas.create_image(coordsshyx1+24, coordsshyy1+25, image=shystale)

                score1p.set(score1p.get()-100)      
                                                                                                                                   
            if shyanim==1:
                canvas.delete(spriteshy)
                spriteshy=canvas.create_image(coordsshyx1+24, coordsshyy1+30, image=shystep)
                shyanim-=1
            elif shyanim==0:
                canvas.delete(spriteshy)
                spriteshy=canvas.create_image(coordsshyx1+24, coordsshyy1+30, image=shystale)
                shyanim+=1
            if coordsshyx2>=1280:
                canvas.move(shy,-1280,0)
                canvas.move(spriteshy, -1280, 0)
            if coordsshyx1>coordsplat5x2 and coordsshyy2<=coordsplat5y1:
                fallshyplat5()
            elif coordsshyx1>coordsplatcentrox2 and coordsshyy2<=coordsplatcentroy1:
                fallshyplatcentro()
            elif coordsshyx1>coordsplat1x2 and coordsshyx2<coordsplat2x1  and coordsshyy2==coordsplat1y1:
                fallshyplat1()
        x.after(100+d,shybehaviour)
def fallshyplat5():
    global shy
    global spriteshy
    canvas.tag_raise(shy)
    canvas.tag_raise(spritemario)
    coordsshyx1=int(canvas.coords(shy)[0])
    coordsshyy1=int(canvas.coords(shy)[1])
    coordsshyx2=int(canvas.coords(shy)[2])
    coordsshyy2=int(canvas.coords(shy)[3])
    if coordsshyy2==coordsplatcentroy1:
        return None
    else:
        x.after(2, fallshyplat5)
        canvas.move(shy,0,2)
        canvas.move(spriteshy,0,2)
        
def fallshyplatcentro():
    global shy
    global spriteshy
    coordsshyx1=int(canvas.coords(shy)[0])
    coordsshyy1= int(canvas.coords(shy)[1])
    coordsshyx2=int(canvas.coords(shy)[2])
    coordsshyy2=int(canvas.coords(shy)[3])
    if coordsshyy2==coordsplat2y1:
        return None
    else:
        x.after(2, fallshyplatcentro)
        canvas.move(shy,0,2)
        canvas.move(spriteshy,0,2)
def fallshyplat1():
    global shy
    global spriteshy
    coordsshyx1=int(canvas.coords(shy)[0])
    coordsshyy1= int(canvas.coords(shy)[1])
    coordsshyx2=int(canvas.coords(shy)[2])
    coordsshyy2=int(canvas.coords(shy)[3])
    if coordsshyy2>537:
        return None
    else:
        x.after(2, fallshyplat1)
        canvas.move(shy,0,2)
def fireshy():
##'''
##Función única del Shy Guy en la que este dispara un proyectil que congela a Mario
##'''
    global estadoshy
    global spriteshy
    global shythrow
    global paused

    if paused:
        x.after(100, fireshy)
    else:
        
        if estadoshy=='creado':
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1= int(canvas.coords(shy)[1])
            estadoshy='disparando'
            canvas.delete(spriteshy)
            spriteshy=canvas.create_image(coordsshyx1+24, coordsshyy1+30, image=shythrow)
            x.after(500, shycontinue)
            x.after(5, projectile)
def shycontinue():
    global estadoshy
    estadoshy='creado'
    x.after(7000, shybehaviour)
    x.after(7500, fireshy)
def projectile():
##'''
##Función que mueve al proyectil del Shy Guy y lo desintegra al llegar al borde de la pantalla.
##'''
    global estadobala
    global bala
    global estadoshy
    global powerupm
    global paused

    if paused:
        x.after(2, projectile)
    else:
        
        if difficulty==1:
            d=20
        elif difficulty==2:
            d=15
        elif difficulty==3:
            d=10
        elif difficulty==4:
            d=5
        elif difficulty==5:
            d=0
        if estadobala== None and (estadoshy=='disparando' or estadoshy=='creado'):
            coordsshyx1=int(canvas.coords(shy)[0])
            coordsshyy1= int(canvas.coords(shy)[1])
            coordsshyx2=int(canvas.coords(shy)[2])
            coordsshyy2=int(canvas.coords(shy)[3])
            bala=canvas.create_oval(coordsshyx2+10, coordsshyy1+10, coordsshyx2+30,coordsshyy1+30, fill='white')

            estadobala='creado'
            x.after(10+d, projectile) 
        elif estadobala=='creado':
            canvas.move(bala, 1, 0)
            coordsbalax1=int(canvas.coords(bala)[0])
            coordsbalay1= int(canvas.coords(bala)[1])
            coordsbalax2=int(canvas.coords(bala)[2])
            coordsbalay2=int(canvas.coords(bala)[3])
            overlaps=canvas.find_overlapping(coordsbalax1,coordsbalay1,coordsbalax2,coordsbalay2)
            if estadomario!='muriendo' and estadomario!='congelado':
                coordsmariox1=int(canvas.coords(mario)[0])
                coordsmarioy1= int(canvas.coords(mario)[1])
                coordsmariox2=int(canvas.coords(mario)[2])
                coordsmarioy2=int(canvas.coords(mario)[3])
                if len(overlaps)>=3 and ((coordsmariox1<=coordsbalax2+5 and coordsmariox1>=coordsbalax1) or (coordsmariox1>=coordsbalax1-5 and coordsmariox1<=coordsbalax2)):
                    canvas.delete(bala)
                    estadobala=None
                    if not powerupm:
                        freezemario()
            if coordsbalax2>1285:
                canvas.delete(bala)
                estadobala= None
            else:
                x.after(2+d, projectile)

def shydie():
    global estadoshy
    global spriteshy
    global shyhit1
    global shyhit2
    global shyhitanim
    estadoshy='atacado'
    canvas.delete(spriteshy)
    coordsshyx1=int(canvas.coords(shy)[0])
    coordsshyy1=int(canvas.coords(shy)[1])
    coordsshyx2=int(canvas.coords(shy)[2])
    coordsshyy2=int(canvas.coords(shy)[3])
    if shyhitanim==4 or shyhitanim==2:
        spriteshy=canvas.create_image(coordsshyx1+24,coordsshyy1+25, image=shyhit1)
        shyhitanim-=1
    elif shyhitanim==3 or shyhitanim==1:
        spriteshy=canvas.create_image(coordsshyx1+24,coordsshyy1+25, image=shyhit2)
        shyhitanim-=1
    elif shyhitanim==0:
        estadoshy=None
        canvas.delete(shy)
        canvas.delete(spriteshy)
        return None
    x.after(100,shydie)
    
#########################KOOPA TROOPA##############################
def koopa1_behaviour():
    global koopa1
    global estadokoopa1
    global spritekoopa
    global koopastale
    global koopastep
    global koopaanim
    global estadomario
    global difficulty
    global paused

    if paused:
        x.after(100, koopa1_behaviour)
    else:

        if difficulty==1:
            d=200
        elif difficulty==2:
            d=150
        elif difficulty==3:
            d=100
        elif difficulty==4:
            d=50
        elif difficulty==5:
            d=0
        if estadokoopa1=='creado':
            coordskoopa1x1=int(canvas.coords(koopa1)[0])
            coordskoopa1y1=int(canvas.coords(koopa1)[1])
            coordskoopa1x2=int(canvas.coords(koopa1)[2])
            coordskoopa1y2=int(canvas.coords(koopa1)[3])

            

            canvas.move(koopa1,5,0)
            canvas.move(spritekoopa, 5, 0)
            if estadomario!='muriendo':
                coordsmariox1=int(canvas.coords(mario)[0])
                coordsmarioy1= int(canvas.coords(mario)[1])
                coordsmariox2=int(canvas.coords(mario)[2])
                coordsmarioy2=int(canvas.coords(mario)[3])
                overlaps=canvas.find_overlapping(coordskoopa1x1,coordskoopa1y1,coordskoopa1x2,coordskoopa1y2)
                if coordskoopa1y2>537 and coordskoopa1y2<=540 and coordsmarioy2>537 and coordsmarioy2<=540 and len(overlaps)>=4 and coordskoopa1x1>pipe1coordsx2+20 and ((coordsmariox1<= coordskoopa1x2+5 and coordsmariox1>=coordskoopa1x1) or (coordsmariox1>=coordskoopa1x1-5 and coordsmariox1<=coordskoopa1x2 )):
                    if not(powerupm):
                        mariodie()
                    else:
                        Koopa1_flip()
                        koopadie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
                elif coordskoopa1y2<537 and coordsmarioy2<=coordskoopa1y2 and coordsmarioy2> coordskoopa1y1 and len(overlaps)>5 and ((coordsmariox1<= coordskoopa1x2+5 and coordsmariox1 >=coordskoopa1x1) or (coordsmariox2>=coordskoopa1x1-5 and coordsmariox2<=coordskoopa1x2)):
                    if not(powerupm):
                        mariodie()
                    else:
                        Koopa1_flip()
                        koopadie()
                        score1p.set(score1p.get()+100)
                        if score1p.get() == 900:
                            vidas+=1
                            score1p.set(0)
            if coordskoopa1x1>pipe2coordsx1 and coordskoopa1y2>537:
                canvas.delete(koopa1)
                canvas.delete(spritekoopa)
                koopa1=canvas.create_rectangle(100, 75, 140, coordsplat6y1, fill=None,width=0)
                estadokoopa='creado'
                koopaanim=1
                coordskoopa1x1=int(canvas.coords(koopa1)[0])
                coordskoopa1y1=int(canvas.coords(koopa1)[1])
                coordskoopax2=int(canvas.coords(koopa1)[2])
                coordskoopay2=int(canvas.coords(koopa1)[3])
                spritekoopa=canvas.create_image(coordskoopa1x1+24, coordskoopa1y1+25, image=koopastale)

                score1p.set(score1p.get()-100)    
                                                                                                                                   
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
        x.after(100+d,koopa1_behaviour)

def Koopa1_flip():
    global koopa1
    global estadokoopa1
    global spritekoopa
    global koopaflipped
    global koopaflippedanim
    global background
    global unfliptime
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    estadokoopa1='volteado'
    canvas.delete(koopa1)
    canvas.delete(spritekoopa)
    koopa1=canvas.create_rectangle(coordskoopa1x1-5,coordskoopa1y1+10,coordskoopa1x2+5,coordskoopa1y2,width=0)
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    spritekoopa=canvas.create_image(coordskoopa1x1+26, coordskoopa1y1+20, image=koopaflipped)
    koopaflippedanim=1
    canvas.tag_lower(spritekoopa)
    canvas.tag_lower(background)
    x.after(500, changeflipkoopa)
    x.after(15000, unflipkoopa)

    
def changeflipkoopa():
    global estadokoopa1
    global spritekoopa
    global koopaflipped
    global koopaflipped2
    global koopaflippedanim
    global estadokoopa1
    global background
    global paused

    
    if paused:
        x.after(500, changeflipkoopa)
    else:
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
                canvas.tag_lower(spritekoopa)
                canvas.tag_lower(background)
                koopaflippedanim-=1
            elif koopaflippedanim==0:
                canvas.delete(spritekoopa)
                spritekoopa= canvas.create_image(coordskoopa1x1+26, coordskoopa1y1+20, image=koopaflipped)
                canvas.tag_lower(spritekoopa)
                canvas.tag_lower(background)
                koopaflippedanim+=1
            x.after(500, changeflipkoopa)
        
def unflipkoopa():
    global estadokoopa1
    global spritekoopa
    global koopastale
    global koopa1
    global paused
    if paused:
        x.after(5000, unflipkoopa)
    else:
        
        coordskoopa1x1=int(canvas.coords(koopa1)[0])
        coordskoopa1y1= int(canvas.coords(koopa1)[1])
        coordskoopa1x2=int(canvas.coords(koopa1)[2])
        coordskoopa1y2=int(canvas.coords(koopa1)[3])
        if estadokoopa1!='volteado':
            return None
        
        canvas.delete(koopa1)
        canvas.delete(spritekoopa)
        koopa1=canvas.create_rectangle(coordskoopa1x1+5, coordskoopa1y1-10, coordskoopa1x2-5, coordskoopa1y2, width=0)
        coordskoopa1x1=int(canvas.coords(koopa1)[0])
        coordskoopa1y1= int(canvas.coords(koopa1)[1])
        coordskoopa1x2=int(canvas.coords(koopa1)[2])
        coordskoopa1y2=int(canvas.coords(koopa1)[3])
        spritekoopa=canvas.create_image(coordskoopa1x1+24,coordskoopa1y1+25, image=koopastale)
        estadokoopa1='creado'
        x.after(2, koopa1_behaviour)
    
    
def fallkoopaplat5():
    global koopa1
    global spritekoopa
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
        canvas.move(spritekoopa,0,2)

def fallkoopaplatcentro():
    global koopa1
    global spritekoopa
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    if coordskoopa1y2==coordsplat2y1:
        return None
    else:
        x.after(2, fallkoopaplatcentro)
        canvas.move(koopa1,0,2)
        canvas.move(spritekoopa,0,2)


def fallkoopaplat1():
    global koopa1
    global spritekoopa
    coordskoopa1x1=int(canvas.coords(koopa1)[0])
    coordskoopa1y1= int(canvas.coords(koopa1)[1])
    coordskoopa1x2=int(canvas.coords(koopa1)[2])
    coordskoopa1y2=int(canvas.coords(koopa1)[3])
    if coordskoopa1y2>537:
        return None
    else:
        x.after(2, fallkoopaplat1)
        canvas.move(koopa1,0,2)
        canvas.move(spritekoopa,0,2)


def koopadie():
    
    global coordsreferencekoopa
    global estadokoopa1
    global spritekoopa
    global koopa1
    global estadokoopa1
    global refkoopa
    if estadokoopa1==None:
        return None
    else:
        estadokoopa1='atacado'
        coordskoopa1x1=int(canvas.coords(koopa1)[0])
        coordskoopa1y1= int(canvas.coords(koopa1)[1])
        coordskoopa1x2=int(canvas.coords(koopa1)[2])
        coordskoopa1y2=int(canvas.coords(koopa1)[3])
        if coordskoopa1y1>720:

        
            canvas.delete(spritekoopa)
            canvas.delete(koopa1)
            estadokoopa1=None
            refkoopa=0
        else:


            canvas.move(koopa1,0,2)
            canvas.move(spritekoopa,0,2)
            x.after(4, koopadie)


###########POWER STAR################
def SpawnPowerStar():
##'''
##Crea una Power Star, responsable de ser el powerup de invencibilidad del juego
##'''
    global estadopower
    global powersprite
    global power
    global spritepower
    global paused
    if paused:
        x.after(500, SpawnPowerStar)
    else:
        

        if estadopower==None:
            estadopower='creado'
            power=canvas.create_rectangle(coordsplat1x1+175, coordsplat1y1-85, coordsplat1x1+225, coordsplat1y1-45, width=0)
            spritepower=canvas.create_image(coordsplat1x1+200, coordsplat1y1-65,image=powersprite)

def pickpowerm():
##'''
##Hace que Mario recoja la estrella. Elimina a esta, cambia la música y le asigna el powerup a Mario
##'''
    global powerupm
    global estadopower
    global spritepower
    global power
    global mainm
    canvas.delete(power)
    canvas.delete(spritepower)
    estadopower=None
    powerupm=True
    mainm=threading.Thread(target=powermusic)
    mainm.start()
    
    canvas.after(30000, unpower)
def unpower():
    global powerupm
    global mainm
    powerupm=False
    mainm=threading.Thread(target=mainmusic)
    mainm.start()
    canvas.after(60000, SpawnPowerStar)


################POW###############

def powpress():
##'''
##Función de presionar el POW. Funciona 3 veces y voltea a todos los enemigos que esten en contacto con el suelo
##'''
    global rempow
    global estadoparatroopa
    global estadokoopa1
    global estadoshy
    global estadoshadow
    global shadowlife
    global shadowhitanim
    global shyhitanim
    global powsprite
    if rempow>0:
        
        rempow-=1
        if rempow==0:
            canvas.delete(powsprite)
        if estadokoopa1=='creado':
            coordskoopa1y2=int(canvas.coords(koopa1)[3])
            if coordskoopa1y2==coordsplat1y1 or coordskoopa1y2==coordsplat3y1 or coordskoopa1y2==coordsplat5y1 or (coordskoopa1y2<540 and coordskoopa1y2>=537):
                Koopa1_flip()
        elif estadokoopa1=='volteado':
            coordskoopa1y2=int(canvas.coords(koopa1)[3])            
            if coordskoopa1y2==coordsplat1y1 or coordskoopa1y2==coordsplat3y1 or coordskoopa1y2==coordsplat5y1 or (coordskoopa1y2<540 and coordskoopa1>=537):
                unflipkoopa()
        if estadoparatroopa=='creado':
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])
            if coordsparatroopay2==coordsplat1y1 or coordsparatroopay2==coordsplat3y1 or coordsparatroopay2==coordsplat5y1 or (coordsparatroopay2<540 and coordsparatroopay2>=537):
                flipparatroopa()
        elif estadoparatroopa=='volteado':
            coordsparatroopay2=int(canvas.coords(paratroopa)[3])            
            if coordsparatroopay2==coordsplat1y1 or coordsparatroopay2==coordsplat3y1 or coordsparatroopay2==coordsplat5y1 or (coordsparatroopay2<540 and coordsparatroopay2>=537):
                unflipparatroopa()

                
        if estadoshadow=='creado':
            coordsshadowy2=int(canvas.coords(shadow)[3])
            if coordsshadowy2==coordsplat1y1 or coordsshadowy2==coordsplat3y1 or coordsshadowy2==coordsplat5y1 or (coordsshadowy2<540 and coordsshadowy2>=537):
                    if shadowlife==2:
                        shadowhitanim=4
                        shadowhitfun()
                    elif shadowlife==1:
                        flipshadow()
        elif estadoshadow=='volteado':
            coordsshadowy2=int(canvas.coords(shadow)[3])            
            if coordsshadowy2==coordsplat1y1 or coordsshadowy2==coordsplat3y1 or coordsshadowy2==coordsplat5y1 or (coordsshadowy2<540 and coordsshadowy2>=537):
                unflipshadow()
                
        if estadoshy=='creado':
            coordsshyy2=int(canvas.coords(shy)[3])
            if coordsshyy2==coordsplat1y1 or coordsshyy2==coordsplat3y1 or coordsshyy2==coordsplat5y1 or (coordsshyy2<540 and coordsshy>=537):
                shyhitanim=4
                shydie()
            
######Funcionalidad Varia#####


def bindings():
##'''
##Función para abreviar los 'bindings' necesarios en el juego.
##'''
    canvas.bind('<a>', keym)
    canvas.bind('<d>', keym)
    canvas.bind('<w>', jumpm)
    
##'''
##Funciones de música: Las hice en funciones aparte para facilitar el uso de threads.
##'''
def Initialmusic():
    winsound.PlaySound('Menu.wav', winsound.SND_ASYNC)
def mainmusic():
    winsound.PlaySound('Maint.wav', winsound.SND_ASYNC|winsound.SND_LOOP)
def powermusic():
    winsound.PlaySound('powertheme.wav',winsound.SND_ASYNC)
def gameovermusic():
    winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)


def menuinic(event):
##'''
##Función correspondiente al menú principal del juego, que permite seleccionar entre el juego y cambiar la dificultad.
##'''
    global state
    global men
    global menuopt
    global menuini
    global dif1
    global txt
    if event.char=='s':
        

        if state==0:
            menu.delete(men)
            men=menu.create_image(0,0,image=menuopt, anchor=NW)
            state+=1
        elif state==1:
            menu.delete(men)
            men=menu.create_image(0,0,image=menuini,anchor=NW)
            state-=1
    elif event.char=='w':
        
        if state==0:
            menu.delete(men)
            men=menu.create_image(0,0,image=menuopt, anchor=NW)
            state+=1
        elif state==1:
            menu.delete(men)
            men=menu.create_image(0,0,image=menuini, anchor=NW)
            state-=1
    else:
        
        if state==1:
            menu.delete(men)
            men=menu.create_image(0,0,image=dif1,anchor=NW)
            menu.bind('<s>', ignore)
            menu.bind('<w>', ignore)
            menu.bind('<Return>', dif)
            menu.bind('<a>', dif)
            menu.bind('<d>', dif)
        elif state==0:
            menu.delete(men)
            men=menu.create_image(0,0, image=load1, anchor=NW)        
            menu.bind('<s>', ignore)
            menu.bind('<w>', ignore)
            menu.bind('<Return>', loadscreen)
            menu.bind('<a>', loadscreen)
            menu.bind('<d>', loadscreen)
            state=0





            
def loadscreen(event):
##'''
##Función correspondiente a la pantalla que pregunta si el jugador quiere cargar la partida.
##'''
    global state
    global men
    global load1
    global load2
    global txt
    global state
    
    if event.char=='d':
        
        if state==0:
            state=1
            menu.delete(men)
            men=menu.create_image(0,0,image=load2, anchor=NW)
            
        elif state==1:
            state-=1
            menu.delete(men)
            men=menu.create_image(0,0,image=load1,anchor=NW)
    elif event.char=='a':
        
        if state==0:
            state+=1
            menu.delete(men)
            men=menu.create_image(0,0,image=load2, anchor=NW)
            
        elif state==1:
            state-=1
            menu.delete(men)
            men=menu.create_image(0,0,image=load1,anchor=NW)
    else:
        if state==1:
            menu.delete(men)
            men=menu.create_image(0,0,image=nametype, anchor=NW)
            menu.bind('<s>', ignore)
            menu.bind('<w>', ignore)
            menu.bind('<Return>', destruirprueba)
            menu.bind('<a>', ignore)
            menu.bind('<d>', ignore)
            txt=Entry(menu, textvariable=nombre1)
            bot=Button(menu, text='Lets go!', command=destruirprueba)
            menu.create_window(700,360, window=bot)
            menu.create_window(600, 360, window=txt)
        elif state==0:
            load()









def save():
##'''
##Función que guarda el estado del juego en el archivo save.txt
##'''
    archivo=open('save.txt','w')
    savedata=[]
    global estadomario
    global mario
    global estadokoopa1
    global koopa1
    global shadow
    global shy
    global paratroopa
    global estadoshy
    global estadoshadow
    global estadoparatroopa
    global rempow
    global shadowlife
    global score1p
    global q1
    global vidas1
    global difficulty
    global monstruos
    savedata.append(estadomario)
    if estadokoopa1=='atacado':
        estadokoopa1=None
    if estadoparatroopa=='atacado':
        estadoparatroopa=None
    if estadoshadow=='atacado':
        estadoshadow=None
    if estadoshy=='atacado':
        estadoshy=None
    if estadomario!='muriendo':
        
        coordsmario=canvas.coords(mario)
    else:
        coordsmario=[0,490,51,540]
    savedata.append(coordsmario)

    
    savedata.append(estadokoopa1)
    if estadokoopa1!=None:
        coordskoopa=canvas.coords(koopa1)
    else:
        coordskoopa=[0,0,0,0]
    savedata.append(coordskoopa)

    
    savedata.append(estadoparatroopa)
    if estadoparatroopa!=None:
        coordsparatroopa=canvas.coords(paratroopa)
    else:
        coordsparatroopa=[0,0,0,0]
    savedata.append(coordsparatroopa)

    
    savedata.append(estadoshadow)
    if estadoshadow!=None:
        coordsshadow=canvas.coords(shadow)
    else:
        coordsshadow=[0,0,0,0]
    savedata.append(coordsshadow)
    savedata.append(shadowlife)

    
    savedata.append(estadoshy)
    if estadoshy!=None:
        coordsshy=canvas.coords(shy)
    else:
        coordsshy=[0,0,0,0]
    savedata.append(coordsshy)

    savedata.append(rempow)
    savedata.append(score1p.get())
    savedata.append(q1)
    savedata.append(vidas1.get())
    savedata.append(difficulty)
    savedata.append(monstruos)

    archivo.write(str(savedata))
    archivo.close()
    


def pause(event):
##'''
##Función que pausa el juego y despliega el menú de pausa. También corresponde al manejo de este menú.
##'''
    global paused
    global pausemenu1
    global pausemenu2
    global pausemen
    global state
    if not paused:
        paused=True
        pausemen=canvas.create_image(1280,0,image=pausemenu1, anchor=NE)
        canvas.bind('<a>', ignore)
        canvas.bind('<d>', ignore)
        canvas.bind('<s>', pause)
        canvas.bind('<w>', pause)
        state=0
    else:
        if event.char=='w' or event.char=='s':
            if state==0:
                canvas.delete(pausemen)
                pausemen=canvas.create_image(1280,0,image=pausemenu2, anchor=NE)
                state +=1
            elif state==1:
                canvas.delete(pausemen)
                pausemen=canvas.create_image(1280,0,image=pausemenu1, anchor=NE)
                state -=1                
        else:
            if state==0:
                canvas.delete(pausemen)
                paused=False
                bindings()
            elif state==1:
                save()
                x.destroy()
                quit()
        
                
    
        
    
    


def dif(event):
##'''
##Función que corresponde a la pantalla en donde el jugador selecciona la dificultad
##'''
    global difficulty
    global men
    global dif1
    global dif2
    global dif3
    global dif4
    global dif5
    global state
    if event.char=='d':
        if difficulty ==5:
            menu.delete(men)
            men=menu.create_image(0,0,image=dif1, anchor=NW)
            difficulty=1
        else:
            menu.delete(men)
            if difficulty==1:
                men=menu.create_image(0,0,image=dif2, anchor=NW)
            elif difficulty ==2:
                men=menu.create_image(0,0,image=dif3, anchor=NW)
            elif difficulty==3:
                men=menu.create_image(0,0,image=dif4, anchor=NW)
            elif difficulty==4:
                men=menu.create_image(0,0,image=dif5, anchor=NW)
            difficulty+=1
    elif event.char=='a':
        
        if difficulty ==1:
            menu.delete(men)
            men=menu.create_image(0,0,image=dif5, anchor=NW)
            difficulty=5
        else:
            menu.delete(men)
            if difficulty==5:
                men=menu.create_image(0,0,image=dif4, anchor=NW)
            elif difficulty ==2:
                men=menu.create_image(0,0,image=dif1, anchor=NW)
            elif difficulty==3:
                men=menu.create_image(0,0,image=dif2, anchor=NW)
            elif difficulty==4:
                men=menu.create_image(0,0,image=dif3, anchor=NW)
            difficulty-=1
    else:
        menu.bind('<a>', ignore)
        menu.bind('<d>', ignore)
        menu.bind('<w>', menuinic)
        menu.bind('<s>', menuinic)
        menu.bind('<Return>', menuinic)
        state=0
        menu.delete(men)
        men=menu.create_image(0,0,image=menuini, anchor=NW)
        
    
        



        

def destruirprueba():
##'''
##Función principal del juego, se crea el canvas con las figuras iniciales y se definen todas las constantes y archivos necesarios para la correcta ejecución de este. 
##'''
    global nombre1, score1p, scorep1, vidas1
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

    global pipe2
    global pipe2coordsx1
    global pipe2coordsx2
    global pipe2coordsy1
    global pipe2coordsy2
    global pipesprite2

    global POW
    global powsprite
    global coordspowx1
    global coordspowy1
    global coordspowx2
    global coordspowy2
    global rempow
    global spritepow

    global monstruos

    global koopastale
    global koopastep
    global koopaflipped
    global koopaflipped2

    global estadoparatroopa
    global paratroopastale
    global paratroopaflap
    global paratroopaflipped
    global paratroopaflipped2


    global estadoshadow
    global shadowstale
    global shadowstep
    global shadowflipped
    global shadowflipped2
    global shadowhit
    global shadowhit2
    global shadowlife

    global estadoshy
    global shystale
    global shystep
    global shyhit1
    global shyhit2
    global shythrow

    global estadobala

    
    global x
    global imagenmarioderecha
    global spritemario
    global estadomario
    global imagenmarioizquierda
    global imagenmariosaltoizquierda
    global imagenmariosaltoderecha
    global imagenmarioholdizquierda
    global imagenmarioholdderecha
    global imagenmariohitizquierda
    global imagenmariohitderecha
    global mariodieleft
    global mariodieright
    global mariodeadleft
    global mariodeadright
    global frozenmario

    global background
    global addscore
    global estadopower
    global powersprite
    global powerupm
    global vidas1

   # global musica1


    global paused
    global pausemenu1
    global pausemenu2
    global q1

    
    x= Crear_Ventana()
    mainm=threading.Thread(target=mainmusic)
    mainm.start()
    x.after(5000, spawn_monster)
    estadokoopa1=None
    estadoparatroopa=None
    estadoshadow=None
    estadoshy=None
    estadobala=None
    estadopower=None
    powerupm=False
    paused=False
    shadowlife=0
    rempow=3
    canvas= Canvas(x, width=1280, height=720)
    canvas.focus_set()
    monstruos=4+difficulty #No. de monstruos en el nivel
    estadomario='derecha'
    canvas.bind('<a>', keym)
    canvas.bind('<d>', keym)
    canvas.bind('<w>', jumpm)
    canvas.bind('<Return>', pause)
    addscore=True
    q1=nombre1.get()
    nomb1=Label(canvas, text=q1, fg='white', bg='black')
    score1p=IntVar()
    scorep1=Label(canvas, textvariable=score1p, fg='white', bg='black')
    canvas.create_window(100, 600, window=scorep1)
    nomb1.pack()
    canvas.create_window(50,600,window=nomb1)
    mario= canvas.create_rectangle(0,490,51,540,fill=None,width=0 )

    x.after(5000, SpawnPowerStar)
    vidas1=IntVar()
    v1=Label(canvas, textvariable=vidas1, fg='white', bg='black')
    canvas.create_window(150,600, window=v1)
    vidas1.set(3)
    
    canvas.pack()

    ####Plataformas####
    plat1= canvas.create_rectangle(1,415, 400, 440, fill= 'brown')
    plat2= canvas.create_rectangle(820, 415, 1280, 440, fill='brown')
    plat3= canvas.create_rectangle(1,275, 150, 300, fill='brown')
    plat4= canvas.create_rectangle(1130,275,1280,300, fill='brown')
    platcentro= canvas.create_rectangle(380,275,840,300,fill='brown')
    plat5= canvas.create_rectangle(1,125, 550, 150, fill='brown')
    plat6= canvas.create_rectangle(730, 125, 1280, 150, fill='brown')

    ####Bloque POW####
    POW= canvas.create_rectangle(590,405,630,440, fill='grey')
    spritepow=PhotoImage(file='powsprite.gif')
    


    ###Sprites de Mario##
    imagenmarioderecha= PhotoImage(file='staleright.gif')
    imagenmarioizquierda= PhotoImage(file='staleleft.gif')
    imagenmariosaltoizquierda= PhotoImage(file='jumpleft.gif')
    imagenmariosaltoderecha=PhotoImage(file='jumpright.gif')
    imagenmarioholdizquierda=PhotoImage(file='mariohammerholdleft.gif')
    imagenmarioholdderecha=PhotoImage(file='mariohammerholdright.gif')
    imagenmariohitizquierda=PhotoImage(file='mariohammerhitleft.gif')
    imagenmariohitderecha=PhotoImage(file='mariohammerhitright.gif')
    mariodieleft=PhotoImage(file='mariodieleft.gif')
    mariodieright=PhotoImage(file='mariodieright.gif')
    mariodeadleft=PhotoImage(file='mariodeadleft.gif')
    mariodeadright=PhotoImage(file='mariodeadright.gif')
    frozenmario=PhotoImage(file='frozenmario.gif')


    ###Texturas del entorno y fondo####
    pipeleft=PhotoImage(file='pipeleft.gif')
    piperight=PhotoImage(file='piperight.gif')
    back=PhotoImage(file='background.gif')
    background=canvas.create_image(0,0,image=back, anchor=NW)
    canvas.tag_lower(background)


    ###Sprites de la Koopa Troopa###
    koopastale=PhotoImage(file='koopastale.gif')
    koopastep=PhotoImage(file='koopastep.gif')
    koopaflipped=PhotoImage(file='koopaflipped.gif')
    koopaflipped2=PhotoImage(file='koopaflipped2.gif')


    ###Sprites de la Paratroopa###
    paratroopastale=PhotoImage(file='paratroopastale.gif')
    paratroopaflap=PhotoImage(file='paratroopaflap.gif')
    paratroopaflipped=PhotoImage(file='paratroopaflipped1.gif')
    paratroopaflipped2=PhotoImage(file='Paratroopaflipped2.gif')


    ###Sprites de la Shadow Koopa###
    shadowstale=PhotoImage(file='Shadowtroopastale.gif')
    shadowstep=PhotoImage(file='Shadowkoopastep.gif')
    shadowflipped=PhotoImage(file='shadowkoopaflipped.gif')
    shadowflipped2=PhotoImage(file='shadowkoopaflipped2.gif')
    shadowhit=PhotoImage(file='shadowkoopahit1.gif')
    shadowhit2=PhotoImage(file='shadowkoopahit2.gif')

    ###Sprites del Shy Guy###
    shystale=PhotoImage(file='shyguystale.gif')
    shystep=PhotoImage(file='shyguystep.gif')
    shyhit1=PhotoImage(file='shyguyhit.gif')
    shyhit2=PhotoImage(file='shyguyhit2.gif')
    shythrow=PhotoImage(file='shyguythrow.gif')

    ###Power Star###
    powersprite=PhotoImage(file='powerstar.gif')

    ###Menú de Pausa###
    pausemenu1=PhotoImage(file='pausemenu1.gif')
    pausemenu2=PhotoImage(file='pausemenu2.gif')



    
    ###Definición de constantes necesarias para el funcionamiento del juego###
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

    pipe2=canvas.create_rectangle(1145,20, 1280, coordsplat6y1, fill=None, width=0)
    pipe2coordsx1= int(canvas.coords(pipe2)[0])
    pipe2coordsx2= int(canvas.coords(pipe2)[2])
    pipe2coordsy1= int(canvas.coords(pipe2)[1])
    pipe2coordsy2= int(canvas.coords(pipe2)[3])
    pipesprite2=canvas.create_image(pipe2coordsx1+65,pipe2coordsy1+53, image=pipeleft)

    pipe3=canvas.create_rectangle(0,445, 136, 560, fill=None, width=0)
    pipe3coordsx1= int(canvas.coords(pipe3)[0])
    pipe3coordsx2= int(canvas.coords(pipe3)[2])
    pipe3coordsy1= int(canvas.coords(pipe3)[1])
    pipe3coordsy2= int(canvas.coords(pipe3)[3])
    pipesprite3=canvas.create_image(pipe3coordsx1+65,pipe3coordsy1+53, image=piperight)

    pipe4=canvas.create_rectangle(1145,445, 1280, 560, fill=None, width=0)
    pipe4coordsx1= int(canvas.coords(pipe4)[0])
    pipe4coordsx2= int(canvas.coords(pipe4)[2])
    pipe4coordsy1= int(canvas.coords(pipe4)[1])
    pipe4coordsy2= int(canvas.coords(pipe4)[3])
    pipesprite4=canvas.create_image(pipe4coordsx1+65,pipe4coordsy1+53, image=pipeleft)

    coordspowx1=int(canvas.coords(POW)[0])
    coordspowy1=int(canvas.coords(POW)[1])+1
    coordspowx2=int(canvas.coords(POW)[2])-2
    coordspowy2=int(canvas.coords(POW)[3])

    

    powsprite=canvas.create_image(coordspowx1+20,coordspowy1+10, image=spritepow)
    spritemario=canvas.create_image(coordsmariox1glob+25,coordsmarioy2glob-27, image=imagenmarioderecha)
    
    
    

    x.mainloop()


def load():
##'''
##Función casi igual a destruirprueba(), sólo que esta incorpora los datos guardados en el save para cargar efectivamente la partida.
##'''
    global nombre1, score1p, scorep1, vidas1
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

    global pipe2
    global pipe2coordsx1
    global pipe2coordsx2
    global pipe2coordsy1
    global pipe2coordsy2
    global pipesprite2

    global POW
    global powsprite
    global coordspowx1
    global coordspowy1
    global coordspowx2
    global coordspowy2
    global rempow
    global spritepow

    global monstruos

    global koopastale
    global koopastep
    global koopaflipped
    global koopaflipped2

    global estadoparatroopa
    global paratroopastale
    global paratroopaflap
    global paratroopaflipped
    global paratroopaflipped2


    global estadoshadow
    global shadowstale
    global shadowstep
    global shadowflipped
    global shadowflipped2
    global shadowhit
    global shadowhit2
    global shadowlife

    global estadoshy
    global shystale
    global shystep
    global shyhit1
    global shyhit2
    global shythrow

    global estadobala

    
    global x
    global imagenmarioderecha
    global spritemario
    global estadomario
    global imagenmarioizquierda
    global imagenmariosaltoizquierda
    global imagenmariosaltoderecha
    global imagenmarioholdizquierda
    global imagenmarioholdderecha
    global imagenmariohitizquierda
    global imagenmariohitderecha
    global mariodieleft
    global mariodieright
    global mariodeadleft
    global mariodeadright
    global frozenmario

    global background
    global addscore
    global estadopower
    global powersprite
    global powerupm

    
    global paused
    global pausemenu1
    global pausemenu2
    global difficulty
    global q1



    global koopa1
    global spritekoopa
    global paratroopa
    global spriteparatroopa
    global shadow
    global spriteshadow
    global shy
    global spriteshy
    global koopaanim
    global paratroopaanim
    global shadowanim
    global shyanim
    archivo=open('save.txt','r')
    data= ast.literal_eval(archivo.read())
    archivo.close()
    x= Crear_Ventana()
    difficulty=data[15]
    mainm=threading.Thread(target=mainmusic)
    mainm.start()
    x.after(5000, spawn_monster)
    estadokoopa1=data[2]
    estadoparatroopa=data[4]
    estadoshadow=data[6]
    estadoshy=data[9]
    estadobala=None
    estadopower=None
    powerupm=False
    paused=False
    shadowlife=data[8]
    rempow=data[11]
    canvas= Canvas(x, width=1280, height=720)
    canvas.focus_set()
    monstruos=data[16] #No. de monstruos en el nivel
    estadomario=data[0]
    canvas.bind('<a>', keym)
    canvas.bind('<d>', keym)
    canvas.bind('<w>', jumpm)
    canvas.bind('<Return>', pause)
    q1=str(data[13])
    nomb1=Label(canvas, text=q1, fg='white', bg='black')
    score1p=IntVar()
    score1p.set(data[12])
    scorep1=Label(canvas, textvariable=score1p, fg='white', bg='black')
    canvas.create_window(100, 600, window=scorep1)
    nomb1.pack()
    canvas.create_window(50,600,window=nomb1)
    x.after(50000, SpawnPowerStar)
    vidas1=IntVar()
    v1=Label(canvas, textvariable=vidas1, fg='white', bg='black')
    canvas.create_window(150,600, window=v1)
    vidas1.set(data[14])
    

    mario=canvas.create_rectangle(data[1][0],data[1][1],data[1][2],data[1][3], width=0)
    
    canvas.pack()

    ####Plataformas####
    plat1= canvas.create_rectangle(1,415, 400, 440, fill= 'brown')
    plat2= canvas.create_rectangle(820, 415, 1280, 440, fill='brown')
    plat3= canvas.create_rectangle(1,275, 150, 300, fill='brown')
    plat4= canvas.create_rectangle(1130,275,1280,300, fill='brown')
    platcentro= canvas.create_rectangle(380,275,840,300,fill='brown')
    plat5= canvas.create_rectangle(1,125, 550, 150, fill='brown')
    plat6= canvas.create_rectangle(730, 125, 1280, 150, fill='brown')

    ####Bloque POW####
    POW= canvas.create_rectangle(590,405,630,440, fill='grey')
    spritepow=PhotoImage(file='powsprite.gif')
    


    ###Sprites de Mario##
    imagenmarioderecha= PhotoImage(file='staleright.gif')
    imagenmarioizquierda= PhotoImage(file='staleleft.gif')
    imagenmariosaltoizquierda= PhotoImage(file='jumpleft.gif')
    imagenmariosaltoderecha=PhotoImage(file='jumpright.gif')
    imagenmarioholdizquierda=PhotoImage(file='mariohammerholdleft.gif')
    imagenmarioholdderecha=PhotoImage(file='mariohammerholdright.gif')
    imagenmariohitizquierda=PhotoImage(file='mariohammerhitleft.gif')
    imagenmariohitderecha=PhotoImage(file='mariohammerhitright.gif')
    mariodieleft=PhotoImage(file='mariodieleft.gif')
    mariodieright=PhotoImage(file='mariodieright.gif')
    mariodeadleft=PhotoImage(file='mariodeadleft.gif')
    mariodeadright=PhotoImage(file='mariodeadright.gif')
    frozenmario=PhotoImage(file='frozenmario.gif')


    ###Texturas del entorno y fondo####
    pipeleft=PhotoImage(file='pipeleft.gif')
    piperight=PhotoImage(file='piperight.gif')
    back=PhotoImage(file='background.gif')

    background=canvas.create_image(0,0,image=back, anchor=NW)
    canvas.tag_lower(background)


    ###Sprites de la Koopa Troopa###
    koopastale=PhotoImage(file='koopastale.gif')
    koopastep=PhotoImage(file='koopastep.gif')
    koopaflipped=PhotoImage(file='koopaflipped.gif')
    koopaflipped2=PhotoImage(file='koopaflipped2.gif')


    ###Sprites de la Paratroopa###
    paratroopastale=PhotoImage(file='paratroopastale.gif')
    paratroopaflap=PhotoImage(file='paratroopaflap.gif')
    paratroopaflipped=PhotoImage(file='paratroopaflipped1.gif')
    paratroopaflipped2=PhotoImage(file='Paratroopaflipped2.gif')


    ###Sprites de la Shadow Koopa###
    shadowstale=PhotoImage(file='Shadowtroopastale.gif')
    shadowstep=PhotoImage(file='Shadowkoopastep.gif')
    shadowflipped=PhotoImage(file='shadowkoopaflipped.gif')
    shadowflipped2=PhotoImage(file='shadowkoopaflipped2.gif')
    shadowhit=PhotoImage(file='shadowkoopahit1.gif')
    shadowhit2=PhotoImage(file='shadowkoopahit2.gif')

    ###Sprites del Shy Guy###
    shystale=PhotoImage(file='shyguystale.gif')
    shystep=PhotoImage(file='shyguystep.gif')
    shyhit1=PhotoImage(file='shyguyhit.gif')
    shyhit2=PhotoImage(file='shyguyhit2.gif')
    shythrow=PhotoImage(file='shyguythrow.gif')

    ###Power Star###
    powersprite=PhotoImage(file='powerstar.gif')

    ###Menú de Pausa###
    pausemenu1=PhotoImage(file='pausemenu1.gif')
    pausemenu2=PhotoImage(file='pausemenu2.gif')



    
    ###Definición de constantes necesarias para el funcionamiento del juego###
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

    pipe2=canvas.create_rectangle(1145,20, 1280, coordsplat6y1, fill=None, width=0)
    pipe2coordsx1= int(canvas.coords(pipe2)[0])
    pipe2coordsx2= int(canvas.coords(pipe2)[2])
    pipe2coordsy1= int(canvas.coords(pipe2)[1])
    pipe2coordsy2= int(canvas.coords(pipe2)[3])
    pipesprite2=canvas.create_image(pipe2coordsx1+65,pipe2coordsy1+53, image=pipeleft)

    pipe3=canvas.create_rectangle(0,445, 136, 560, fill=None, width=0)
    pipe3coordsx1= int(canvas.coords(pipe3)[0])
    pipe3coordsx2= int(canvas.coords(pipe3)[2])
    pipe3coordsy1= int(canvas.coords(pipe3)[1])
    pipe3coordsy2= int(canvas.coords(pipe3)[3])
    pipesprite3=canvas.create_image(pipe3coordsx1+65,pipe3coordsy1+53, image=piperight)

    pipe4=canvas.create_rectangle(1145,445, 1280, 560, fill=None, width=0)
    pipe4coordsx1= int(canvas.coords(pipe4)[0])
    pipe4coordsx2= int(canvas.coords(pipe4)[2])
    pipe4coordsy1= int(canvas.coords(pipe4)[1])
    pipe4coordsy2= int(canvas.coords(pipe4)[3])
    pipesprite4=canvas.create_image(pipe4coordsx1+65,pipe4coordsy1+53, image=pipeleft)

    coordspowx1=int(canvas.coords(POW)[0])
    coordspowy1=int(canvas.coords(POW)[1])+1
    coordspowx2=int(canvas.coords(POW)[2])-2
    coordspowy2=int(canvas.coords(POW)[3])



    
    if rempow>0:
        
        powsprite=canvas.create_image(coordspowx1+20,coordspowy1+10, image=spritepow)

    if estadomario=='derecha':
        
        spritemario=canvas.create_image(coordsmariox1glob+25,coordsmarioy2glob-27, image=imagenmarioderecha)
    elif estadomario=='izquierda':
        spritemario=canvas.create_image(coordsmariox1glob+25,coordsmarioy2glob-27, image=imagenmarioizquierda)
    if estadokoopa1!=None:
        koopa1=canvas.create_rectangle(data[3][0],data[3][1],data[3][2],data[3][3], width=0)
        if estadokoopa1=='creado':
            koopaanim=1
            spritekoopa=canvas.create_image(data[3][0]+24,data[3][1]+25, image=koopastale)
            x.after(2, koopa1_behaviour)
        elif estadokoopa1=='volteado':
            spritekoopa=canvas.create_image(data[3][0]+24,data[3][1]+25, image=koopaflipped)
            x.after(2, changeflipkoopa)
            x.after(7000, unflipkoopa)
    if estadoparatroopa!=None:
        paratroopa=canvas.create_rectangle(data[5][0], data[5][1],data[5][2],data[5][3], width=0)
        if estadoparatroopa=='creado':
            paratroopaanim=1
            spriteparatroopa=canvas.create_image(data[5][0]+24,data[5][1],+25, image=paratroopastale)
            x.after(2, paratroopabehaviour)
        elif estadoparatroopa=='volteado':
            spriteparatroopa=canvas.create_image(data[5][0]+26, data[5][0]+20, image=paratroopaflipped)
            x.after(2, changeflipparatroopa)
            x.after(7000, unflipparatroopa)
    if estadoshadow!=None:
        shadow=canvas.create_rectangle(data[7][0],data[7][1],data[7][2],data[7][3], width=0)
        if estadoshadow=='creado':
            shadowanim=1
            spriteshadow=canvas.create_image(data[7][0]+24,data[7][1]+25, image=shadowstale)
            x.after(2, shadow_behaviour)
        elif estadoshadow=='volteado':
            spriteshadow=canvas.create_image(data[7][0]+24,data[7][1]+25, image=shadowflipped)
            x.after(2, changeflipshadow)
            x.after(7000, unflipshadow)
    if estadoshy!=None:
        shyanim=1
        shy=canvas.create_rectangle(data[10][0],data[10][1],data[10][2],data[10][3],width=0)
        spriteshy=canvas.create_image(data[10][0]+24, data[10][1]+25, image=shystale)
        x.after(2, shybehaviour)

    if data[1][3]<coordsplat5y1:
        canvas.move(mario, 0, (coordsplat5y1-data[1][3]))
        canvas.move(spritemario, 0, (coordsplat5y1-data[1][3]))
    elif data[1][3]<coordsplat3y1 and data[1][3]>coordsplat5y1:
        fallmplat5()
    elif data[1][3]<coordsplat1y1 and data[1][3]>coordsplat3y1:
        fallmplat3()
    elif data[1][3]<540 and data[1][3]>coordsplat1y1:
        fallmplat1()
    
###    if data[5][3]<coordsplat5y1:
##        canvas.move(paratroopa, 0, (coordsplat5y1-data[1][3]))
##        canvas.move(spriteparatroopa, 0, (coordsplat5y1-data[1][3]))
##



    x.mainloop()

#######Menu Inicial######


ventanprueb=Tk()
ventanprueb.title('game')
menu=Canvas(ventanprueb, width=1280, height=720)
menuini=PhotoImage(file='menusp.gif')
menuopt=PhotoImage(file='menuopt.gif')
dif1=PhotoImage(file='dif1.gif')
dif2=PhotoImage(file='dif2.gif')
dif3=PhotoImage(file='dif3.gif')
dif4=PhotoImage(file='dif4.gif')
dif5=PhotoImage(file='dif5.gif')
load1=PhotoImage(file='load1.gif')
load2=PhotoImage(file='load2.gif')
nametype=PhotoImage(file='nametype.gif')
state=0
menu.pack()
menu.focus_set()
men=menu.create_image(0,0,image=menuini, anchor=NW)
menu.bind('<s>', menuinic)
menu.bind('<w>', menuinic)
menu.bind('<Return>', menuinic)
menu.bind('<a>', ignore)
menu.bind('<d>', ignore)
musica1=threading.Thread(target=Initialmusic)
musica1.start()
difficulty=1
nombre1=StringVar()
ventanprueb.mainloop()


