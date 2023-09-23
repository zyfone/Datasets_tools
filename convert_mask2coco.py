import os
import cv2
import numpy as np
import json
from pycocotools import mask as coco_mask

# 示例输入：存储 mask 图像的文件夹路径以及相关信息
mask_folder = 'mask_images/'  # 请替换为包含 mask 图像的文件夹路径
image_id = 1  # 图像的唯一ID
category_id = 1  # 物体类别的唯一ID

# 获取文件夹中所有 mask 图像文件的列表
mask_files = os.listdir(mask_folder)

# 创建用于存储 COCO 格式标注的列表
annotations = []

# 遍历每个 mask 图像文件
for mask_file in mask_files:
    # 读取 mask 图像
    mask_image = cv2.imread(os.path.join(mask_folder, mask_file), cv2.IMREAD_GRAYSCALE)
    
    # 将二值 mask 转换为 COCO 格式的多边形
    segmentation = coco_mask.encode(np.asfortranarray(mask_image))
    
    # 计算 mask 的边界框
    bbox = coco_mask.toBbox(segmentation)
    
    # 创建 COCO 格式的标注
    annotation = {
        'image_id': image_id,
        'category_id': category_id,
        'segmentation': segmentation,
        'area': float(coco_mask.area(segmentation)),
        'bbox': bbox.tolist(),
        'iscrowd': 0,
        'id': len(annotations) + 1  # 你需要为每个标注分配一个唯一的ID
    }
    
    # 将标注添加到列表中
    annotations.append(annotation)

# 创建 COCO 数据集对象
coco_dataset = {
    'images': [],
    'annotations': annotations,
    'categories': [{'id': category_id, 'name': 'object'}]  # 这里只有一个类别示例
}

# 指定要保存的 JSON 文件路径
json_filename = 'coco_dataset.json'

# 保存 COCO 数据集为 JSON 文件
with open(json_filename, 'w') as json_file:
    json.dump(coco_dataset, json_file, indent=4)

print(f"COCO dataset saved to {json_filename}")
