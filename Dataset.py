import os
import pandas as pd


def download():
    if os.path.exists("games.csv"):
        os.remove("games.csv")

    if os.path.exists("games.json"):
        os.remove("games.json")

    os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

    from kaggle import KaggleApi

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('fronkongames/steam-games-dataset', path='.', unzip=True)

    if os.path.exists("games.json"):
        os.remove("games.json")
        print("downloaded")


def remove_columns():
    # Load the Excel file
    df = pd.read_csv('games.csv')

    # List of columns you want to remove
    columns_to_remove = ['Header image', 'Website', "Metacritic url", "About the game", "Header image",
                         "Reviews", "AppID", "Metacritic url", "Screenshots", "Movies", "Support url",
                         "Support email", "Notes", "Score rank"]

    # Remove the specified columns
    df.drop(columns=columns_to_remove, inplace=True)

    df.to_csv("games.csv", index=False)
    print("removed columns successfully")


download()
remove_columns()
