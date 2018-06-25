from easycurses import *

def life(): #conway's game of life. 
    try:
        dc = DrawController()
        dc.init_screen()
        dc.full_draw()
        h,w = dc.size
        y,x = h//2,w//2 #center of screen
        CC = ColorController
        
        #Initial state of grid (r-pentomino)
        active = [
        (y,x),
        (y,x+1),
        (y+1,x+1),
        (y+1,x+2),
        (y+2,x+1)
        ]

        active, enough, new_active = set(map(lambda p:Pair(p[0],p[1]), active)), set(), set()
        while True:
            for a in active:
                c = Char(a, ' ', color=CC.get_color("white","white"))
                dc.draw([c])

            dc.render()

            n_count = defaultdict(int)
            enough.clear()
            for o in active:
                for n in o.get_neighbors(ortho=False):
                    if n in n_count and (n in active or n_count[n] > 1):
                        enough.add(n)
                    n_count[n]+=1

            new_active = set()

            for k in enough:
                c = n_count[k]
                if k in active:
                    if c == 2 or c == 3:new_active.add(k)
                elif c == 3:new_active.add(k)
                

            active = new_active

    finally:
        dc.end() #do this to restore terminal to normal.
life()
