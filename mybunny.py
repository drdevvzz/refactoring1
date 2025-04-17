import pygame as pg
import math as m

pg.init(); S=pg.display.set_mode((800,800)); pg.display.set_caption("Зайчик")

C1,C2,C3,C4,C5,C6=(210,180,140),(240,220,180),(190,160,120),(255,245,225),(255,240,230),(0,0,0); C7=(230,230,235)

def e(s,p,l,a):
    E=pg.Surface((20,l),pg.SRCALPHA); pg.draw.ellipse(E,C1,(0,0,20,l)); pg.draw.ellipse(E,C5,(5,5,10,l-10))
    s.blit(pg.transform.rotate(E,a),pg.transform.rotate(E,a).get_rect(center=p))

def h(s,x,y):
    pg.draw.ellipse(s,C1,(x,y,250,180)); pg.draw.ellipse(s,C1,(x+50,y-50,120,100)); pg.draw.ellipse(s,C2,(x+70,y-30,70,50))

def ey(s,x,y):
    pg.draw.circle(s,C6,(x+90,y+10),5); pg.draw.circle(s,C6,(x+130,y+10),5)

def n(s,x,y):
    pg.draw.circle(s,C6,(x+110,y+30),4)

def w(s,x,y):
    for i in range(-10,11,10):
        pg.draw.line(s,C6,(x+110,y+30),(x+80,y+20+i),1); pg.draw.line(s,C6,(x+110,y+30),(x+140,y+20+i),1)

def p(s,x,y):
    pg.draw.circle(s,C3,(x+30,y+150),30); pg.draw.circle(s,C3,(x+170,y+150),30); pg.draw.circle(s,C3,(x-10,y+80),35); pg.draw.circle(s,C3,(x+210,y+80),35)

def t(s,x,y):
    pg.draw.circle(s,C4,(x-20,y+70),25)

def d(s,x,y):
    h(s,x,y); ey(s,x,y); n(s,x,y); w(s,x,y); e(s,(x+80,y-70),140,-10); e(s,(x+140,y-70),140,10); p(s,x,y); t(s,x,y)

r=True; cl=pg.time.Clock()

while r:
    for ev in pg.event.get():
        if ev.type==pg.QUIT: r=False
    S.fill(C7); d(S,300,300); pg.display.flip(); cl.tick(30)

pg.quit()
