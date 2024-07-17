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
    bg_image = ''.join([APP_ROOT_DIR, "/assets/images/grayscale_base.png"])
    bg_color = input("请输入背景颜色：默认随机选择\n")
    if(bg_color == ""):
        bg_color = random.choice(default_bg_colors)
    main_text = input("请输入主要文本：默认为#Hello World\n")
    if(main_text == ""):
        main_text = "#Hello World"
    text_font = input("请输入字体：默认为苹方中\n")
    if(text_font == ""):
        text_font = ''.join([APP_ROOT_DIR, "/assets/fonts/PingFang-Mod-19.0d5e3-SC-Medium.otf"])
    output_image = ''.join([APP_ROOT_DIR, f"/output/{main_text}.png"])

    command = f"magick {bg_image} +level-colors \"{bg_color},\" -gravity center -fill white -font \"{text_font}\" -pointsize 96 -annotate 0 \"{main_text}\" {output_image}"

    print(f"Running command: {command}\n")
    run_magick_command(command)
    print(f"Output image: {output_image}")

if __name__ == "__main__":
    main()
