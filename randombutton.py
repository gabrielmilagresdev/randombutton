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

nf='#'
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
color = nf+ln1+ln2+ln3+ln4+ln5+ln6
clr = color
ln1 = random.choice(n1)
ln2 = random.choice(n2)
ln3 = random.choice(n3)
ln4 = random.choice(n4)
ln5 = random.choice(n5)
ln6 = random.choice(n6)
color = nf+ln1+ln2+ln3+ln4+ln5+ln6
nclr = color

circle = canvas.create_oval(xp, xp, yp, yp, fill=clr, outline="#000000", width=4)
circle_shadow = canvas.create_oval(xs,xs,ys,ys,fill="#000000")
canvas.tag_lower(circle_shadow, None) 
text = canvas.create_text(300, 50, text="Click", fill=nclr, font=('Helvetica 15 bold'))


def on_click(event):
    xp = 50
    yp = 250
    tp = 150
    xs = 60
    ys = 260
    xpa = xp+10
    ypa = yp+10
    tpa = tp+10
    x, y = event.x, event.y
    ln1 = random.choice(n1)
    ln2 = random.choice(n2)
    ln3 = random.choice(n3)
    ln4 = random.choice(n4)
    ln5 = random.choice(n5)
    ln6 = random.choice(n6)
    color = nf+ln1+ln2+ln3+ln4+ln5+ln6
    clr = color
    ln1 = random.choice(n1)
    ln2 = random.choice(n2)
    ln3 = random.choice(n3)
    ln4 = random.choice(n4)
    ln5 = random.choice(n5)
    ln6 = random.choice(n6)
    color = nf+ln1+ln2+ln3+ln4+ln5+ln6
    nclr = color
    if not clr == nclr and xp <= x <= yp and xp <= y <= yp: 
        canvas.itemconfig(circle, fill=clr,)
        canvas.itemconfig(text, fill=nclr )
        canvas.coords(circle,xpa,xpa,ypa,ypa)
        root.after(100, lambda: canvas.coords(circle,xp,xp,yp,yp))
        root.after(200, lambda: canvas.coords(circle, xp,xp,yp,yp ))
        root.after(0, lambda: canvas.coords(circle_shadow,xs,xs,ys,ys))
canvas.bind("<Button-1>", on_click)

root.mainloop()