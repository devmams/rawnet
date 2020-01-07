import torch.nn as nn
import torch.nn.functional as F
import importlib
import torch
import torch.optim as optim
from modele_Data import RawNetData

class RawNet(nn.Module):
    def __init__(self):
        super(RawNet, self).__init__()
        self.criterion = nn.CrossEntropyLoss()

        self.lrelu = nn.LeakyReLU()
        self.lrelu_keras = nn.LeakyReLU(negative_slope=0.3)

        self.first_conv = nn.Conv1d(in_channels = 1,#3
			out_channels = 128,#128
			kernel_size = 3,#3
        )

        self.bn = nn.BatchNorm1d(num_features = 128)

    def forward(self, x):
        out = self.first_conv(x)
        out = self.bn(out)
        out = self.lrelu_keras(out)

        
        print("shape : ",out.shape)
        return out

def train(model, train_loader):
    for batch_idx, (data,target) in enumerate(train_loader):
        output = model(data)
        print("output : ", output)

if __name__ == '__main__':

    DIRECTORY = "/info/home/larcher/ATAL/2019/voxceleb1/dev/wav"
    print(DIRECTORY)
    print("-----")
    dataset = RawNetData(DIRECTORY)
    data_loader = torch.utils.data.DataLoader(dataset,batch_size=1,shuffle=True)
    print(data_loader)
    print("-----")
    model = RawNet()
    print(model)
    #print(dataset.shape)
    #print(data_loader.shape)
    #for batch_idx, (data, target) in enumerate(data_loader):
        #print("data")
  #      print("target")
        #break
    # rawnet.forward 
    train(model,data_loader)
