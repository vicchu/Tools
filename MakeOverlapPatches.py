# -*- coding: utf-8 -*-
"""
    生成数据集
"""
import os
import tqdm
import time
import datetime
import numpy as np
from skimage import io

def make_imagepatch(image,targetsize,path):

    target_size = targetsize
    quarter_target_size = target_size // 4
    half_target_size = target_size // 2
    patchs = []
    for row_begin in range(0, image.shape[0], half_target_size):
        for col_begin in range(0, image.shape[1], half_target_size):
            row_end = row_begin + target_size
            col_end = col_begin + target_size
            if row_end > image.shape[0]:
                row_end = image.shape[0]
                row_begin = row_end - target_size
            if col_end > image.shape[1]:
                col_end = image.shape[1]
                col_begin = col_end - target_size
            patchs.append((row_begin, row_end, col_begin, col_end))
    for b in patchs:
        imagepatch = image[b[0]:b[1],b[2]:b[3]]
        imagepath =path+'/'+ str(b[0])+'_'+ str(b[1])+'_'+ str(b[2])+'_'+ str(b[3])+'.png'
        io.imsave(imagepath,imagepatch)

if __name__ == '__main__':
    image_path='/data/image.tif'

    print('Processing!')

    image = io.imread(image_path)

    DataPath = '/data/'
    datasetpath = os.path.join(DataPath,'dataset')

    targetsize = 512

    t0 = time.time()
    make_imagepatch(image, targetsize, datasetpath)
    print('time cost: %0.2f(min).' % ((time.time() - t0) / 60))




