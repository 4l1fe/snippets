import threading, time, sys
from tkinter import Tk, Canvas, Button, LEFT, RIGHT, NORMAL, DISABLED


global champion

distance = 300
colors = ["Red","Orange","Yellow","Green","Blue","DarkBlue","Violet"]
nrunners = len(colors)
positions = [0] * nrunners
h, h2 = 20, 10

def run(n):
    global champion
    while True:
        for i in range(10000): pass
        graph_lock.acquire()
        positions[n] += 1
        if positions[n] == distance:
            if champion is None:
                champion = colors[n]
            graph_lock.release()
            break
        graph_lock.release()

def ready_steady_go():
    graph_lock.acquire()
    for i in range(nrunners):
        positions[i] = 0
        threading.Thread(target=run, args=(i, )).start()
    graph_lock.release()

def update_positions():
    graph_lock.acquire()
    for n in range(nrunners):
        c.coords(rects[n], 0, n*h, positions[n], n*h+h2)
    tk.update_idletasks()
    graph_lock.release()

def quit():
    tk.quit()
    sys.exit(0)

tk = Tk()
tk.title('Соревнование потоков')
c = Canvas(tk, width=distance, height=nrunners*h, bg="White")
c.pack()
rects = [c.create_rectangle(0, i*h, 0, i*h+h2, fill=colors[i]) for i in range(nrunners)]
go_b = Button(text="Go", command=tk.quit)
go_b.pack(side=LEFT)
quit_b = Button(text="Quit", command=quit)
quit_b.pack(side=RIGHT)

graph_lock = threading.Lock()

while True:
    go_b.config(state=NORMAL), quit_b.config(state=NORMAL)
    tk.mainloop()
    champion = None
    ready_steady_go()
    go_b.config(state=DISABLED), quit_b.config(state=DISABLED)
    while sum(positions) < distance*nrunners:
        update_positions()
    update_positions()
    go_b.config(bg=champion)
    tk.update_idletasks()

