FROM continuumio/miniconda3

RUN apt-get update && apt-get install libgl1 -y

ADD dl_dp_obj_det_env /opt/conda/envs/dl_dp_obj_det_env

ADD dp_uied3 /opt/conda/envs/dp_uied3

ADD AidUI /AidUI

COPY resnet50-0676ba61.pth /root/.cache/torch/hub/checkpoints/

COPY cnn-rico-1.h5 /root/.cache/torch/hub/checkpoints/


