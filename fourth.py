import os


def get_next_exemplar(mark: int, id: int) -> str:
    '''Returns name of next file'''
    return  os.path.abspath("..\\application_programming_l1\\dataset" + f"\\{mark}" + f"\\{id:04}.txt")


if __name__ == "__main__":
    path = os.path.abspath("../application_programming_l1/dataset")
    mark = 4
    path_to_folder = path + f'/{mark}'
    num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                        for f in os.listdir(path_to_folder)) + 1
    for id in range(1,num_of_files):
        print(get_next_exemplar(mark, id))