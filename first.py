import os
import csv

def write_as_csv(path: str, path_to_files: str) -> None:
    '''Writes path to files in CSV file'''
    with open("annotation.csv", mode="w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Absolute path", "Relative path", "Class"])
        for i in range(0,len(path_to_files)):
            writer.writerow([f'{path + path_to_files[i]}',
                             f'dataset{path_to_files[i]}', f'{path_to_files[i][1]}'])


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
    write_as_csv(path, path_to_files)