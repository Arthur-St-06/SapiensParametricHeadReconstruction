import numpy as np

file_path = '/home/arthur/ParametricHeadReconstruction/dataset/direct_neutral_landmarks/numpy/IMG_0045_kpt3d.npy'

print(np.load(file_path))
print(np.load(file_path).shape)