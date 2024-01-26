import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('OCR_input2.jpg')
OCR_output= pytesseract.image_to_string(img,lang="eng")

text= open('OCR_output.txt','w')
text.write(OCR_output)
text.close()