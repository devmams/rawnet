
import torch
from torch.utils.data.dataset import Dataset
import numpy as np
from wave import Wave_write
import torchaudio
import os
from torch.utils import data



## permet de transformer la durée de l'audio de soorte à avoir 3,59 seconde
def transform_audio(x):
    nb_time = 59049
    my_time =np.asarray(x[:, 1:] - 0.97 * x[:, :-1], dtype=np.float32).shape[1]
    if nb_time > my_time:
        start_idx = np.random.randint(low=0,
                                      high=nb_time - my_time)
        x = x[:, start_idx:start_idx + my_time]
    elif nb_time < my_time:
        nb_dup = int(my_time / nb_time) + 1
        x = np.tile(x, (1, nb_dup))[:, :my_time]
    else:
        x = x

    return x

def getFirst(directory):
    import os
    for _, d, _ in os.walk(directory):
        return d

def loadAudioFromDirectory(path):
    # get all wave files in the directory
    files = []
    for r, _, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
        return files


# cette fonction permet de recuperer tous les fichiers audio d'un dossier wav et les classe par ID
# retourne une liste de liste, pour chaque element de la liste , le premier element correspond à l'id et le second correspond au chemin d'accès du fichier wave
def getAllWaveFileByWaveDirectory(directory):
    listeWavefiles = []
    listeIdAuteur = []
    listeIdAuteur = getFirst(directory);
    for idAuteur in listeIdAuteur:
        waveFolderByIdAuteur =getFirst(directory+"/"+idAuteur)
        for elt in waveFolderByIdAuteur:
            for file in  loadAudioFromDirectory(directory+"/"+idAuteur+"/"+elt):
                listeWavefiles.append([idAuteur, file])
    return listeWavefiles


class RawNetData(Dataset):

    def __init__(self,  directory):

        # data, une liste contenant pour chaque elemment, l'auteur(son id ) et l'audio (chemin d'accès)
        self.data = getAllWaveFileByWaveDirectory(directory)



    def __len__(self):
        # renvoie le nom d'element dans la liste wave
        return len(self.data )

    def __getitem__(self, idx):
        X , _ =torchaudio.load(self.data[idx][1])
        data= transform_audio(X)
        target = self.data[idx][0]

        return data, target



class RawNetDataLoder( ):
    def __init__(self,  directory):
        dataSet = RawNetData(directory)
        data_loader = torch.utils.data.DataLoader(dataSet,
                                                  batch_size=16,
                                                  shuffle=True,
                                                  num_workers=0
                                                  )
        print(type (data_loader))






