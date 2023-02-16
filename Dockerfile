FROM continuumio/miniconda3

RUN apt-get update && apt-get install libgl1 -y

## Use these enviornment files found in this repo
ADD dl_dp_obj_det_env /opt/conda/envs/dl_dp_obj_det_env

## Use these enviornment files found in this repo
ADD dp_uied3 /opt/conda/envs/dp_uied3

ADD AidUI /AidUI

## This can be found at https://pytorch.org/hub/nvidia_deeplearningexamples_resnet50/
COPY resnet50-0676ba61.pth /root/.cache/torch/hub/checkpoints/

## Can be found at https://drive.google.com/file/d/1Gzpi-V_Sj7SSFQMNzy6bcgkEwaZBhGWS/view
COPY cnn-rico-1.h5 /root/.cache/torch/hub/checkpoints/


