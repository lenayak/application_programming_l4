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
    return count_words


def cleanwords(words: str) -> str:
    """returns a list of pure words"""
    words_result = list()
    for i in range(0, len(words)):
        words[i] = words[i].strip()
        words[i] = words[i].lower()
        if words[i] != " ":
            words_result.append(re.sub("[^абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ \n]", "", words[i]))
    return words_result


def pos(word, morth=pymorphy2.MorphAnalyzer()):
    "return a likely part of speech for the *word*."""
    return morth.parse(word)[0].tag.POS


def Lemmatize(datafraime: pd.DataFrame, column: str):
    """lem"""
    text_nomalized = str()
    for i in range(0, len(datafraime.index)):
        text = datafraime.iloc[i]
        text = text[column]
        words = text.split()
        words = cleanwords(words)
        for i in range(0,len(words)):
            text_nomalized += words[i]
            text_nomalized += ' '
    m = Mystem()
    lemmas = m.lemmatize(text_nomalized)
    functors_pos = {'ADJF'}  
    lemmas = [lemma for lemma in lemmas if pos(lemma) in functors_pos]
    print(lemmas)
    lemmas = cleanwords(lemmas)     
    return lemmas
    
    
def LemmalizeClass(datafraime: pd.DataFrame, column: str, mark:str) -> str:
    lemmas = Lemmatize(datafraime, column)
    word_dict = Counter(lemmas)
    word_dict = dict(word_dict) 
    result = dict()
    for key, value in word_dict.items():    
        if value > 500:
            result[key] = value
    return result


def Top10Lemmas(lemmatized: str) -> str:
    pass


if __name__ == '__main__':
    print("-"*99)
    columns = ["mark", "review", "num_of_words"]
    dataset_path = get_path_to_dataset()
    dataframe = get_datafraime(dataset_path)
    dataframe.to_csv(r"dataframe.csv", index=False)
    num_of_words = count_of_words(dataframe, "review")
    dataframe[columns[2]] = pd.Series(num_of_words)
    dataframe[columns[2]] = pd.Series(num_of_words)
    print(dataframe)
    stat = dataframe[columns[2]].describe()
    print(stat)
    df_words_filtered = pd.DataFrame(dataframe[dataframe[columns[2]] <= 100])
    print(df_words_filtered)
    df_1 = pd.DataFrame(dataframe[dataframe[columns[0]] == '1'])
    print(df_1)
    stat_1 = df_1[columns[2]].describe()
    print('\nДля оценки 1:\n')
    print('Минимальное кол-во слов:', stat_1['min'])
    print('Максимальное кол-во слов:', stat_1['max'])
    print('Среднее кол-во слов:', stat_1['mean'])
    lemmatized_class = LemmalizeClass(dataframe, columns[1], '1')
    fig = pl.figure(figsize=(20,10))
    ax = fig.add_subplot()
    ax.bar(list(lemmatized_class.keys()), lemmatized_class.values(), color='g')
    pl.show()
    print("-"*99)