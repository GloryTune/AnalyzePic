import tkinter.filedialog
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk,ImageFilter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root=Tk()

root.title('析图')
root.geometry("1280x791+200+20")

global img_jpg,Img, label_Img,img_g,a

def xuanze():
    global a,Img, label_Img,img_jpg,label_Img1
    a = tkinter.filedialog.askopenfilename()
    #global img_jpg
    Img = Image.open(a)
    x_s = 485
    y_s = 300
    out = Img.resize((x_s, y_s), Image.ANTIALIAS)
    img_jpg = ImageTk.PhotoImage(out)
    label_Img1=tk.Label(root,image=img_jpg)
    label_Img1.place(x=800,y=0,width=485,height=300)
#灰度
def huidu():
    global a, Img, label_Img, img_jpg1
    Img_l = Img.convert('LA')
    x_s = 485
    y_s = 300
    out = Img_l.resize((x_s, y_s), Image.ANTIALIAS)
    img_jpg1 = ImageTk.PhotoImage(out)
    label_Img = tk.Label(root, image=img_jpg1)
    label_Img.place(x=0,y=470,width=485, height=300)
    #label_Img1.place(x=900, y=0, width=485, height=300)
#颜色直方图

    src = PIL.Image.open(a)
    r, g, b = src.split()
    figure1=plt.figure(figsize=(5,4))
    ar = np.array(r).flatten()
    plt.hist(ar, bins=256, density=True, facecolor='r', edgecolor='r')
    ag = np.array(g).flatten()
    plt.hist(ag, bins=256, density=True, facecolor='g', edgecolor='g')
    ab = np.array(b).flatten()
    plt.hist(ab, bins=256, density=True, facecolor='b', edgecolor='b')

    canvas = FigureCanvasTkAgg(figure1,master=root)
    canvas.get_tk_widget().place(x=800,y=450,width=485, height=300)
    canvas.draw()


#高斯模糊
def gauss():
    global img_g,img1_jpg,Img
    gao = e_user.get()
    Img_g = Img.filter(ImageFilter.GaussianBlur(radius=int(gao)))
    x_s = 485
    y_s = 300
    out = Img_g.resize((x_s, y_s), Image.ANTIALIAS)
    img1_jpg = ImageTk.PhotoImage(out)
    label1_Img = tk.Label(root, image=img1_jpg)
    label1_Img.place(x=800,y=0,width=485, height=300)



btn=Button(root,text="高斯模糊",command=gauss)
btn.place(x=10,y=50,width=120, height=25)
btn2=Button(root,text="RGB直方图,灰度图",command=huidu)
btn2.place(x=10,y=25,width=120, height=25)
btn3=Button(root,text="选择图片",command=xuanze)
btn3.place(x=10,y=0,width=120, height=25)
l1=tk.Label(root,text='模糊值:')
l1.place(x=10,y=75,width=40, height=25)
e_user =Entry(root)
e_user.place(x=60,y=75,width=120, height=25)

root.mainloop()