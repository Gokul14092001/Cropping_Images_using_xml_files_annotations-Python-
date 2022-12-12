import glob 
import xml.etree.ElementTree as ET 
from PIL import Image


#adding images in a folder to list
li=[]
for j in glob.glob("E:/gokul/PascalVOC-to-Images/data/*.jpg"): #path to data folder(should contain image and xml in same folder)
    li.append(j)

#for cropping images from a list by using bounding box in pascal voc(xml)
count=0
for i in glob.glob("E:/gokul/PascalVOC-to-Images/data/*.xml"): #path to data folder(should contain image and xml in same folder)
    # print('name',j)
    tree = ET.parse(i)
    # print('tree',tree)

    root = tree.getroot()
    # print('root',root)

    objects = root.findall('object')
    # print('objects',objects)
    temp=0
    for o in objects:
        bndbox = o.find('bndbox') # reading bound box
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        print(xmin,ymin,xmax,ymax)
        bbox=(xmin,ymin,xmax,ymax)
        # print('fin',bbox)
        image=li[count]
        im=Image.open(image)
        im=im.crop(bbox)
        im.show()
        im.save(f"E:/gokul/PascalVOC-to-Images/output/cropped_image{count}_{temp}.jpg") #set save directory(E:/gokul/PascalVOC-to-Images/output/)
        temp=temp+1
    count=count+1