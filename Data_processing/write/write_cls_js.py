import json
from json import dumps
import os
from glob import glob

im_path = '/home/blin/Projects/small_corner_cls/dogs-vs-cats/train/'
im_ls = glob(im_path + '/*.jpg')


data = {
            "record": [],
            "class_dict": [
                {
                    "class_name": "cat"
                },
                {
                    "class_id": 1,
                    "class_name": "dog"
                }
            ]
        }

for im in im_ls[:]:
    

    record = {
                "info": {
                    "image_path": im
                },
                "gt_inst": [
                    {
                        "class_name": os.path.basename(im).split('.')[0]
                    }
                ]
            }
    data["record"].append(record)

write_data = dumps(data, indent=4)
with open('./train.json', 'w') as json_file:
    json_file.write(write_data)