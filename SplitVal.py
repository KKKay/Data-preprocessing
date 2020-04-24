import os
import glob
from PIL import Image
import shutil
import random
import numpy as np
import pandas as pd


# https://blog.csdn.net/u010167269/article/details/51084312

def moveFile(fileDir,tarDir,fileAnnDir,tarAnnDir):
	pathDir = os.listdir(fileDir)
	filenumber = len(pathDir)
	
    #用于验证集的比例
    rate = 0.05
	picknumber = int(filenumber*rate)
	sample = random.sample(pathDir,picknumber)
	print(sample)
	for name in sample:
		shutil.move(fileDir+name,tarDir+name)
		shutil.move(fileAnnDir+name,tarAnnDir+name)
	return



if __name__ == '__main__':
	fileDir = r'/home/wyh/Data/remote/images/train/'
	tarDir = r'/home/wyh/Data/remote/images/val/'
	fileAnnDir = r'/home/wyh/Data/remote/annotations/label_train/'
	tarAnnDir = r'/home/wyh/Data/remote/annotations/label_test/'
	moveFile(fileDir,tarDir,fileAnnDir,tarAnnDir)
