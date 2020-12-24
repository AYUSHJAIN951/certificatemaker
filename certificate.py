# Python program to explain cv2.putText() method 
# a=input().split(" ")
# print(len(a))

import csv
import string

import os
a=[]
with open('list.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for Namee in csvReader:
        a.append(Namee)
        

print(a)

def newname(name):
    newname=""
    name=name.split(" ")
    leng=len(name)
    for i in name:
        newname += i.capitalize()+" "

    return(newname)
i=0
for j in range(len(a)):
    # importing cv2 
    import cv2
    
    name=str(a[i][0])	
    
    i=i+1
    # path
    print(i)
    print(name)
    name=string.capwords(name)
    path = r'certificate (9).png'
        
    # Reading an image in default mode 
    image = cv2.imread(path) 
    height , width  = image.shape[:2]

    # Window name in which image is displayed 
    window_name = 'Image'

    # font 
    font = cv2.FONT_HERSHEY_COMPLEX 

    # fontScale 
    fontScale = 2.5

    # Blue color in BGR 
    color = (0, 0, 0) 

    # Line thickness of 2 px 
    thickness = 5
    
    #
    # Name is formatted properloy for capitalisation
    name=newname(name)
    
    #
    fontScale = 2.3
    fontThickness = 1
    fontFace=font
# make sure font thickness is an integer, if not, the OpenCV functions that use this may crash
    fontThickness = int(fontThickness)

    scale=1
    textSize, baseline = cv2.getTextSize(name, fontFace, fontScale, fontThickness)
    textSizeWidth, textSizeHeight = textSize

    org = (int(1050-textSizeWidth/2),int(680 - textSizeHeight))

    








    # Using cv2.putText() method 
    image = cv2.putText(image, name , org, font, 
                    fontScale, color, thickness, cv2.LINE_AA) 

    # Displaying the image 
    # cv2.imshow(window_name, image)
    path="certs/"
    if (os.path.isdir(path) == False):
        os.mkdir("certs")
        print("Certs created")
    
    cv2.imwrite(path+name+".jpg",image) 


