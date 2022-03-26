#!/bin/bash

# -------------------sample commands-----------------------
# echo "What is your name?"
# read PERSON
# echo "Hello, $PERSON"

# source ~/anaconda3/etc/profile.d/conda.sh
# conda activate my_env
# jupyter nbconvert --to notebook --execute mynotebook.ipynb

# https://stackoverflow.com/questions/2119702/calling-a-python-function-from-bash-script
# -------------------sample commands-----------------------

#---------------------test---------------------------------
python -c "import evaluation.evaluation as evaluation; evaluation.test_confusion_matrix()"
#---------------------test---------------------------------

# # input to turn on evaluation mode
# EVAL_MODE="off"
# echo "turn on evaluation mode? answer with y/n"
# read answer
# echo "answer: $answer"
#
# if [[ $answer = "y" ]]
# then
#   EVAL_MODE="on"
# fi
#
# # copy evaluation datast UIs to ./input folder
# # create the groud truth info for each UI
# if [[ $EVAL_MODE = "on" ]]
# then
#   echo "EVAL MODE is ON"
#   python -c "import evaluation.evaluation as evaluation; evaluation.set_evaluation_data()"
#   echo "--------------------------------------input UIs copied to input folder----------------------------------------------------------------"
# else
#   echo "EVAL MODE is OFF"
# fi
#
# sleep 10s
#
# # create object detection directories
# mkdir ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_data/
# mkdir ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_data/test
# mkdir ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_output/
# # create UIED directories
# mkdir ./UIED/data/input/
#
# # copy input files to object detection module
# cp ./input/*.* ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_data/test
# echo "--------------------------------------input UIs copied to object detection module----------------------------------------------------------------"
#
# # copy input files to UIED module
# cp ./input/*.* ./UIED/data/input
# echo "--------------------------------------input UIs copied to UIED module----------------------------------------------------------------------------"
#
# # activate UIED env (dp_uied3) & execute text content area extraction
# eval "$(conda shell.bash hook)"
# conda activate dp_uied3
# echo "--------------------------------------conda environment dp_uied3 activated-----------------------------------------------------------------------"
# cd ./UIED/
# echo "--------------------------------------executing text content area extraction---------------------------------------------------------------------"
# python run_uied.py
# echo "waiting 10s"
# sleep 10s
#
# # activate object detection env (dl_dp_obj_det_env) & execute object detection inference
# conda activate dl_dp_obj_det_env
# echo "--------------------------------------conda environment dl_dp_obj_det_env activated--------------------------------------------------------------"
# cd ..
# cd ./object_detection/object_detection_frcnn_mscoco_boilerplate
# echo "--------------------------------------executing object detection inference-----------------------------------------------------------------------"
# jupyter nbconvert --to notebook --execute object_detection_frcnn_mscoco_inference.ipynb
# echo "waiting 10s"
# sleep 10s
#
# # execute DP detection
# echo "--------------------------------------executing DP detection-------------------------------------------------------------------------------------"
# cd ../..
# python main.py
