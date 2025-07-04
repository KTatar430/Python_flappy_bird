# This file contains the multi-layer perceptron (MLP) model for the Flappy Bird clone.

import torch
import torch.nn as nn
import torch.nn.functional as F

class FlappyBird_MLP(nn.Module):
    def __init__(self, device):
        super(FlappyBird_MLP, self).__init__()
        self.fc1 = nn.Linear(5, 16)   # 5 inputs
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 1)   # 1 output (flap or not flap)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x)) 
        return x