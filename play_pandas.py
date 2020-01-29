import numpy as np
import pandas as pd
import os.path as path


def get_some_random_number_multi_dimension(*argv, **kwargs):
    rand = np.random.rand(*argv, **kwargs)
    return rand


def get_some_random_numbers(how_many):
    random_num = np.random.rand(how_many)
    return random_num


def create_panda_series_with_index(nums, index):
    rn = get_some_random_numbers(nums)
    sr = pd.Series(data=rn, name="Ten Random Numbers", index=index)
    return sr


def show_pandas_series_metadata():
    sr = create_panda_series_with_index(nums=10, index="a b c d e f g h i j".split())
    print(sr)
    return sr


def get_csv_from_website(url, number_of_rows_to_get: int):
    """

    :param number_of_rows_to_get: how many rows to return from the website
    :param url: https link
    :return: dataframe from data that lives in teh https link

    Note: in order from reading of data from url to work, you have to
        install ssl script: "Install Certificates.command"
        under the Python installed root directory.
        The Python install process does not seem to run this as a default
    """
    data_file = "./artwork_data.csv"

    if not path.exists(data_file):
        return pd.read_csv(url, nrows=number_of_rows_to_get)
    else:
        return pd.read_csv(data_file, nrows=number_of_rows_to_get)


def get_tate_data(
        url='https://raw.githubusercontent.com/tategallery/collection/master/artwork_data.csv') -> pd.DataFrame:
    """
    Assumes the tate like is in the default param to this function

    :return: data from the tate dataset as a Pandas.DataFrame
    """
    columns_of_interest = ['id', 'artist', 'title', 'medium',
                           'year', 'acquisitionYear', 'height', 'width', 'units']

    local_data_file = "./artwork_data.csv"

    if not path.exists(local_data_file):
        source_location = local_data_file
    else:
        source_location = url

    dframe = pd.read_csv(source_location,
                         usecols=columns_of_interest,
                         index_col='id')
    return dframe


def save_data_to_pickle(dframe: pd.DataFrame, save_file: str = "save_data.pickle"):
    dframe.to_pickle("save_file")


def get_distinct_list_of_artists(dframe: pd.DataFrame):
    """
        LEARNING Point: DataFrame has a unique() function return distinct elements in a column

    :param dframe: data from which to get the artist column
    :return:
    """
    distinct_list = sorted(dframe["artist"].unique())  # LEARNING POINT: "unique" function in dataframe
    distinct_list = [(artist[0], artist) for artist in distinct_list]
    return len(distinct_list), distinct_list


def get_filtering_particular_artist(dframe: pd.DataFrame,
                                    artist_name: str = 'Bacon, Francis') -> int:
    """
        LEARNING POINT: Filtering for a particular artist
    :param dframe:
    :param artist_name:
    :return:
    """

    # LEARNING: returns a series of True or False for each row, indicating
    # which row has artist == artist_name
    truth_table = (dframe['artist'] == artist_name)  # LEARNING: df["column"]== FilterValue

    # LEARNING: series has a value_counts() function
    # counts unique values in a series and return the number of times it appears in teh
    # series, like count(*) group by the column
    truth_table_count_true_or_false = truth_table.value_counts()  # LEARNING: value_counts()

    return truth_table_count_true_or_false[True]


def get_count_of_work_by_each_artist(dframe: pd.DataFrame) -> pd.DataFrame:
    """
        GET count of work for each artist, using the value_counts() for the entire column
        This is like ding a group by in SQL for that column and doing a select count(*)
    :param dframe: 
    :return: 
    """
    df = pd.DataFrame(data=dframe['artist'].value_counts())
    df = df.rename_axis("artist")
    print("get count:", df)
    return df


# get the data
df_local = get_tate_data()
print(df_local.columns)

# save the data as pickle (binary)
save_data_to_pickle(df_local)

# get unique artists
artist_count, distinct_artists = get_distinct_list_of_artists(df_local)

[print(artist) for artist in distinct_artists]
print("distinct artist count:", artist_count)

# Filter for one artist
artist = 'Bacon, Francis'
count = get_filtering_particular_artist(df_local, artist)
print("# of works by", artist, "is:", count)

# Count # of work by each artist
count_summary_df = get_count_of_work_by_each_artist(df_local)

count_summary_df.rename = count_summary_df.rename(columns={"artist": "Artifact_Count"})
print("\ncolumns:", count_summary_df.columns)

print(count_summary_df)
# [print(count_item["index"]) for count_item in count_summary_df]
count_summary_df.plot()
