import os
import numpy as np

folder_path = '/home/arthur/ParametricHeadReconstruction/dataset/direct_neutral_landmarks/txt'
output_folder = '/home/arthur/ParametricHeadReconstruction/dataset/direct_neutral_landmarks/numpy'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    keypoints = np.loadtxt(file_path)

    keypoints = keypoints[68-51:, :3]

    output_path = os.path.join(output_folder, filename[:-4])
    np.save(output_path, keypoints)

    print(f"Processed and saved: {output_path}")
        
