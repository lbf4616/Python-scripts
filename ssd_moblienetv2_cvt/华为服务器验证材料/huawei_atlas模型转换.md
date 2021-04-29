### 1. 模型转换参数

- --model
```
待转换的tensorflow 的 pb格式模型， .h5 的需要转换为 .pb格式进行转换
```
- --output
```
转换好的om模型需要输出的文件路径以及文件名
```
- --input_shape
```
需要转换输出的图像batch以及size大小
```

+ **h5 2 pb**

```
python /home/blin/Documents/Scripts/h5_to_pb.py \
	--input_model /disk/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_nvidia/vi_piece_offset_single.h5 \
	--output_model /disk/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_nvidia/vi_piece_offset_single.pb
```

### 2. 各模型转换命令

#### 2.1 转换ssd模型

```
1、 直接运行python3.7 cut_faster_rccnn_post_process.py，脚本中输入文件与输出路径改一下，第16行和第236行。

2、 sudo -i 

3、 再运行bash trans_pb2om_without_aipp.sh，如果有需要，改一下第7行的pb文件路径。

/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc --model=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_ssd_single_0316_cut.pb \
    --framework=3 \
    --output=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_atlas/vi_ssd_single_0316 \
    --input_shape="image_tensor:1,512,512,3" \
	--output_type=FP32 \
    --soc_version=Ascend310 \
	--log=info
```

#### 2.2 转换resnet34模型

+ **el_region_cls:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_space_abnormal_0410.pb \
	--framework=3 \
	--output=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_atlas/vi_space_abnormal_0410 \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="data_1:1,128,128,3" \
	--log=info
```

+ **vi_region_cls:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_piece_offset_0322.pb \
	--framework=3 \
	--output=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_atlas/vi_piece_offset_0322  \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="data:1,224,224,3" \
	--log=info
```

+ **el_piece_unbalanced:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_unbalanced.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_unbalanced \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="data_1:1,64,1024,3" \
	--log=info
```

+ **vi_fold_abnormal:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_fold_abnormal.pb \
	--framework=3 \
	--output=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_atlas/vi_fold_abnormal \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="data_1:1,224,224,3" \
	--log=info
```



#### 2.3 转换yolo模型

+ **el_yolo:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_yolo_single_0317.pb \
	--framework=3 \
	--output=/dsk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_atlas/vi_yolo_single_0317 \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="image:1,416,416,3" \
	--log=info
```

+ **vi_yolo:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_nvidia/vi_yolo_single_0122.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_yolo_single_0122 \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="image:1,416,416,3" \
	--log=info
```

+ **vi_piece_offset_yolo:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_offset_yolo.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_offset_yolo \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input/input_data:1,384,384,3" \
	--log=info
```



#### 2.4 转换unet模型

+ **el_piece_cut:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_nvidia/el_piece_cut.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_cut \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,512,2048,3" \
	--log=info
```

+ **vi_piece_cut:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_offset_single1.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_offset_single1 \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,224,384,3" \
	--log=info
```

+ **el_short_circuit_cut:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_nvidia/el_short_circuit_cut.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_short_circuit_cut \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,512,1024,3" \
	--log=info
```

+ **el_seg_roi_unet:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_nvidia/el_seg_roi_unet.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_seg_roi_unet \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,512,512,3" \
	--log=info
```

+ **vi_piece_shift:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_shift_1.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_shift_1 \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,384,1024,3" \
	--log=info
```

+ **vi_piece_offset**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_shift.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_piece_shift \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,384,1024,3" \
	--log=info
```



#### 2.5 分类小网络

+ **el_region_cls_pp:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_region_cls_pp.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_region_cls_pp \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="conv2d_input:1,45,45,3" \
	--log=info
```

#### 2.6 VGG (el_piece_unbalanced_anban, el_piece_unbalanced_elbujun)

+ **el_piece_unbalanced_anban:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_unbalanced_anban.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_unbalanced_anban \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,64,1024,3" \
	--log=info
```

+ **el_piece_unbalanced_elbujun:**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_unbalanced_elbujun.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_el/models_atlas/el_piece_unbalanced_elbujun \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,64,1024,3" \
	--log=info
```

### 2.7 MobileNet ###

+ **vi_space_abnormal_single.pb(串间距)**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_space_abnormal_single.pb \
	--framework=3 \
	--output=/home/blin/Pictures/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_atlas/vi_space_abnormal_single \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,128,128,3" \
	--log=info
```

+ **vi_piece_offset_single.pb**

```
/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc \
	--model=/disk/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_nvidia/vi_piece_offset_single.pb \
	--framework=3 \
	--output=/disk/huansheng_inspection_pipeline_lbf/solar_defect_detection_vi/models_nvidia/vi_piece_offset_single \
	--soc_version=Ascend310 \
	--output_type=FP32 \
	--input_shape="input_1:1,224,224,3" \
	--log=info
```



### 3. 推理样例路径 ###

```
/usr/local/Ascend/ascend-toolkit/latest/pyACL/sample/
```

### 4. 环境变量

```
export PATH=/usr/local/python3.7.5/bin:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/ccec_compiler/bin:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/bin:$PATH

#export PYTHONPATH=/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/python/site-packages/te:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/python/site-packages/topi:$PYTHONPATH

export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/lib64:$LD_LIBRARY_PATH

export ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/opp

export PYTHONPATH=/usr/local/Ascend/ascend-toolkit/latest/pyACL/python/site-packages/acl/:$PYTHONPATH

export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/acllib/lib64:$LD_LIBRARY_PATH

export PYTHONPATH=/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/python/site-packages:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/python/site-packages/auto_tune.egg/auto_tune:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/atc/python/site-packages/schedule_search.egg:$PYTHONPATH
echo "ASCEND ACITVATED"

```