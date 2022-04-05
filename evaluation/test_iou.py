import torch
import torchvision.ops.boxes as bops

box1 = torch.tensor([[511, 41, 577, 76]], dtype=torch.float)
box2 = torch.tensor([[544, 59, 610, 94]], dtype=torch.float)
iou = bops.box_iou(box1, box2)
print(float(iou))
