    应用于边界测量

# 建模

## 假设

    观察数据集，做出一些切片的假设

1. 切口部分的形状均为近似长方形
2. 切口部分可不平行于图像边缘
3. 非切口部分（背景）的图像特征近似相同

## 思路

1. 由于切口部分形状近似长方形，所以当切口平行于图像边缘时，可以用图像每行的像素平均值来区分图像该行属于背景还是切口；（主要思路）
2. 图像旋转可以将切口调整到平行图像的位置；

## 实践

1. 使用 HSV 模型描述图像
2. 使用 Pillow 库处理图像
3. 使用简单的二分类模型区分图像(待完成)
