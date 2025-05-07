import tkinter as tk
import random

root = tk.Tk()
root.title = ("Random Button")
root.geometry("300x300")
canvas = tk.Canvas(root, width=300, height=300, bg="#FFFFFF", highlightthickness=2)
canvas.pack()

xp = 50
yp = 250
tp = 150
xs = 60
ys = 260
xpa = xp+10
ypa = yp+10
tpa = tp+10

def random_color():
    n1 = ['0','1','2','3','4','5','6','7','8','9','F','E','D','C','B','A']
    n2 = ['0','1','2','3','4','5','6','7','8','9','F','E','D','C','B','A']
    n3 = ['0','1','2','3','4','5','6','7','8','9','F','E','D','C','B','A']
    n4 = ['0','1','2','3','4','5','6','7','8','9','F','E','D','C','B','A']
    n5 = ['0','1','2','3','4','5','6','7','8','9','F','E','D','C','B','A']
    n6 = ['0','1','2','3','4','5','6','7','8','9','F','E','D','C','B','A']
    ln1 = random.choice(n1)
    ln2 = random.choice(n2)
    ln3 = random.choice(n3)
    ln4 = random.choice(n4)
    ln5 = random.choice(n5)
    ln6 = random.choice(n6)
    color = '#'+ln1+ln2+ln3+ln4+ln5+ln6
    return color

def start_circle():
    global z
    global circle
    global text
    circle = canvas.create_oval(xp, xp, yp, yp, fill=clr, outline="#000000", width=4)
    circle_shadow = canvas.create_oval(xs,xs,ys,ys,fill="#000000")
    canvas.tag_lower(circle_shadow, None)
    text = canvas.create_text(tp,tp, text="Random Button", fill=nclr,font=("Arial", 14, "bold")) 
    z=1

def shape_square(event):
    global z
    global square
    global text
    canvas.delete("all")
    square = canvas.create_rectangle(xp, xp, yp, yp, fill=clr, outline="#000000", width=4)
    square_shadow = canvas.create_rectangle(xs,xs,ys,ys,fill="#000000")
    canvas.tag_lower(square_shadow, None)
    text = canvas.create_text(tp,tp, text="Random Button", fill=nclr,font=("Arial", 14, "bold"))
    z=0

def shape_circle(event):
    global z
    global circle
    global text
    canvas.delete("all")
    circle = canvas.create_oval(xp, xp, yp, yp, fill=clr, outline="#000000", width=4)
    circle_shadow = canvas.create_oval(xs,xs,ys,ys,fill="#000000")
    canvas.tag_lower(circle_shadow, None)
    text = canvas.create_text(tp,tp, text="Random Button", fill=nclr,font=("Arial", 14, "bold")) 
    z=1

def on_click(event):
    global z
    x, y = event.x, event.y
    clr = random_color()
    nclr = random_color()
    if not clr == nclr and xp <= x <= yp and xp <= y <= yp and z==1: 
            canvas.itemconfig(circle, fill=clr,)
            canvas.itemconfig(text, fill=nclr)
            canvas.coords(circle,xpa,xpa,ypa,ypa)
            canvas.coords(text,tpa,tpa)
            root.after(9999999999999, lambda: canvas.coords(circle,xp,xp,yp,yp))
            root.after(9999999999999, lambda: canvas.coords(text,tp,tp))
    if not clr == nclr and xp <= x <= yp and xp <= y <= yp and z==0: 
            canvas.itemconfig(square, fill=clr,)
            canvas.itemconfig(text, fill=nclr)
            canvas.coords(square,xpa,xpa,ypa,ypa)
            canvas.coords(text,tpa,tpa)
            root.after(9999999999999, lambda: canvas.coords(square,xp,xp,yp,yp))
            root.after(9999999999999, lambda: canvas.coords(text,tp,tp))
def on_release(event):
        global z
        if z==1:
            canvas.coords(circle,xp,xp,yp,yp)
        if z==0:
            canvas.coords(square,xp,xp,yp,yp)
        canvas.coords(text,tp,tp)
clr = random_color()
nclr = random_color()

start_circle()
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)
canvas.bind("<ButtonPress-3>", shape_square)
canvas.bind("<ButtonPress-2>",shape_circle)

root.mainloop()