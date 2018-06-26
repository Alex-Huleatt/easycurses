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

        def finish_editing_callback(c): #variable in scope to inside and outside this function
            finish_editing_callback.done=True
        finish_editing_callback.done=False

        ic.register_keyset(['\n'], finish_editing_callback) #space to finish editing
        active = set() #list of active cells

        def mouse_callback(pos, state): #upon a mouse click
            if pos in active:
                active.remove(pos)
            else:
                active.add(pos)

        ic.register_mouse(mouse_callback)
        
        while not finish_editing_callback.done: #finish_editing.done will be true after space is pressed
            ic.getkeys()
            for a in active:
                c = Char(a, ' ', color=CC.get_color("white","white"))
                dc.draw([c])
            dc.render()

        enough = set() #used to speed up generation
        new_active = set() #temporary buffer
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
