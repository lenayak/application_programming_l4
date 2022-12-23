import os
import re
from collections import Counter

from matplotlib import pyplot as pl
import pandas as pd
from pymystem3 import Mystem
import pymorphy2

from third import Review, get_dataset


def get_path_to_dataset() -> str:
    """Returns path to dataset"""
    path = os.path.abspath("../application_programming_l1/dataset")
    return path


def get_datafraime(path_to_dataset: str) -> pd.DataFrame:
    """generates a datafraime"""
    dataset = get_dataset(path_to_dataset)
    reviews = []
    marks = []
    for review in dataset:
        reviews.append(str(review.review))
        marks.append(str(review.mark))
    dataframe = pd.DataFrame({"mark": marks, "review": reviews})
    return dataframe


def check(dataframe: pd.DataFrame, name_col: str) -> bool:
    """check for emptiness"""
    return dataframe[name_col].isnull().values.any()


def info(dataframe: pd.DataFrame, name_col: str) -> pd.Series:
    """returns information about column"""
    return dataframe[name_col].describe()    


def count_of_words(datafraime: pd.DataFrame, col: str) -> list:
    """counts words in reviews"""
    count_words = []
    for i in range(0, len(datafraime.index)):
        text = datafraime.iloc[i]
        text = text[col]
        words = text.split()
        count_words.append(len(words))