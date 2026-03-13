import os
from PIL import Image

def resize_png_images(input_folder, output_folder, max_width=1024):
    """
    将输入文件夹中的所有PNG图片按比例缩小，保持宽高比，并保存到输出文件夹。
    文件大小会因尺寸减小而显著降低。
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # 打开图片
                with Image.open(input_path) as img:
                    # 获取原始尺寸
                    original_width, original_height = img.size

                    # 如果原始宽度已经小于或等于最大宽度，可以选择直接复制（或者也做优化）
                    if original_width <= max_width:
                        print(f"{filename} 宽度 {original_width} <= {max_width}，直接保存优化版")
                        # 仍然保存一下，启用优化可能会略微减小文件大小
                        img.save(output_path, optimize=True)
                        continue

                    # 计算新尺寸，保持宽高比
                    new_width = max_width
                    new_height = int(original_height * (max_width / original_width))

                    # 调整尺寸（使用抗锯齿）
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # 保存为PNG，启用优化
                    resized_img.save(output_path, optimize=True)

                    print(f"已处理: {filename} ({original_width}x{original_height} -> {new_width}x{new_height})")

            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")

if __name__ == "__main__":
    # 请修改为你的文件夹路径
    input_folder = "D:\\code\\web\\qitupage\\pic"   # 原始图片所在文件夹
    output_folder = "D:\\code\\web\\qitupage\\pic" # 缩小后图片保存的文件夹
    max_width = 1024  # 你可以根据需要调整最大宽度

    resize_png_images(input_folder, output_folder, max_width)