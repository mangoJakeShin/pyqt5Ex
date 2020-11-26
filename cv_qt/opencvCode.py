from PIL import Image
import cv2
import os
from matplotlib import pyplot as plt

def actResize(src, choice):
    if choice == 1:
        size = (256, 256)
        dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
        return dst

def actRotate(src, choice):
    if choice == 1:
        height, width, channel = src.shape
        matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
        dst = cv2.warpAffine(src, matrix, (width, height))
        return dst

def actBlur(src, choice):

    if choice == 1:
        dst = cv2.blur(src, (5, 5))
        #setting new image's name
        #writing image - dstname = path, dst = image
        return dst


def actCrop(src, choice):
    if choice == 1:
        y,x,z = src.shape
        if(y>20 and x > 20):
            dst = src[y//2:y, x//2:x]
        return dst


def actSave(src):
    global path
    global count
    dstname = path + "change.%i" % count + ".jpg"
    cv2.imwrite(dstname, src)
    count += 1
    print(dstname + " saved")
