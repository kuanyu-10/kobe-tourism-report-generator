import pandas as pd


def load_tourism_data(file_path):

    df = pd.read_excel(file_path)

    df = df.drop_duplicates()

    df = df.reset_index(drop=True)

    return df