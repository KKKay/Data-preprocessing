from skimage import io
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

#添加后可用于完全展示图像的值
# np.set_printoptions(threshold=np.inf)

#创建一个尺寸为m*n的图片
def create_image(m,n):
    img = np.zeros([m,n],np.uint8)
    return img

#从8位标注图片转换到二值标注图片
#假设图片中共有k类标注，对应的序列图值分别是0～k-1
def EightToBinary(file_path,save_path,m,n,dict_k):
    for parent,dirnames,filenames in os.walk(file_path):
        for filename in filenames:
            img_path = os.path.join(parent,filename)
            if filename=='.DS_Store':
                continue
            print(img_path)
            
            #读取数据
            img = cv2.imread(img_path)   
            rows,cols = img.shape
            
            fileName = os.path.splitext(filename)[0]
            index = 0
            
            k = len(dict_k)
            #生成二值图像
            for label in range(k):
                if(label != 0):
                    temp = create_image(m,n)
                    for i in range(rows):
                        for j in range(cols):
                            if(temp[i,j]==k):
                                temp[i,j] = 255            
                    cv2.imwrite(os.path.join(save_path,fileName+f"_{dict_k[k]}_"+f"{index}.png"),temp)
                    index = index+1 #index原用于区分实例，这里没有区分实例，并无意义
                

#从16位灰度标注图片转换到二值标注图片
def GrayToBinary(file_path,save_path,m,n,dict_k,gray_color):
    for parent,dirnames,filenames in os.walk(file_path):
        for filename in filenames:
            img_path = os.path.join(parent,filename)
            if filename=='.DS_Store':
                continue
            print(img_path)

            #读取数据,读取的是灰度图
            img = cv2.imread(img_path)
            #转换通道
            rows,cols = img.shape
            fileName = os.path.splitext(filename)[0]
            index = 0
            
            k = len(dict_k)
            for label in range(k):
                if(label!=0)
                    temp = create_image(m,n)
                    for i in range(rows):
                        for j in range(cols):
                            if(temp[i,j]==gray_color[k]):
                                gray_img1[i,j] = 255
                    cv2.imwrite(os.path.join(save_path,fileName+f"_{dict_k[k]}_"+f"{index}.png"),temp)
                    index = index+1 #index原用于区分实例，这里没有区分实例，并无意义

if __name__=='__main__':
    filepath = r'/home/wyh/AI-Data/remote/images/test2020/5'
    savepath = r'/home/wyh/AI-Data/remote/images/test2020'
    m = 7939
    n = 7969
    #假设图片中共有5类标注，对应的灰度值分别是0，63，127，191，255
    dict_k = {'0':backgroud,'1':grass,'2':building,'3':water,'4':road} #0统一为背景
    gray_color = [0,63,127,191,255] 
    GrayToBinary(filepath,savepath,m,n,dict_k,gray_color)
    

