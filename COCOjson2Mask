import numpy as np
import json
from skimage import io
import os
import cv2
# from pycocotools.coco import COCO
# import pycocotools.mask as maskUtils
from skimage.draw import polygon
# import matplotlib.pyplot as plt
# OrgImgPath = '/data/images'

def CreatMask(OrgImgPath,JsonPath):
    f = open(JsonPath, encoding='utf-8')
    anns = json.load(f)
    categorylist = anns['categories']
    imagelist = anns['images']
    seglist = anns['annotations']

    # coco = COCO('/data/coco.json')

    cat_id = [0,7, 11, 10, 3, 10015,5,10012,1,2,10020,10019,8]
    cat_map = dict(zip(cat_id, range(len(cat_id))))

    for i in range(len(imagelist)):
        image_id = imagelist[i]['file_name']
        # image = io.imread(image_path)
        mask = np.zeros((imagelist[i]["height"],imagelist[i]["width"])).astype(np.uint8)
        image_path = os.path.join(OrgImgPath, image_id)
        for j in range(len(seglist)):
            if seglist[j]['image_id'] == image_id:
                s = seglist[j]
                l = cat_map[seglist[j]["category_id"]]
                segm =seglist[j]['segmentation'][0]
                r = np.array(segm[1::2])
                c = np.array(segm[0::2])
                rr, cc = polygon(r, c,(imagelist[i]["height"],imagelist[i]["width"]))
                # rr, cc = polygon(r, c)
                mask[rr, cc] = l
                # mask += np.where(mask==0,True,False)*maskUtils.decode(rle)
        # print(mask.max())
        # print(np.unique(mask))
        # plt.imsave('mass.png',mask)
        io.imsave(image_path.replace('images','mask').replace('jpg','png'),mask,as_grey=True)
        # cv2.imwrite(image_path.replace('images','mask').replace('jpg','png'),mask)

if __name__ == '__main__':
    RootPath = '/data/'
    i=0
    for root,dir,files in os.walk(RootPath,topdown=True):
        for d in dir:
            JsonPath = os.path.join(root,d,'coco.json')
            OrgImgPath = os.path.join(root,d,'images')
            MaskPath = os.path.join(root,d,'mask')
            if not os.path.exists(MaskPath):
                os.makedirs(MaskPath)
            CreatMask(OrgImgPath,JsonPath)
            i=i+1
            print(i)
        break
