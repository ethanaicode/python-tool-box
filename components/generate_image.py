import random

from globals import APP_ROOT_DIR

from components.magick_command import magickCli

class generateImage:
    def generate_image(self):
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
        bg_image_id_select = input("请选择背景图片：默认随机选择\n1. base01\n2. base02\n3. base03\n")
        if bg_image_id_select == "":
            bg_image_id_select = random.randint(1, 3)
        bg_image = ''.join([APP_ROOT_DIR, f"/assets/images/grayscale_base_{bg_image_id_select}.png"])
        print(f"已选择背景图片: {bg_image}\n")
        # define background color
        bg_color = input("请输入背景颜色：默认随机选择\n")
        if(bg_color == ""):
            bg_color = random.choice(default_bg_colors)
        print(f"已选择背景颜色: {bg_color}\n")
        # define main text
        main_text = input("请输入主要文本：默认为#HelloWorld\n")
        if(main_text == ""):
            main_text = "#HelloWorld"
        print(f"已输入文本: {main_text}\n")
        # define font size
        font_size = self.get_font_size()
        print(f"已输入字体大小: {font_size}\n")
        # define font
        text_font = input("请输入字体：默认为苹方中\n")
        if(text_font == ""):
            text_font = ''.join([APP_ROOT_DIR, "/assets/fonts/PingFang-Mod-19.0d5e3-SC-Medium.otf"])
        print(f"已选择字体: {text_font}\n")
        # default output file
        output_image = ''.join([APP_ROOT_DIR, f"/output/{main_text}.png"])
        text_color = "white"

        # run magick command
        command = f"magick {bg_image} -colorspace Gray -fill \"{bg_color}\" -tint 100 -gravity center -fill \"{text_color}\" -font \"{text_font}\" -pointsize {font_size} -annotate 0 \"{main_text}\" \"{output_image}\""

        print(f"开始生成图片: {command}")
        magickCli.run_magick_command(command, is_print=False)
        print(f"图片已生成: {output_image}")

    def get_font_size(self, default_size="96"):
        while True:
            text_size = input(f"请输入字体大小：默认为{default_size}\n默认配置适合中文5个字，英文10个字\n")
            if not text_size:
                return default_size
            if text_size.isdigit():
                return text_size
            print("Error: Invalid font size.")