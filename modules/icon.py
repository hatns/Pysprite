import pygame as p
z = p.Surface
c = p.SRCALPHA
m = "#000000"
n = "#FFFFFF"
def get_surface():
    a = z((16, 16), p.SRCALPHA, 32)
    def d(clr,pos,b=255):
        s = z((1,1), c)
        s.fill(clr)
        s.set_alpha(b)
        a.blit(s, pos)
    d(m,(1,1));d(m,(2,1));d(m,(3,1));d(m,(4,1));d(m,(5,1));d(m,(1,2));d(m,(5,2));d(m,(6,2));d(m,(1,3));d(m,(6,3));d(m,(8,3));d(m,(9,3));d(m,(11,3));d(m,(1,4));d(m,(6,4));d(m,(8,4));d(m,(11,4));d(m,(1,5));d(m,(5,5));d(m,(6,5));d(m,(8,5));d(m,(9,5));d(m,(11,5));d(m,(1,6));d(m,(2,6));d(m,(3,6));d(m,(4,6));d(m,(5,6));d(m,(8,6));d(m,(11,6));d(m,(1,7));d(m,(8,7));d(m,(9,7));d(m,(10,7));d(m,(11,7));d(m,(12,7));d(m,(13,7));d(m,(14,7));d(m,(1,8));d(m,(1,9));d(m,(5,9));d(m,(8,9));d(m,(10,9));d(m,(14,9));d(m,(1,10));d(m,(5,10));d(m,(6,10));d(m,(7,10));d(m,(8,10));d(m,(10,10));d(m,(11,10));d(m,(13,10));d(m,(14,10));d(m,(1,11));d(m,(8,11));d(m,(11,11));d(m,(12,11));d(m,(13,11));d(m,(1,12));d(m,(5,12));d(m,(8,12));d(m,(10,12));d(m,(11,12));d(m,(13,12));d(m,(14,12));d(m,(0,13));d(m,(1,13));d(m,(2,13));d(m,(5,13));d(m,(6,13));d(m,(7,13));d(m,(8,13));d(m,(10,13));d(m,(14,13));d(m,(1,14));
    return a
if __name__ == "__main__":

    surface = get_surface()
    window = p.display.set_mode((500, 500))
    window.fill((255,255,255))
    window.blit(surface, (250-int(surface.get_width()/2), 250-int(surface.get_width()/2)))
    while True:
        p.display.update()
