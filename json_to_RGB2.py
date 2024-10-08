from PIL import Image, ImageDraw
import json
import os
import hashlib

def get_color(label):
    # 使用哈希函数将标签映射为颜色值
    hash_object = hashlib.sha256(label.encode())
    hash_hex = hash_object.hexdigest()
    return "#" + hash_hex[:6]  # 取哈希值的前6位作为颜色值

def create_label_image(json_file_path, output_folder_path):
    # 以UTF-8编码打开JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # 获取图像信息
    image_path = data['imagePath']
    image_width = data['imageWidth']
    image_height = data['imageHeight']

    # 创建空白图像
    label_image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(label_image)

    # 提取标注信息并绘制标签
    for shape in data['shapes']:
        label = shape['label']
        points = shape['points']

        # 获取颜色
        color = get_color(label)

        # 将多段线坐标转换为整数坐标
        polygon = [(int(x), int(y)) for x, y in points]

        # 绘制多段线
        for i in range(len(polygon) - 1):
            draw.line([polygon[i], polygon[i + 1]], fill=color, width=2)

        # 填充区域
        draw.polygon(polygon, outline=color, fill=color)

    # 确保输出文件夹存在
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 生成标签图像的文件名（假设保存为PNG格式）
    output_image_filename = os.path.splitext(os.path.basename(json_file_path))[0] + '.jpg'
    output_image_path = os.path.join(output_folder_path, output_image_filename)

    # 保存标签图像
    label_image.save(output_image_path)

# 示例用法
json_folder = ''
output_folder = ''

# 遍历JSON文件夹中的所有文件并生成标签图像
for json_filename in os.listdir(json_folder):
    if json_filename.endswith('.json'):
        json_file_path = os.path.join(json_folder, json_filename)
        create_label_image(json_file_path, output_folder)
