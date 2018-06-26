from easycurses import *
from time import sleep
def life(): #conway's game of life. 
    try:
        dc = DrawController()
        dc.init_screen()
        dc.full_draw()
        h,w = dc.size

        CC = ColorController
        ic = InputController(dc.get_screen())

        def finish_editing(c):
            finish_editing.done=True
        finish_editing.done=False
        ic.register_keyset([' '], finish_editing)
        active = []

        def clicked(pos, state):
            if pos in active:
                active.remove(pos)
            else:
                active.append(pos)
        ic.register_mouse(clicked)
        
        while not finish_editing.done:
            ic.getkeys()
            for a in active:
                c = Char(a, ' ', color=CC.get_color("white","white"))
                dc.draw([c])
            dc.render()

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

            sleep(.05)

    finally:
        dc.end() #do this to restore terminal to normal.
life()
