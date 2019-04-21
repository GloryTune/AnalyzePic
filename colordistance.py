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

def xuanze2():
    global   img_jpg1,b
    b = tkinter.filedialog.askopenfilename()
    Img = Image.open(b)
    x_s = 485
    y_s = 300
    out = Img.resize((x_s, y_s), Image.ANTIALIAS)
    img_jpg1= ImageTk.PhotoImage(out)
    label_Img1 = tk.Label(root, image=img_jpg1)
    label_Img1.place(x=510, y=300, width=485, height=300)



def jisuan():
    global c,a,b
    img1 = cv2.imread(a)
    img2 = cv2.imread(b)

    img1_Bmean = np.mean(img1[:,:,0])
    img1_Gmean = np.mean(img1[:,:,1])
    img1_Rmean = np.mean(img1[:,:,2])
    img2_Bmean = np.mean(img2[:,:,0])
    img2_Gmean = np.mean(img2[:,:,1])
    img2_Rmean = np.mean(img2[:,:,2])

    rgb_11 = (img1_Rmean,img1_Gmean,img1_Bmean)
    rgb_22 = (img2_Rmean,img2_Gmean,img2_Bmean)

    R_1,G_1,B_1 = rgb_11
    R_2,G_2,B_2 = rgb_22
    rmean = (R_1 +R_2 ) / 2
    R = R_1 - R_2
    G = G_1 -G_2
    B = B_1 - B_2
    print(math.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2)))
    c=float(math.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2)))

    label_1 = tk.Label(root, text=c)
    label_1.place(x=10, y=200, width=820, height=30)

btn3=Button(root,text="选择图片1",command=xuanze1)
btn3.place(x=0,y=0,width=120, height=25)
btn2=Button(root,text="选择图片2",command=xuanze2)
btn2.place(x=0,y=25,width=120, height=25)
btn1=Button(root,text="色差",command=jisuan)
btn1.place(x=0,y=50,width=120, height=25)

root.mainloop()