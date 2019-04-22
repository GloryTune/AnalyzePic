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
    label_1.place(x=10, y=200, width=820, height=30)


btn3=Button(root,text="选择图片(纯英文路径)",command=xuanze1)
btn3.place(x=0,y=0,width=120, height=25)
btn2=Button(root,text="色差计算",command=disdance)
btn2.place(x=0,y=25,width=120, height=25)
root.mainloop()