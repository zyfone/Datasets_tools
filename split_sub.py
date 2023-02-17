import os
import random 
 
xmlfilepath=r'BDD\daytime_clear\VOC2007\ImageSets\Main\all.txt'
saveBasePath=r"D:/new_BDD/BDD/daytime_clear/VOC2007/ImageSets/Main/"

trainval_percent=0.7


temp_xml = open(xmlfilepath, "r",encoding='utf-8')
train_lines = temp_xml.readlines()
total_xml = train_lines
temp_xml.close()

num=len(total_xml)  
list=range(num)  
tv=int(num*trainval_percent)  
trainval= random.sample(list,tv)  


 
print("trainval size",tv)
print("test",num-tv)
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')  
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')  

 
for i  in list:  
    name=total_xml[i]
    if i in trainval:  
        ftrainval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftest .close()
