## 遥感语义分割比赛

### 1、[比赛地址](https://datacontest.fjbdg.com.cn/v3/cmptDetail.html?id=878)

### 2、数据上传在toUser.zip

​		***同样可以直接通过官网提供的网址[下载](https://pan.baidu.com/share/init?surl=LbEs7q5F_uoErDTBAi7LBw) 提取码：sb4h***

### 3、[比赛提交细则](https://pu-datacastle.obs.cn-north-1.myhuaweicloud.com/%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BA%A4%E7%A4%BA%E4%BE%8B.html)

### 4、项目介绍

项目地址位于4090 ubuntu系统`/home/msi2/wzb/FuJian`

`FuJian_iChen`

**├── crop.py**   
**├── data**  # 数据  
**│   ├── FuJian_img1**  # 数据1  
**│   └── FuJian_img2**  # 数据2  
**├── README.md**  
**└── toUser** # 官方数据  
    **├── submit_example.zip** # 提交示例  
    **└── train** 

[git教程](https://www.bilibili.com/video/BV1r3411F7kn/?spm_id_from=333.337.search-card.all.click&vd_source=764979a4787f7e93c23804b906ecf5ac)

`corp.py文件是用于图像处理，将大的遥感影像划分为512*512小的图像`

```python
class Config:

    image_path = r"toUser/toUser/train/img1/img1.tif" # 配置原始影像的地址
    mask_path = r"toUser/toUser/train/img1/img1_ mask.tif" # 配置mask影像的地址
    size = 512 # 设置大小，可以为int也可以为tuple

    crop = dict(
        size=size,
        work_dir=r"./data", # 保存的路径
        data_name="FuJian_img1", # 为数据起名
        # 数据分割后放在./data/FuJian_img1/train 与 ./data/FuJian_img1/lable之中
        drop_out=True
        # 设置是否丢弃不足size的块
    )
```

