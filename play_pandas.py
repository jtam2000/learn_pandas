import numpy as np
import pandas as pd


def get_some_random_number_multi_dimension(*argv, **kwargs):
    rand = np.random.rand(*argv, **kwargs)
    print(rand)


def get_some_random_numbers(how_many):
    random_num = np.random.rand(how_many)
    return random_num


def create_panda_series(nums, index):

    rn = get_some_random_numbers(nums)
    sr = pd.Series(data=rn, name="Ten Random Numbers", index=index)
    return sr


def show_pandas_series_metadata():

    sr = create_panda_series(nums=10, index="a b c d e f g h i j".split())
    print(sr)


show_pandas_series_metadata()
get_some_random_number_multi_dimension(3, 4, 5, 2)
get_some_random_number_multi_dimension(2, 3)