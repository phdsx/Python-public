# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     图片加水印
   Description :
   Author :       phdsx
   date：          2021/4/2
-------------------------------------------------
   Change Activity:
                   2021/4/2:
-------------------------------------------------
"""
from PIL import Image, ImageDraw, ImageFont
import os, time, random


class StartUp():
    def __init__(self):
        self.path_work = os.getcwd()
        self.path_source = self.path_work + "\\原始图片"
        self.path_output = self.path_work + "\\处理完成图片"
        self.judge_folder_exist(self.path_source, self.path_output)
        self.judge_img_exist(self.path_source)
        self.clean_up_output_folder()

    def judge_folder_exist(self, *argv):
        for self.each in argv:
            if os.path.exists(self.each):
                pass
            else:
                os.mkdir(self.each)
                print(self.each.split("\\")[-1] + "文件夹不存在，已创建")

    def judge_img_exist(self, path):
        self.file_list = os.listdir(path)
        self.count = 0
        if len(self.file_list) == 0:
            print("源文件夹为空")
            print("程序将于5秒后自动关闭")
            time.sleep(5)
            exit(0)
        for self.each in self.file_list:
            if self.each.split(".")[-1].lower() in ["jpg", "png", "bmp", "webp"]:
                print(f"找到第{self.count + 1}个图片")
                img_dict[self.count] = self.each
                self.count += 1

            else:
                print("源文件不存在或格式不受支持")
                print("程序将于5秒后自动关闭")
                time.sleep(5)
                exit(0)

    def clean_up_output_folder(self):
        self.output_file_list = os.listdir(self.path_output)
        print("正在清空输出文件夹")
        try:
            for self.each in self.output_file_list:
                os.remove(self.path_output + "\\" + self.each)
            print("输出文件夹清空完成")
        except:
            print("输出文件夹为空")

    def add_text_to_img(self, file_name, text):
        self.path_source = os.getcwd() + "\\原始图片\\" + file_name

        self.image = Image.open(self.path_source)
        self.img_area=self.image.size[0]*self.image.size[1]
        self.font = ImageFont.truetype(r'C:\Windows\Fonts\STKAITI.TTF', self.img_area//8000)
        self.new_img = Image.new('RGBA', (self.image.size[0] * 3, self.image.size[1] * 3), (0, 0, 0, 0))

        self.new_img.paste(self.image, self.image.size)

        self.font_len = len(text)
        self.rgba_image = self.new_img.convert('RGBA')
        self.text_overlay = Image.new('RGBA', self.rgba_image.size, (255, 255, 255, 0))
        self.image_draw = ImageDraw.Draw(self.text_overlay)

        for i in range(0, self.rgba_image.size[0], 2*self.font_len*(self.img_area//10000)):
            for j in range(0, self.rgba_image.size[1], 100):
                self.image_draw.text((i,j ), text,
                                     font=self.font, fill=(0, 0, 0, 50))
        self.text_overlay = self.text_overlay.rotate(-45)
        self.image_with_text = Image.alpha_composite(self.rgba_image, self.text_overlay)

        self.image_with_text = self.image_with_text.crop(
            (self.image.size[0], self.image.size[1], self.image.size[0] * 2, self.image.size[1] * 2))
        self.image_with_text.save(os.getcwd() + "\\处理完成图片\\" + file_name.split(".")[0] + ".png")
        print(f"图片{file_name.split('.')[0] + '.png'}保存成功")


img_dict = {}
pic = StartUp()
text = input("请输入水印文字：")
for i in range(len(img_dict)):
    pic.add_text_to_img(img_dict[i], text)
time.sleep(5)
exit(0)
