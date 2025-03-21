### This code plots an interactive time series visualisation of temperature trends over Brazilian cities###
import pandas as pd
import os, sys
import plotly.express as px
import numpy as np

def read_file(path):
    """
    This function loads data from the csv files in the given path and returns them as a Pandas Dataframe object.
        The data in the Brazilian city temperature dataset is stored in multiple csv files.
        Each csv file contains data for a different city.
        We read each file and concatenate them into a single Pandas Dataframe object.
        We get the city name from the name of the file and add the city name as a column in the Dataframe.
        The name of the file is in the format: station_{city_name}.csv
    Args:
        path: the path to the data to be read
    Returns:
        data: a Dataframe object containing the loaded dataset
    """
    for i, name in enumerate(names for names in os.listdir(path)):
        city_name = name.split('_')[1].split('.')[0]
        city_data = pd.read_csv(os.path.join(path, name))
        city_data.insert(0, 'City', city_name)
        if i == 0:
            data = city_data
        else:
            data = pd.concat([data, city_data])
    return data

def check_missing(data):
    """
    This function checks the loaded data for missing values.
    Args:
        data: a Dataframe object containing the loaded dataset
    Returns:
        missing: the number of columns with missing values
    """
    missing = 0
    for key in data.keys():
        if data[key].isnull().any():
            print(f"Missing values found in column: {key}")
            missing += 1
    return missing

def load_data(path, attempts, to_replace=np.nan):
    """
    This function covers all the steps required to load and prepare the dataset for visualisation.
    Args:
        path: Path to the dataset
        attempts: Number of attempts to load the dataset before exiting code
        to_replace: Value that corresponds to error/incorrect values in the dataset, to be replaced by NaN
    Returns:
        df: a Dataframe object containing the loaded dataset
    """
    count = 0
    while count < attempts:
        df = read_file(path)
        missing = check_missing(df)
        if missing == 0:
            break
        else:
            count += 1
    # Check if the max no of attempts has been reached
    if count < attempts:
        print("The dataset has been loaded.")
    else:
        print(f"Error loading dataset. Max attempts reached. Exiting program.")
        sys.exit()
    # Check if any error/incorrect values need to be replaced with NaN
    if to_replace != np.nan:
        df.replace(to_replace, np.nan, inplace=True)

    return df

def time_series_plot(df):
    """
    This function plots the time series graph on the given data
    Args:
        df: a DataFrame object containing the loaded dataset
    Returns:
         No returns: creates a time series plot with a range slider
    """
    fig = px.line(df, x='YEAR', y='metANN', color='City', title='Average Temperature trends over Brazilian cities')
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    print("Plot has been created")
    return None

def main():
    path = "/__Enter the path to dataset__/"
    try:
        max_attempts = int(input("Enter the max no of attempts to load the dataset: "))
    except ValueError:
        print("The provided input is not an integer. Please enter an integer.")
    df = load_data(path, max_attempts, to_replace=999.90)
    time_series_plot(df)

if __name__ == "__main__":
    main()
