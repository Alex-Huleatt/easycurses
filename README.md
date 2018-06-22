# For making text-based UIs



Sad that making those new-fangled moving pictures can be so complicated?
Do you *really* not care about the quality of your graphics as long it works?

Well suffer no more!


![](./assets/life_example.gif)
(gif with extra jpeg for your pleasure)


# life of py (with fewer tigers)
```
from easycurses import *
from time import sleep
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

        active = map(lambda p:Pair(p[0],p[1]), active)
        while True:
            for a in active:
                c = Char(a, ' ', color=CC.get_color("white","white"))
                dc.draw([c])

            dc.render()

            n_count = defaultdict(int)
            for o in active:
                for n in o.get_neighbors(ortho=False):
                    n_count[n]+=1

            new_active = []
            for k in n_count.keys():
                c = n_count[k]
                if k not in active and c == 3:
                    new_active.append(k)
                elif k in active and c in [2,3]:
                    new_active.append(k)

            active = new_active
            sleep(.05)
    finally:
        dc.end() #do this to restore terminal to normal.
life()
```

Waow! Concise! Whoooooopie. 