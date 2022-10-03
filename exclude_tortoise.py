import os
import shutil
from distutils.dir_util import copy_tree

IMAGE_DIRECTORY = 'C:/Users/robir/OneDrive/Documents/GitHub/csci-e-599/siamese-animal-tracking/data/filter_aug'


def exclude_tortoise(file_path: str, folder_num: int) -> str:
    train_src, test_src = file_path+"/train", file_path+"/test"
    train_dst = file_path + f"/tortoises_except_{folder_num}/train"
    test_dst = file_path + f"/tortoises_except_{folder_num}/test"
    copy_tree(train_src, train_dst)
    copy_tree(test_src, test_dst)
    train_folder_paths = [f.path for f in os.scandir(train_dst) if f.is_dir()]
    train_folder_paths.sort()
    test_folder_paths = [f.path for f in os.scandir(test_dst) if f.is_dir()]
    test_folder_paths.sort()

    # delete ith subdirectory in new_dir/train and new_dir/test
    shutil.rmtree(train_folder_paths[folder_num])
    shutil.rmtree(test_folder_paths[folder_num])

    return file_path + f"/tortoises_except_{folder_num}"


if __name__ == "__main__":
    exclude_tortoise(file_path=IMAGE_DIRECTORY, folder_num=0)
    # exclude_tortoise(file_path=IMAGE_DIRECTORY, folder_num=1)
    # exclude_tortoise(file_path=IMAGE_DIRECTORY, folder_num=2)
