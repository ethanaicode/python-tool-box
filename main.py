import subprocess
import random

from globals import APP_ROOT_DIR

def run_magick_command(command, is_print=True):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        if is_print:
            print(f"Error: {result.stderr.decode('utf-8')}")
        raise Exception(f"Error: {result.stderr.decode('utf-8')}")
    else:
        if is_print:
            print(result.stdout.decode('utf-8'))

def is_magick_installed():
    try:
        run_magick_command(command = "magick -version", is_print=False)
        return True
    except Exception as e:
        return False

def main():
    if not is_magick_installed():
        print("Error: ImageMagick is not installed.")
        return

    images_handler_chosen = input("你需要什么服务？\n1. 生成图片\n2. 转换图片\n0. 退出\n")

    match images_handler_chosen:
        case "1":
            generate_image()
        case "2":
            images_transform_chosen = input("你需要什么服务？\n1. 转换png图片为ico\n0. 退出\n")
            match images_transform_chosen:
                case "1":
                    input_image = input("请输入图片路径：\n")
                    # Check if the image exists
                    check_image = subprocess.run(f"magick identify {input_image}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if check_image.returncode != 0:
                        print(f"Error: {check_image.stderr.decode('utf-8')}")
                        return
                    output_image = input("请输入输出图片路径：默认为./output/favicon.ico\n")
                    if(output_image == ""):
                        output_image = ''.join([APP_ROOT_DIR, "/output/favicon.ico"])
                    command = f"magick convert {input_image} -define icon:auto-resize=256,128,96,64,48,32,16 {output_image}"
                    print(f"Running command: {command}\n")
                    run_magick_command(command)
                    print(f"Output image: {output_image}")
                case "0":
                    print("Goodbye!")
                case _:
                    print("Error: Invalid choice.")
        case "0":
            print("Goodbye!")
        case _:
            print("Error: Invalid choice.")

def generate_image():
    default_bg_colors = [
        "#90839b",
        "#536a49",
        "#3a80a8",
        "#5f879e",
        "#13abbf",
        "#3e2ca9",
        "#7843aa",
        "#283599",
        "#2a488c",
        "#028e85",
        "#008da6",
        "#36a4d6",
        "#2983cc",
        "#316bff",
        "#1a73e8",
        "#9ab27c",
        "#22b14c",
        "#4ca4c4",
        "#745274",
        "#5f889e",
    ]
    # define background grayscale image
    bg_image_id_select = input("请选择背景图片：默认随机选择\n1. base01\n2. base02\n")
    if bg_image_id_select == "":
        bg_image_id_select = random.randint(1, 2)
    bg_image = ''.join([APP_ROOT_DIR, f"/assets/images/grayscale_base_{bg_image_id_select}.png"])
    print(f"已选择背景图片: {bg_image}\n")
    # define background color
    bg_color = input("请输入背景颜色：默认随机选择\n")
    if(bg_color == ""):
        bg_color = random.choice(default_bg_colors)
    print(f"已选择背景颜色: {bg_color}\n")
    # define main text
    main_text = input("请输入主要文本：默认为#Hello World\n")
    if(main_text == ""):
        main_text = "#Hello World"
    print(f"已输入文本: {main_text}\n")
    # define font size
    font_size = get_font_size()
    print(f"已输入字体大小: {font_size}\n")
    # define font
    text_font = input("请输入字体：默认为苹方中\n")
    if(text_font == ""):
        text_font = ''.join([APP_ROOT_DIR, "/assets/fonts/PingFang-Mod-19.0d5e3-SC-Medium.otf"])
    print(f"已选择字体: {text_font}\n")
    # default output file
    output_image = ''.join([APP_ROOT_DIR, f"/output/{main_text}.png"])

    # run magick command
    command = f"magick {bg_image} +level-colors \"{bg_color},\" -gravity center -fill white -font \"{text_font}\" -pointsize {font_size} -annotate 0 \"{main_text}\" \"{output_image}\""

    print(f"开始生成图片: {command}")
    run_magick_command(command, is_print=False)
    print(f"图片已生成: {output_image}")

def get_font_size(default_size="96"):
    while True:
        text_size = input(f"请输入字体大小：默认为{default_size}\n默认配置适合中文4个字，英文8个字\n")
        if not text_size:
            return default_size
        if text_size.isdigit():
            return text_size
        print("Error: Invalid font size.")

if __name__ == "__main__":
    main()
