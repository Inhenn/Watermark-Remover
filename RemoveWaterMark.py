
import cv2
pixel_set=set()

img = cv2.imread('this_pic.png')#the path+name of your picture
for row in img:
    for pixels in row:
        if pixels[0]>200 or pixels[1]>200 or pixels[2]>200:
            pixels[0]=255
            pixels[1]=255
            pixels[2]=255

cv2.imwrite('image.png', img)#output file
