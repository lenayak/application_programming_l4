import os
import csv
import shutil


def make_new_dataset() -> None:
    '''Create folder with name:"new_dataset"'''
    os.mkdir("new_dataset")


def copy_dataset(path: str) -> str:
    '''Copies dataset into the new direct'''
    make_new_dataset()
    new_dataset_path = os.path.abspath("../application_programming_l2/new_dataset")
    for num_of_folder in range(1,6):
        path_to_folder = os.path.join(path, str(num_of_folder))
        num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                           for f in os.listdir(path_to_folder)) + 1
        for i in range(0, (num_of_files -1)):
            shutil.copy(path_to_folder + f"/{(i+1):04}.txt",new_dataset_path)
            os.rename(f"./new_dataset/{(i+1):04}.txt", f"./new_dataset/{num_of_folder}_{(i+1):04}.txt")
    return new_dataset_path



def write_as_csv(path: str, path_to_files: str) -> None:
    '''Writes path to files in CSV file'''
    with open("annotation1.csv", mode="w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Absolute path", "Relative path", "Class"])
        for p in path_to_files:
            p = p[0:2] + "_" + p[3:]
            writer.writerow([f"{path + p}",
                             f"dataset{p}", f"{p[1]}"])


def get_path_to_files(path: str) -> str:
    '''Get path to files from dataset'''
    path_to_files = []
    for num_of_folder in range(1,6):
        path_to_folder = os.path.join(path, str(num_of_folder))
        num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                           for f in os.listdir(path_to_folder)) + 1
        for i in range(1, num_of_files):
            path_to_file = os.path.join(path_to_folder, f"{(i):04}.txt")
            print(f"{num_of_folder}:{(i):04}")
            path_to_files.append(path_to_file[len(path):])
    return path_to_files


if __name__ == "__main__":
    path = os.path.abspath("../application_programming_l1/dataset")
    path_to_files = get_path_to_files(path)
    new_dataset_path = copy_dataset(path)
    write_as_csv(new_dataset_path, path_to_files)