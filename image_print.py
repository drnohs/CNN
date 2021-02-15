import numpy as np
from PIL import Image

class ImagePrint:
    def __init__(self,px,py,cx,cy,space=1,bgcolor=255):
        self.px = px # Picture width, height
        self.py = py
        self.cx = cx # Picture Count Horizontal, Vertical
        self.cy = cy
        self.space = space
        self.bgcolor=bgcolor

        self.w = (px + space) * cx - space
        self.h = (py + space) * cy - space

        self.out=np.zeros((self.h, self.w))+bgcolor

    def print_size(self):
        print("W x H : ",self.w,"x",self.h)

    def input_image(self, idx, img, ratio):
        idx_x = idx % self.cx
        idx_y = idx // self.cx
        self.input_image_xy(idx_x, idx_y, img, ratio)

    def input_image_xy(self, idx_x, idx_y, img, ratio):
        x = idx_x * (self.px + self.space)
        y = idx_y * (self.py + self.space)

        img = img.reshape(-1,1) * ratio
        max_img = np.zeros_like(img)+255
        t_img = np.concatenate((img,max_img),axis=1)
        img=t_img.min(axis=1)

        self.out[y:y+self.py,x:x+self.px]=img.reshape(self.px,self.py)

    def img_show(self):
        pil_img = Image.fromarray(np.uint8(self.out))
        pil_img.show()
