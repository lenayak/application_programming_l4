import os


class SimpleIterator:
    def __init__(self, filename: int) -> None:
        self.filename = filename
        self.counter = 0
        self.list = []
        file = open(self.filename, "r")
        for row in file:
            self.list.append(row)
        file.close()


    def __get_next__(self):
        return self

    def __next__(self):
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration


if __name__ == "__main__":
    mark = 4
    path = os.path.abspath("../application_programming_l1/dataset")
    path_to_folder = path + f"/{mark}"
    num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                        for f in os.listdir(path_to_folder)) + 1
    iter = SimpleIterator(num_of_files)
    iter = SimpleIterator(num_of_files, mark, path_to_folder)