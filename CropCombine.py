import cv2 as cv
import numpy as np
import os
import math

def crop_one(path,filename,cols,rows):
    img = cv.imread(path+filename,-1)
    sum_rows = img.shape[0]
    sum_cols = img.shape[1]
    save_path = path+"crop_{}_{}*{}/".format(os.path.splitext(filename)[0],cols,rows)

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    print("crop to {} cols, {} rows".format(int(sum_cols/cols)+1,int(sum_rows/rows)+1))

    new_sum_cols = (int(sum_cols/cols)+1)*cols
    new_sum_rows = (int(sum_rows/rows)+1)*rows

    print(sum_rows,new_sum_rows)
    print(sum_cols,new_sum_cols)

    imgdone = cv.copyMakeBorder(img,0,new_sum_rows-sum_rows,0,new_sum_cols-sum_cols ,cv.BORDER_CONSTANT,value =0)


    for i in range(int(sum_cols/cols)+1):
        for j in range(int(sum_rows/rows)+1):
            temp = imgdone[j*rows:(j+1)*rows,i*cols:(i+1)*cols,:]

            cv.imwrite(save_path+os.path.splitext(filename)[0]+'_'+str(j)+'_'+str(i)+os.path.splitext(filename)[1],temp)
    
    paths = os.listdir(save_path)
    for name in paths:
        img = cv.imread(os.path.join(save_path,name))
        print(name)
        print(img.shape)


def combine_all(combine_path,dst_path,cols,rows,channels,num_of_cols,num_of_rows):
    pathDir = os.listdir(combine_path)
    dst = np.zeros((rows*num_of_rows,cols*num_of_cols,channels),np.uint8)
    print(dst.shape)

    for filename in pathDir:
        img = cv.imread(combine_path+filename)
        filename = os.path.splitext(filename)[0]
        cols_th = int(filename.split("_")[-1])
        rows_th = int(filename.split("_")[-2])
        roi = img[0:rows,0:cols,:]

        print("ths:{},{}".format(cols_th,rows_th))
        print("roi.shape:{}".format(roi.shape))
        print(dst[rows_th*rows:(rows_th+1)*rows,cols_th*cols:(cols_th+1)*cols,:].shape)
        dst[rows_th*rows:(rows_th+1)*rows,cols_th*cols:(cols_th+1)*cols,:]=roi

    cv.imwrite(dst_path+"merge.jpg",dst)



def crop_with_overlapped(path,filename,cols_val,rows_val,overlap):
    img = cv.imread(path+filename,-1)
    print(img.shape)

    sum_rows = img.shape[0]
    sum_cols = img.shape[1]

    save_path = path+"test{}/".format(os.path.splitext(filename)[0])+"crop_{}_{}*{}_{}/".format(os.path.splitext(filename)[0],cols_val,rows_val,overlap)

    rows = (sum_rows-overlap)/(rows_val-overlap)
    cols = (sum_cols-overlap)/(cols_val-overlap)

    rows = math.ceil(rows)
    cols = math.ceil(cols)

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    print("crop to {} rows, {} cols".format(rows,cols))

    new_sum_cols = cols*cols_val-overlap*(cols-1)
    new_sum_rows = rows*rows_val-overlap*(rows-1)

    print(sum_rows,new_sum_rows)
    print(sum_cols,new_sum_cols)

    imgdone = cv.copyMakeBorder(img,0,new_sum_rows-sum_rows,0,new_sum_cols-sum_cols,cv.BORDER_CONSTANT,value =0)
    print(imgdone.shape)

    for i in range(rows):
        for j in range(cols):
            temp = imgdone[i*rows_val-i*overlap:i*rows_val-i*overlap+rows_val,j*cols_val-j*overlap:j*cols_val-j*overlap+cols_val,:]
            cv.imwrite(save_path+os.path.splitext(filename)[0]+'_'+str(i)+'_'+str(j)+os.path.splitext(filename)[1],temp)

    paths = os.listdir(save_path)
    for name in paths:
        img = cv.imread(os.path.join(save_path,name))
        print(name)
        print(img.shape)
    
    return rows,cols


def combine_with_overlap(combine_path,dst_path,cols_val,rows_val,channels,cols,rows,overlap):
    pathDir = os.listdir(combine_path)

    new_sum_rows = rows*rows_val-overlap*(rows-1)
    new_sum_cols = cols*cols_val-overlap*(cols-1)

    dst = np.zeros((new_sum_rows,new_sum_cols,channels),np.uint8)
    print(dst.shape)

    for filename in pathDir:
        img = cv.imread(combine_path+filename)
        filename = os.path.splitext(filename)[0]
        
        rows_th = int(filename.split("_")[-2])
        cols_th = int(filename.split("_")[-1])

        print(rows_th,cols_th)
        
        roi = img[0:rows_val,0:cols_val,:]

        print("ths: rows-{},cols-{}".format(rows_th,cols_th))
        
        print("roi.shape:{}".format(roi.shape))

        row_pos_start = rows_th*rows_val-rows_th*overlap
        row_pos_end = rows_th*rows_val-rows_th*overlap+rows_val

        col_pos_start = cols_th*cols_val-cols_th*overlap
        col_pos_end = cols_th*cols_val-cols_th*overlap+cols_val
        

        print("dst.shape:{}".format(dst[row_pos_start:row_pos_end,col_pos_start:col_pos_end,:].shape))

        dst[row_pos_start:row_pos_end,col_pos_start:col_pos_end,:] = dst[row_pos_start:row_pos_end,col_pos_start:col_pos_end,:] + roi

    cv.imwrite(dst_path+"merge.jpg",dst)


    

if __name__ == "__main__":
    
    channels = 3
    rows_val = 1024
    cols_val = 1024
    overlap = 400
    
    path = r'/home/wyh/AI-Data/remote/images/test2020/'
    filename = r'1.png'
    combine_path = path+"test{}/".format(os.path.splitext(filename)[0])+"crop_{}_{}*{}_{}/".format(os.path.splitext(filename)[0],cols_val,rows_val,overlap)
    dst_path = r'/home/wyh/Desktop/'

    combine_path = r'/home/wyh/AI-Code/DeepGlobe-Road-Extraction-Challenge-master/submits/log01_dink34/'

    rows = 8
    cols = 9

    combine_with_overlap(combine_path,dst_path,cols_val,rows_val,channels,cols,rows,overlap)


    