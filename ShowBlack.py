import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

#函数作用是显示黑色的标注图片。黑色标注图片是8位图片，存储的是像素点标注索引。
#可通过函数将其转化为16位灰度图进行可视化。
def img_showblack(filepath,savepath):
    for parent,dirnames,filenames in os.walk(filepath):
        for filename in filenames:
            img_path = os.path.join(parent, filename)
            #filePath = unicode(img_path, 'utf8')
            print(img_path)
            uint16_img = cv2.imread(img_path, -1)
            uint16_img -= uint16_img.min()
            uint16_img = uint16_img / (uint16_img.max() - uint16_img.min())
            uint16_img *= 255
            new_uint16_img = uint16_img.astype(np.uint8)
            path = savepath
            cv2.imwrite(os.path.join(path,f"{filename}"),new_uint16_img)

if __name__ == '__main__':
    filepath = r"/Users/wangyuhan/Desktop/train/label"
    savepath = r'/Users/wangyuhan/Desktop/after'
    img_showblack(filepath,savepath)
    
#删除./DS Store文件的方法
#sudo   find ./ -name ".DS_Store" -depth -exec rm {} \; 
