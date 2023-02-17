from shutil import copy
from tqdm import tqdm

 
xmlfilepath=r'D:\new_BDD\BDD\night_sunny\VOC2007\ImageSets\Main\all.txt'

old_path=r"D:\new_BDD\BDD\night_sunny\VOC2007\Annotations_old\\"
new_path=r"D:\new_BDD\BDD\night_sunny\VOC2007\Annotations\\"

#daytime_clear            night_sunny


temp_xml = open(xmlfilepath, "r",encoding='utf-8')
train_lines = temp_xml.read().splitlines()
total_xml = train_lines
for file in tqdm(total_xml):
    file=file+'.xml'
    copy(old_path+file,new_path+file)

temp_xml.close()