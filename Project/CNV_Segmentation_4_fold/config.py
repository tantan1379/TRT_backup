'''
@File    :   config.py
@Time    :   2021/08/12 10:28:03
@Author  :   Tan Wenhao 
@Version :   1.0
@Contact :   tanritian1@163.com
@License :   (C)Copyright 2021-Now, MIPAV Lab (mipav.net), Soochow University. All rights reserved.
'''
import os

class cnv_single_config(object):
    k_fold = 4
    num_epochs = 60
    epoch_start_i = 0
    checkpoint_step = 4
    crop_height = 360
    crop_width = 360
    batch_size = 2                  # *
    make_file = False               
    # SGD优化器相关
    lr = 0.001                       # 学习率 *
    lr_mode = 'poly'                # poly优化策略
    momentum = 0.9                  # 优化器动量
    weight_decay = 1e-4             # L2正则化系数
    # 训练相关
    net_work = 'pspnet'               # 可选网络 * backbone/unet/cpfnet//unet_spp_se/pspnet/deeplabv3plus
    num_workers = 0                 # dataloader设置
    num_classes = 1                 # 分割类别数 类别数+加背景 *
    cuda = '0'                      # GPU id选择 *
    pretrained = True
    use_gpu = True
    # 路径相关
    data = r'F:\Dataset\ZSQ'    # 数据存放的根目录 *
    dataset = 'ZSQ_all_png_4_fold'      # 数据库名字(需修改成自己的数据名字) *
    log_dirs = './results/save/'          # 存放tensorboard log的文件夹() *
    save_model_path = './logs/'+net_work  # 保存模型的文件夹
    result_path = './results/img_seg/'+net_work  # 保存分割图像的文件夹
