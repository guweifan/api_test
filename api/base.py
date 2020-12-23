# -*- coding: utf-8 -*-
import base64

def get_image_01_base():
    image_path = "D:\\Python_work\\walnuts_api\\api_test\\img\\1.jpg"
    with open(image_path, 'rb') as f:
        image = f.read()
        image_01 = str(base64.b64encode(image), encoding='utf-8')
    return image_01

def get_image_02_base():
    image_path = "D:\\Python_work\\walnuts_api\\api_test\\img\\2.jpg"
    with open(image_path, 'rb') as f:
        image = f.read()
        image_02 = str(base64.b64encode(image), encoding='utf-8')
    return image_02

def get_image_03_base():
    image_path = "D:\\Python_work\\walnuts_api\\api_test\\img\\3.jpg"
    with open(image_path, 'rb') as f:
        image = f.read()
        image_03 = str(base64.b64encode(image), encoding='utf-8')
    return image_03

if __name__ == "__main__":
    print(get_image_01_base())