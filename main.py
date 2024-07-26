import subprocess
import random

from globals import APP_ROOT_DIR

from components.magick_command import Magick
from components.generate_image import generateImage

def main():
    if not Magick.is_magick_installed():
        print("Error: ImageMagick is not installed.")
        return

    images_handler_chosen = input("你需要什么服务？\n1. 生成图片\n2. 转换图片\n0. 退出\n")

    match images_handler_chosen:
        case "1":
            generate_cls = generateImage()
            generate_cls.generate_image()
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
                    Magick.run_magick_command(command)
                    print(f"Output image: {output_image}")
                case "0":
                    print("Goodbye!")
                case _:
                    print("Error: Invalid choice.")
        case "0":
            print("Goodbye!")
        case _:
            print("Error: Invalid choice.")

if __name__ == "__main__":
    main()
