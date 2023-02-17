import os
import random 
 
xmlfilepath=r'D:/new_BDD/BDD/night_sunny/VOC2007/Annotations'
saveBasePath=r"D:/new_BDD/BDD/night_sunny/VOC2007/ImageSets/Main/"

trainval_percent=0.7


temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

num=len(total_xml)  
list=range(num)  
tv=int(num*trainval_percent)  
trainval= random.sample(list,tv)  


 
print("trainval size",tv)
print("test",num-tv)
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')  
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')  

 
for i  in list:  
    name=total_xml[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftest .close()
