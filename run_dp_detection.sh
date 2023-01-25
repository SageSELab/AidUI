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
# python -c "import evaluation.evaluation as evaluation; evaluation.test_confusion_matrix()"
#---------------------test---------------------------------

# create ./input directory
mkdir ./input/

# input to turn on evaluation mode
EVAL_MODE="off"
echo "turn on evaluation mode? answer with y/n"
read answer
echo "answer: $answer"

if [[ $answer = "y" ]]
then
  EVAL_MODE="on"
fi

if [[ $EVAL_MODE = "on" ]]
then
  echo "EVAL MODE is ON"
  # copy evaluation datast UIs to ./input folder and create the groud truth info for each UI
  python -c "import evaluation.evaluation as evaluation; evaluation.set_evaluation_data()"
  echo "--------------------------------------input UIs copied to input folder--------------------------------------"
  sleep 10s

  echo "--------------------------------------create object detection and UIED directories--------------------------------------"
  mkdir ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_data/
  mkdir ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_data/test
  mkdir ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_output/
  mkdir ./UIED/data/input/

  echo "--------------------------------------conda initiate--------------------------------------"
  eval "$(conda shell.bash hook)"

  echo "---------------activate object detection env (dl_dp_obj_det_env), copy input files & conduct object detection inference---------------"
  conda activate dl_dp_obj_det_env
  cp ./input/*.* ./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_data/test
  cd ./object_detection/object_detection_frcnn_mscoco_boilerplate
  jupyter nbconvert --to notebook --execute object_detection_frcnn_mscoco_inference.ipynb
  echo "waiting 10s"
  sleep 10s
  cd ../..

  echo "---------------activate UIED env (dp_uied3), iteratively copy input files & conduct text extraction---------------"
  conda activate dp_uied3
  mkdir ./tmp_input/
  destdir="./tmp_input/"
  cp ./input/*.* $destdir
  cd $destdir
  counter=1
  while [ $counter -le 34 ]
    do
      echo $counter
      find . -maxdepth 1 -type f |head -15|xargs cp -t "../UIED/data/input"
      find . -maxdepth 1 -type f |head -15|xargs rm
      sleep 2s
      cd ../UIED/
      python run_uied.py
      echo "waiting 10s"
      sleep 10s
      rm ./data/input/*
      cd ..
      cd $destdir
      ((counter++))
    done
  cd ..
  rmdir $destdir
  cp ./input/*.* ./UIED/data/input

  echo "--------------------------------------execute DP detection & evaluation--------------------------------------"
  eval "$(conda shell.bash hook)"
  conda activate dl_dp_obj_det_env
  python main.py
else
  echo "EVAL MODE is OFF"
  echo "--------------------------------------execute DP detection & evaluation--------------------------------------"
  eval "$(conda shell.bash hook)"
  conda activate dl_dp_obj_det_env
  python main.py
fi
