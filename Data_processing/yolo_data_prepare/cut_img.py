import cv2
import json
import os
from glob import glob
from copy import deepcopy
import matplotlib.pyplot as plt
from tqdm import tqdm


im_ls = glob('/home/blin/Pictures/数据收集/破片/*.jpg')
save_dir = '/home/blin/Pictures/huansheng/big_img/cutted/'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

for im in tqdm(im_ls[:]):
    # im = '/home/blin/Pictures/huansheng/big_img/ng_all/Q38D10379710_el.jpg'
    img = cv2.imread(im)
    name = os.path.basename(im)
    img_1 = img[:-150, :int(img.shape[1] / 2), :]
    img_2 = img[:-150, img.shape[1] - int(img.shape[1] / 2):, :]
    # plt.imshow(img_1)
    # plt.show()
    # plt.imshow(img_2)
    # plt.show()
    data_1 = {
        "version": "4.2.10",
        "flags": {},
        "shapes": [],
        "imagePath": "",
        "imageData": None,
        "imageHeight": 0,
        "imageWidth": 0
    }

    shape_1 = {
        "label": "",
        "points":[],
        "group_id": None,
        "shape_type": "rectangle",
        "flags": {}
    }

    data_2 = deepcopy(data_1)
    shape_2 = deepcopy(shape_1)
    shapes_1 = []
    shapes_2 = []

    with open(im.replace('.jpg', '.json'), 'r') as f:
        data = json.load(f)
    for bad in data['shapes']:
        points = bad["points"]
        xmid = (points[0][0] + points[1][0]) / 2
        if xmid < int(img.shape[1] / 2):
            bad["points"][1][0] = min(bad["points"][1][0], img_1.shape[1] - 1)
            bad["points"][1][1] = min(bad["points"][1][1], img_1.shape[0] - 1)
            shapes_1.append(bad)
        else:
            bad["points"][0][0] -= int(img.shape[1] / 2)
            bad["points"][1][0] -= int(img.shape[1] / 2)
            bad["points"][1][1] = min(bad["points"][1][1], img_2.shape[0] - 1)
            shapes_2.append(bad)
    if shapes_1 != []:
        data_1["shapes"] = shapes_1
        name_1 = name[:-4] + '_1' + name[-4:]
        data_1["imagePath"] = name_1
        data_1["imageHeight"] = img_1.shape[0]
        data_1["imageWidth"] = img_1.shape[1]
        cv2.imwrite(os.path.join(save_dir, name_1), img_1)
        with open(os.path.join(save_dir, name_1.replace('jpg', 'json')), 'w') as f:
            json.dump(data_1, f, indent=2)

    if shapes_2 != []:
        data_2["shapes"] = shapes_2
        name_2 = name[:-4] + '_2' + name[-4:]
        # print(name_2)
        data_2["imagePath"] = name_2
        data_2["imageHeight"] = img_2.shape[0]
        data_2["imageWidth"] = img_2.shape[1]
        cv2.imwrite(os.path.join(save_dir, name_2), img_2)
        with open(os.path.join(save_dir, name_2.replace('jpg', 'json')), 'w') as f:
            json.dump(data_2, f, indent=2)

