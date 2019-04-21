import cv2
import numpy as np
import math
import tkinter.filedialog
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
root=Tk()
root.title('色差')
root.geometry("990x600+200+20")
global a,b
def xuanze1():
    global  img_jpg,a
    a = tkinter.filedialog.askopenfilename()
    Img = Image.open(a)
    x_s = 485
    y_s = 300
    out = Img.resize((x_s, y_s), Image.ANTIALIAS)
    img_jpg = ImageTk.PhotoImage(out)
    label_Img1 = tk.Label(root, image=img_jpg)
    label_Img1.place(x=0, y=300, width=485, height=300)
def disdance():
    img = cv2.imread(a)
    sp = img.shape
    ht = sp[0]
    wh = sp[1]
    cropImg = img[int((ht/4)):int((ht/2)),int((wh/4)):int((wh/2))]
    cv2.imwrite('d:\\yyy\\' + '.jpg', cropImg)
btn3=Button(root,text="选择图片1",command=xuanze1)
btn3.place(x=0,y=0,width=120, height=25)
btn2=Button(root,text="选择图片2",command=disdance)
btn2.place(x=0,y=25,width=120, height=25)
root.mainloop()