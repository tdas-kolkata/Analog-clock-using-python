
import pygame as p
from datetime import *
from math import *


p.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,150,0)
scn=p.display.set_mode([400,400])


clock=p.time.Clock()


p.display.set_caption('analog clock')
clockexit=False

img=p.image.load('clock.jpeg')
click_sound=p.mixer.Sound('Clock_Ticking.wav')

p.display.set_icon(img)
font=p.font.SysFont('arial',25)
def hand(length,phi,width,colour):
    p.draw.line(scn,colour,[200,200],[200+length*sin(radians(phi)),200-length*cos(radians(phi))],width)
def dateprint(msg):
    date=font.render(msg,True,green)
    scn.blit(date,[160,240])
msg=str(date.today().day)+'.'+str(date.today().month)+'.'+str(date.today().year)
phi_s=(datetime.now().time().second)*6
phi_m=(datetime.now().time().minute)*6+(datetime.now().time().second)*0.1
phi_h=(datetime.now().time().hour)*30+(datetime.now().time().minute)*0.5
while clockexit==False:
    scn.fill(white)
    scn.blit(img,[50,50])
    
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            quit()
    dateprint(msg)
    hand(90,phi_s,2,red)
    hand(110,phi_m,4,black)
    hand(60,phi_h,6,green) 
    phi_s+=6
    phi_m+=6/60
    phi_h+=6/3600
    clock.tick(1)
    p.mixer.Sound.play(click_sound)
    p.display.update()

p.quit()
quit()
