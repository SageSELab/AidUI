#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# install pytorch
# !pip install --pre torch torchvision torchaudio -f https://download.pytorch.org/whl/nightly/cu102/torch_nightly.html -U


# In[4]:


# test torch version and CUDA device
import torch
print(torch.__version__)


# In[5]:


# mount google drive
# from google.colab import drive
# drive.mount("/content/gdrive")


# In[113]:


# # change to project home directory
# import os
# os.chdir("/content/gdrive/My Drive/object_detection_frcnn_mscoco_boilerplate")


# In[7]:


import os
import numpy as np
import torch
import torch.nn as nn
import torchvision
from torchvision import datasets, transforms, models
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor


# In[8]:


import utils


# In[14]:


import pprint
pp = pprint.PrettyPrinter()
import json


# In[15]:


# path to data and annotation
data_dir = 'inference_data'


# In[17]:


test_transforms = transforms.Compose([transforms.Resize(224),
                                      transforms.ToTensor(),
                                      #transforms.Normalize([0.485, 0.456, 0.406],
                                      #                     [0.229, 0.224, 0.225])
                                     ])
dataset_test = datasets.ImageFolder(data_dir, transform=test_transforms)


# In[18]:


data_loader_test = torch.utils.data.DataLoader(
    dataset_test, batch_size=1, shuffle=False, num_workers=1,
    collate_fn=utils.collate_fn)


# In[19]:


# select device (whether GPU or CPU)
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")


# In[20]:


num_classes = 6


# In[21]:


model = torchvision.models.detection.fasterrcnn_resnet50_fpn()
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
# model.load_state_dict(torch.load('trained-visual-cue-detection-model.pth'))
model.load_state_dict(torch.load('trained-visual-cue-detection-model.pth', map_location=device))


# In[22]:


model.eval()


# In[23]:


print("================= INFERENCE ===========================")
with torch.no_grad():
    correct = 0
    total = 0
    inference_result = {}
    # for images, labels in data_loader_test:
    for i, (images, labels) in enumerate(data_loader_test, 0):
        # print("================== batch ==================")
        sample_fname, _ = data_loader_test.dataset.samples[i]
        filename = sample_fname.split("/")[2]
        print("filename: ", filename)
        outputs = model(images)
        # print("outputs")
        # pp.pprint(outputs)

        # init boxes, labels, scores
        boxes = None
        labels = None
        scores = None

        # get boxes, labels, scores
        if len(outputs[0]["boxes"]) != 0:
          boxes = outputs[0]["boxes"][0].numpy().tolist()
        if len(outputs[0]["labels"]) != 0:
          labels = outputs[0]["labels"][0].numpy().tolist()
        if len(outputs[0]["scores"]) != 0:
          scores = outputs[0]["scores"][0].numpy().tolist()

        # populate JSON
        inference_result["boxes"] = boxes
        inference_result["labels"] = labels
        inference_result["scores"] = scores

        # print("inference result")
        # pp.pprint(inference_result)

        # write inference result
        inference_output_dir = "./inference_output/"
        inference_output_filename = inference_output_dir + filename.split(".")[0] + ".json"
        with open(inference_output_filename, "w") as fp:
          json.dump(inference_result, fp)
        fp.close()
        # break


# In[ ]:


# # write inference result
# with open('./inference_result.json', 'w') as fp:
#   json.dump(inference_result, fp)
