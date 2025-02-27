_base_ = "./hyper_default.py"

expname = "vrig/base-chicken_2"
basedir = "./logs/vrig_data"

model_and_render = dict(
    occ_grid_reso=128,
    occ_ema_decay=0.99,
    occ_thre=0.05,
)
data = dict(
    datadir="data/hypernerf/vrig-chicken",
    dataset_type="hyper_dataset",
    white_bkgd=False,
)
