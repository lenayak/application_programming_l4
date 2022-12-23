import os 
import pathlib
import csv
from random import Random, random


class Review:
    def __init__(self):
        self.name = None
        self.review = None
        self.mark = None


def create_folder() -> None:
    '''Create folder for copy dataset'''
    os.mkdir("copy_dataset")
    for i in range(1,6):
        os.mkdir("copy_dataset/" + str(i))


def save_reviews(data: Review, filename: str) -> None:
    '''Save reviews into copy dataset'''      
    for i in range(1,len(data)):
        numbers = [0]
        random = Random()
        number = 0
        while number in numbers:
            number = random.randint(1, 10000)
        file = open(filename + f'/{number:04}' + '.txt', mode="w", encoding="utf-8")
        file.write(data[i].name)
        file.write('\n\n\n')
        file.write(data[i].review)
        file.close
        numbers.append(number)


def get_dataset(path: str) -> str:
    '''Read all files in dataset and returns it as Review class objects'''                     
    dataset = list()
    for num_of_folder in range(1,6):
        path_to_folder = os.path.join(path, str(num_of_folder))
        num_of_files = sum(os.path.isfile(os.path.join(path_to_folder, f))
                           for f in os.listdir(path_to_folder)) + 1
        for i in range(1,num_of_files):
            path_to_file = os.path.join(path_to_folder, f"{(i):04}.txt")
            file = open(path_to_file, mode="r", encoding="utf-8")
            print(f"{num_of_folder}:{(i):04}")
            review = Review()
            review_text = ""
            line_counter = 0
            while True:
                line = file.readline()
                if not line:
                    try:
                        file.close()
                    except Exception as e:
                        print(e.args)
                    break
                if line_counter == 0:
                    review.name = line
                else:
                    review_text += line
                line_counter += 1
                review_text = review_text.replace(u'\xa0', u' ')
                review.mark = float(num_of_folder)
                review.review = review_text.strip()
            dataset.append(review)
    return dataset


def create_copy(path: str) -> None:
    dataset = get_dataset(path)
    create_folder()
    write_dataset(dataset)      


def write_dataset(dataset: Review) -> None:
    '''Writes dataset'''     
    one_data = [el for el in dataset if el.mark < 1.5]
    save_reviews(one_data, "copy_dataset/1")
    two_data = [el for el in dataset if (el.mark >= 1.5) and (el.mark < 2.5)]
    save_reviews(two_data, "copy_dataset/2")
    three_data = [el for el in dataset if (el.mark >= 2.5) and (el.mark < 3.5)]
    save_reviews(three_data, "copy_dataset/3")
    four_data = [el for el in dataset if (el.mark >= 3.5) and (el.mark < 4.5)]
    save_reviews(four_data, "copy_dataset/4")
    five_data = [el for el in dataset if (el.mark >= 4.5) and (el.mark <= 5.0)]
    save_reviews(five_data, "copy_dataset/5")


def get_path_to_files(path: str) -> str:
    '''Get path to files from dataset'''     
    path_to_files = []
    for num_of_folder in range(1,6):
        path_to_folder = os.path.join(path, str(num_of_folder))
        directory = pathlib.Path(path_to_folder)
        for file in directory.iterdir():
            print(file)
            path_to_files.append(file)
    return path_to_files


def write_as_csv(path: str, path_to_files: str) -> None:
    '''Writes path to files in CSV file'''    
    with open("annotation2.csv", mode="w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Absolute path", "Relative path", "Class"])
        for i in range(0, len(path_to_files)):
            path_to_files[i] = str(path_to_files[i])
            writer.writerow([f'{path_to_files[i]}', 
                             os.path.relpath(path_to_files[i],start=os.path.join("Рабочий стол", "application_programming", "application_programming_l2")), os.path.basename(path_to_files[i])])


if __name__ == "__main__":
    path = os.path.abspath("../application_programming_l1/dataset")
    create_copy(path)
    copy_dataset_path = os.path.abspath("../application_programming_l2/copy_dataset")
    path_to_files1 = get_path_to_files(copy_dataset_path)
    write_as_csv(copy_dataset_path, path_to_files1)