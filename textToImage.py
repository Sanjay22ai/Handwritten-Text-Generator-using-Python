import cv2
import os
import textwrap

DIR = r'C:\Users\KIIT\OneDrive\Desktop\New Project\charset'

def crop(img,cropX=10, cropY=10):
    cropped= img[cropY:img.shape[0]-cropY,cropX:img.shape[1]-cropX]
    return cropped

def rescale(img, scaleX=0.75, scaleY=0.75):
    rescaled= cv2.resize(img, None,fx=scaleX, fy=scaleY)
    return rescaled

def lineToimg(line):
    char_imgs =[]
    for letter in line:
        if ord(letter)>127:
            letter = ' '
        ascii = ord(letter)
        path= os.path.join(DIR, str(ascii)+".jpg")
        char_img=cv2.imread(path)
        char_imgs.append(crop(char_img, 27))
    img_h = cv2.hconcat(char_imgs)
    return img_h

line_imgs=[]
para_imgs=[]

f= open('OCR_output.txt','r')
lines= f.read().splitlines()

lineWidth= 45

wrapper = textwrap.TextWrapper(width=lineWidth, initial_indent=' ', subsequent_indent=' ')

for i in lines:
    line_list= wrapper.wrap(text=i)
    if len(line_list)==0:
        line_list=' '
    for line in line_list:
        while len(line)!=lineWidth:
            line=line+' '
        line_imgs.append(lineToimg(line))
    img_v = cv2.vconcat(line_imgs)
    para_imgs.append(img_v)
    line_imgs.clear()
image = cv2.vconcat(para_imgs)

rescaled = rescale(image, 0.24, 0.27)

cv2.imshow('Handwritten', rescaled)
cv2.imwrite('Handwritten.jpg', rescaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('---SUCCESSFULLY CONVERTED---')