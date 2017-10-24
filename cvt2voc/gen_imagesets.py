# -*- coding:utf-8 -*-

import random
import os
from os import listdir
from os.path import join, isfile


__author__ = 'peic'

'''
设置trainval和test数据集包含的图片
'''

_VOC_PATH = '/path/to/your/voc'



if __name__ == '__main__':
    # ImageSets文件夹
    _IMAGE_SETS_PATH = join(_VOC_PATH, 'ImageSets')
    _MAin_PATH = join(_VOC_PATH, 'ImageSets/Main')
    _XML_FILE_PATH = join(_VOC_PATH, 'Annotations')

    # 创建ImageSets数据集
    if os.path.exists(_IMAGE_SETS_PATH):
        print('ImageSets dir is already exists')
        if os.path.exists(_MAin_PATH):
            print('Main dir is already in ImageSets')
    else:
        os.mkdir(_IMAGE_SETS_PATH)
        os.mkdir(_MAin_PATH)

    # f_test = open(os.path.join(_MAin_PATH, 'test.txt'), 'w')
    # f_train = open(os.path.join(_MAin_PATH, 'trainval.txt'), 'w')

    # 遍历XML文件夹
    xml_list = [x for x in listdir(_XML_FILE_PATH) if isfile(join(_XML_FILE_PATH, x)) and not x[0] == '.']
    random.shuffle(xml_list)
    xml_numbers = len(xml_list)
    test_percent, train_percent, val_percent = 0.1, 0.75, 0.15
    test_list = xml_list[:int(xml_numbers*test_percent)]
    train_list = xml_list[int(xml_numbers * test_percent):int(xml_numbers * (test_percent+train_percent))]
    val_list = xml_list[int(xml_numbers * (test_percent+train_percent)):]

    r = '\n'.join([xml.rstrip('.xml') for xml in test_list])
    with open(os.path.join(_MAin_PATH, 'test.txt'), 'w+') as f: f.write(r)

    r = '\n'.join([xml.rstrip('.xml') for xml in train_list])
    with open(os.path.join(_MAin_PATH, 'train.txt'), 'w+') as f: f.write(r)

    r = '\n'.join([xml.rstrip('.xml') for xml in val_list])
    with open(os.path.join(_MAin_PATH, 'val.txt'), 'w+') as f: f.write(r)