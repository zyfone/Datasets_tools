import os
import cv2
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pycocotools.coco import COCO

# COCO格式的JSON文件路径
coco_json_file = "ETIS-LARIB.json"

images_folder = "ETIS-LARIB\images_RGB"  # 存放目标图像的文件夹

# 初始化COCO API
coco = COCO(coco_json_file)

# 获取所有图像的ID
image_ids = coco.getImgIds()

# 定义类别ID到类别名称的映射
categories = {1: "polyp"}  # 您的类别ID和名称映射

# 遍历图像并可视化边界框和类别名称
for image_id in image_ids:
    # 获取图像信息
    image_info = coco.loadImgs(image_id)[0]
    image_file = image_info["file_name"]
    image = cv2.imread(os.path.join(images_folder, image_file))

    # 获取图像的标注信息
    annotation_ids = coco.getAnnIds(imgIds=image_info['id'])
    annotations = coco.loadAnns(annotation_ids)

    # 创建Matplotlib图像对象
    plt.figure()
    
    # 显示图像
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 绘制边界框和类别名称
    for annotation in annotations:
        bbox = annotation["bbox"]
        print(bbox)
        x, y, width, height = map(int, bbox)
        category_id = annotation["category_id"]
        category_name = categories.get(category_id, "Unknown")
        
        rect = Rectangle((x, y), width, height, fill=False, color='red', linewidth=2)
        plt.gca().add_patch(rect)
        
        plt.text(x, y, category_name, color='red', backgroundcolor='white', fontsize=10)

    # 显示图像边界框
    plt.axis('off')
    plt.show()
    print("~~~~~~~~~~~~~~")