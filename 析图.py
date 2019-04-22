import tkinter.filedialog
import cv2
import math
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
    label_Img1.place(x=0,y=0,width=485,height=300)
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

def disdance():
    img = cv2.imread(a)
    sp = img.shape
    ht = sp[0]
    wh = sp[1]
    cropImg_l1 = img[int((ht/8)):int((3*ht/8)),int((wh/16)):int((3*wh/16))]
    cropImg_l2 = img[int((ht / 8)):int((3 * ht / 8)), int((5*wh / 16)):int((7 * wh / 16))]
    cropImg_l3 = img[int((5*ht / 8)):int((7 * ht / 8)), int((wh / 16)):int((3 * wh / 16))]
    cropImg_l4 = img[int((5 * ht / 8)):int((7 * ht / 8)), int((5*wh / 16)):int((7 * wh / 16))]
    cropImg_r1 = img[int((ht/8)):int((3*ht/8)),int((9*wh/16)):int((11*wh/16))]
    cropImg_r2 = img[int((ht / 8)):int((3 * ht / 8)), int((13 * wh / 16)):int((15 * wh / 16))]
    cropImg_r3 = img[int((5 * ht / 8)):int((7 * ht / 8)), int((9*wh / 16)):int((11 * wh / 16))]
    cropImg_r4 = img[int((5 * ht / 8)):int((7 * ht / 8)), int((13 * wh / 16)):int((15 * wh / 16))]
    l1_Bmean = np.mean(cropImg_l1[:, :, 0])
    l1_Gmean = np.mean(cropImg_l1[:, :, 1])
    l1_Rmean = np.mean(cropImg_l1[:, :, 2])
    l2_Bmean = np.mean(cropImg_l2[:, :, 0])
    l2_Gmean = np.mean(cropImg_l2[:, :, 1])
    l2_Rmean = np.mean(cropImg_l2[:, :, 2])
    l3_Bmean = np.mean(cropImg_l3[:, :, 0])
    l3_Gmean = np.mean(cropImg_l3[:, :, 1])
    l3_Rmean = np.mean(cropImg_l3[:, :, 2])
    l4_Bmean = np.mean(cropImg_l4[:, :, 0])
    l4_Gmean = np.mean(cropImg_l4[:, :, 1])
    l4_Rmean = np.mean(cropImg_l4[:, :, 2])

    l_Bmean = (l1_Bmean + l2_Bmean + l3_Bmean + l4_Bmean)/4
    l_Gmean = (l1_Gmean + l2_Gmean + l3_Gmean + l4_Gmean)/4
    l_Rmean = (l1_Rmean + l2_Rmean + l3_Rmean + l4_Rmean)/4

    r1_Bmean = np.mean(cropImg_r1[:, :, 0])
    r1_Gmean = np.mean(cropImg_r1[:, :, 1])
    r1_Rmean = np.mean(cropImg_r1[:, :, 2])
    r2_Bmean = np.mean(cropImg_r2[:, :, 0])
    r2_Gmean = np.mean(cropImg_r2[:, :, 1])
    r2_Rmean = np.mean(cropImg_r2[:, :, 2])
    r3_Bmean = np.mean(cropImg_r3[:, :, 0])
    r3_Gmean = np.mean(cropImg_r3[:, :, 1])
    r3_Rmean = np.mean(cropImg_r3[:, :, 2])
    r4_Bmean = np.mean(cropImg_r4[:, :, 0])
    r4_Gmean = np.mean(cropImg_r4[:, :, 1])
    r4_Rmean = np.mean(cropImg_r4[:, :, 2])

    r_Bmean = (r1_Bmean + r2_Bmean + r3_Bmean + r4_Bmean) / 4
    r_Gmean = (r1_Gmean + r2_Gmean + r3_Gmean + r4_Gmean) / 4
    r_Rmean = (r1_Rmean + r2_Rmean + r3_Rmean + r4_Rmean) / 4

    rgb_l = (l_Rmean,l_Gmean,l_Bmean)
    rgb_r = (r_Rmean,r_Gmean,r_Bmean)
    R_1, G_1, B_1 = rgb_l
    R_2, G_2, B_2 = rgb_r
    rmean = (R_1 + R_2) / 2
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    print(math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2)))
    c = float(math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2)))

    label_1 = tk.Label(root, text=c)
    label_1.place(x=540, y=425, width=150, height=30)


btn=Button(root,text="高斯模糊",command=gauss)
btn.place(x=540,y=350,width=120, height=25)
btn2=Button(root,text="RGB直方图,灰度图",command=huidu)
btn2.place(x=540,y=325,width=120, height=25)
btn3=Button(root,text="选择图片",command=xuanze)
btn3.place(x=540,y=300,width=120, height=25)
l1=tk.Label(root,text='模糊值:')
l1.place(x=540,y=375)
btn4=Button(root,text="色差计算",command=disdance)
btn4.place(x=540,y=400,width=120, height=25)
e_user =Entry(root)
e_user.place(x=600,y=375,width=120, height=25)
L1=tk.Label(root,text='原图')
L1.place(x=230,y=304)
L2=tk.Label(root,text='高斯模糊')
L2.place(x=1020,y=304)
L3=tk.Label(root,text='灰度图')
L3.place(x=230,y=420)
L4=tk.Label(root,text='RGB直方图')
L4.place(x=1020,y=420)

root.mainloop()