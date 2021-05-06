# SSD-TensorRT

## 模型转换

### 1. 修改anchor参数

```
vim ./build_engine.py

line 171    aspectRatios
            # keep same as config
            aspectRatios=[1.0, 2.0, 0.5, 3.0, 0.33, 10.0, 0.1]  
            
line 175    featureMapShapes
            # 300 * 300
            featureMapShapes=[19, 10, 5, 3, 2, 1],
            # 512 * 512
            featureMapShapes=[32, 16, 8, 4, 2, 1],
```

### 2. 转换模型

```
python build_engine.py ssd_mobilenet_v2_coco
```
