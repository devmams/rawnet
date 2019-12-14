import torch.nn as nn
import torch.nn.functional as F
import importlib
import torch
import torch.optim as optim
from modele_RawNet import RawNetData

class RawNet(nn.Module):
    def __init__(self):
        super(RawNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        #conv1D(3,3,128)
        self.first_conv = nn.Conv1d(in_channels = 3,#3
			out_channels = 128,#128
			kernel_size = 3,#3
        )

    def forward(self, x):
        x = self.first_conv(x)

        print("x : ", self.first_conv)
        print("x.shape : ", x.shape)
        print("x : ", x)

        return x


if __name__ == '__main__':

    DIRECTORY = "/info/home/larcher/ATAL/2019/voxceleb1/dev/wav"
    print(DIRECTORY)
    # dataSet = RawNetData(DIRECTORY)
    # data_loader = torch.utils.data.DataLoader(dataSet,batch_size=1,shuffle=True)


    # rawnet = RawNet()
    # print(rawnet)
    # for batch_idx, (data, target) in enumerate(test_loader):

    # rawnet.forward
    
