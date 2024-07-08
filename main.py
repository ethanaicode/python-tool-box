import subprocess
import random

from globals import APP_ROOT_DIR

def run_magick_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode('utf-8')}")
    else:
        print(result.stdout.decode('utf-8'))

def is_magick_installed():
    try:
        run_magick_command("magick -version")
        return True
    except Exception as e:
        return False

def main():
    if not is_magick_installed():
        print("Error: ImageMagick is not installed.")
        return

    images_handler_chosen = input("你需要什么服务？\n1. 生成图片\n")

    match images_handler_chosen:
        case "1":
            generate_image()
        case _:
            print("Error: Invalid choice.")

def generate_image():
    default_bg_colors = [
        "#90839b",
        "#36a4d6",
        "#536a49",
        "#3a80a8",
        "#5f879e",
        "#13abbf",
        "#283599",
        "#028e85",
        "#008da6",
        "#2983cc",
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
    output_image = ''.join([APP_ROOT_DIR, "/output/output.jpg"])

    command = f"magick {bg_image} +level-colors \"{bg_color},\" -gravity center -fill white -font \"{text_font}\" -pointsize 96 -annotate 0 \"{main_text}\" {output_image}"

    print(f"Running command: {command}\n")
    run_magick_command(command)
    print(f"Output image: {output_image}")

if __name__ == "__main__":
    main()
