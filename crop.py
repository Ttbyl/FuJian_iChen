

from PIL import Image, ImageFile
import os

# 去除加载图像块大小限制
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 去除图像加载最大像素限制
Image.MAX_IMAGE_PIXELS = None


class Config:

    image_path = r"toUser/toUser/train/img1/img1.tif"
    mask_path = r"toUser/toUser/train/img1/img1_ mask.tif"
    size = 512

    crop = dict(
        size=size,
        work_dir=r"./data",
        data_name="FuJian_img1",
        drop_out=True
    )


class rs_data_prossing:
    def __init__(self, cfg):
        self.cfg = cfg
        self.check_path("cfg.image_path", self.cfg.image_path)
        self.check_path("cfg.mask_path", self.cfg.mask_path)

        self.mask = None
        self.image = None


    def crop(self,
             size=None,
             drop_out: bool = True,
             work_dir: str = None):
        # 打开影像
        self.open()

        size = self.cfg.crop['size'] if size == None else size

        # 判断size是否为tuple或者int类型
        if not isinstance(size, (tuple, int)):
            raise TypeError('size 必须是 tuple 或 int')
        # 如果是int类型转换成tuple类型
        if isinstance(size, int):
            size = (size, size)

        width = self.image.width
        height = self.image.height
        width_crop = width // size[0]
        height_crop = height // size[1]

        if drop_out != self.cfg.crop['drop_out']:
            width_crop += 1
            height_crop += 1


        # 保存裁剪后的图像路径
        work_dir = self.cfg.crop['work_dir'] if work_dir == None else work_dir
        work_dir = os.path.join(work_dir, self.cfg.crop['data_name']) if self.cfg.crop['data_name'] != None else work_dir
        image_save_path = os.path.join(work_dir, "train")
        os.makedirs(image_save_path, exist_ok=True)

        mask_save_path = os.path.join(work_dir, "val")
        os.makedirs(mask_save_path, exist_ok=True)

        # 保存images和masks裁剪后的图像
        cnt = 0
        for w in range(width_crop):
            for h in range(height_crop):
                # 计算裁剪区域坐上右下的坐标
                left = w * size[0]
                upper = h * size[1]
                right = (w + 1) * size[0] if (w + 1) * size[0] <= width else width
                lower = (h + 1) * size[1] if (h + 1) * size[1] <= height else height

                # 坐标信息存入tuple中
                edge = (left, upper, right, lower)

                # 进行裁剪
                cropped_image = self.image.crop(edge)
                cropped_mask = self.mask.crop(edge)

                # 保存图像
                cropped_image.save(os.path.join(image_save_path, f"img_{cnt}.png"))
                cropped_mask.save(os.path.join(mask_save_path, f"mask_{cnt}.png"))
                cnt += 1

    @staticmethod
    def check_path(name, path):
        # 检测路径是否存在
        if not os.path.exists(path):
            # 引发错误
            raise FileNotFoundError("No such File" + path +
                                    f"\n\tThis may be \'{name}\' Error \n\t")

    def open(self):
        # 打开tif影像
        self.image = Image.open(cfg.image_path)
        self.mask = Image.open(cfg.mask_path)

        # 检查image与mask像素是否一致
        if self.image.size != self.mask.size:
            raise ValueError("Image Size not match Mask Size")


if __name__ == "__main__":
    cfg = Config()
    rs_data = rs_data_prossing(cfg)
    rs_data.crop()

