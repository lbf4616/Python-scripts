from glob import glob
import os
import shutil
from tqdm import tqdm
import json

json_ls = glob("/home/blin/tmp/gitlab/linbofan/co/*.json")

# for json_l in tqdm(json_ls):
#     shutil.move(json_l, json_l.replace('0', 'co'))
#     shutil.move(json_l.replace('json', 'jpg'), json_l.replace('json', 'jpg').replace('0', 'co'))

# json_lss = "/home/blin/tmp/project_data/atesi/recognition/single/data_processed/small2020_v2/ng/"
# sub_file = os.listdir(json_lss)

# for json_l in tqdm(sub_file[:]):
#     print(json_l)
#     json_ls = glob(json_lss + json_l + '/*.json')
#     for json_f in json_ls:
#         # print(json_f)
#         with open(json_f, 'r') as fid:
#             info = json.load(fid)
#         bad_ls = info['shapes']
#         for bad in bad_ls:
#             label = bad['label']
#             # print(label)
#             if label == '0':
#                 print(json_f)
#                 fid.close()
#                 fpath,fname=os.path.split(json_f)
#                 print()
#                 shutil.copyfile(json_f.replace('json', 'jpg'), "/home/blin/tmp/gitlab/linbofan/0/" + fname.replace('json', 'jpg'))
#                 break

from json import dumps

for json_f in json_ls:
    print(json_f)
    with open(json_f, 'r') as fid:
        info = json.load(fid)
    bad_ls = info['shapes']
    for bad in bad_ls:

        x1, y1 = bad['points'][0]
        x2, y2 = bad['points'][1]
        xmin = min(x1, x2)
        ymin = min(y1, y2)
        bad['points'][0] = [xmin, ymin]
        bad['points'][1] = [xmin + 45, ymin + 45]
    
    write_data = dumps(info)
    with open(json_f, 'w') as fid:
        fid.write(write_data)
