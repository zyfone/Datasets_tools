import os
import cv2
import json
import numpy as np

# 输入文件夹路径
images_folder = "Kvasir-SEG/images"  # 存放目标图像的文件夹
masks_folder = "Kvasir-SEG/masks"    # 存放掩码图像的文件夹
output_json_file = "Kvasir-SEG.json"  # 输出的COCO格式JSON文件
threshold_area = 100  # 阈值面积，小于这个面积的区域将被过滤

# 获取目标图像文件列表
image_files = os.listdir(images_folder)

# 初始化COCO格式的标注数据结构
coco_data = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "polyp"}]  # 自定义目标类别名
}

# 遍历目标图像文件列表
for img_id, img_file in enumerate(image_files):
    image = cv2.imread(os.path.join(images_folder, img_file))
    height, width, _ = image.shape

    # 添加图像信息
    coco_data["images"].append({
        "id": img_id,
        "file_name": img_file,
        "width": width,
        "height": height
    })

    # 获取对应的掩码图像
    mask_file = os.path.join(masks_folder, img_file)  # 假设掩码图像的扩展名与图像相同

    # 读取掩码图像
    mask = cv2.imread(mask_file, cv2.IMREAD_GRAYSCALE)

    # 使用阈值处理掩码图像
    _, mask_thresholded = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)

    # 找到掩码的轮廓
    contours, _ = cv2.findContours(mask_thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 初始化边界框列表
    bounding_boxes = []

    # 计算每个轮廓的边界框
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h

        # 过滤掉小于阈值的区域
        if area >= threshold_area:
            bounding_boxes.append([x, y, w, h])

    # 添加注释信息
    for bbox in bounding_boxes:
        x, y, w, h = bbox
        area = int(w * h)

        coco_data["annotations"].append({
            "id": len(coco_data["annotations"]),
            "image_id": img_id,  # 将图像的唯一ID分配给注释
            "category_id": 1,  # 目标类别的ID
            "segmentation": [],  # 这里可以保持空列表，因为已经有边界框信息
            "area": area,
            "bbox": [x, y, w, h],  # 以[x, y, width, height]格式表示
            "iscrowd": 0
        })

# 将COCO数据保存为JSON文件
with open(output_json_file, "w") as json_file:
    json.dump(coco_data, json_file)
