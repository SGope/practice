### This code plots an interactive time series visualisation of temperature trends over Brazilian cities###
import pandas as pd
import os, sys
import plotly.express as px
import numpy as np

def main():
    path = "/home/sayantan-gope/PycharmProjects/practice/weather_visualisation/archive/"
    for i, name in enumerate(names for names in os.listdir(path)):
        city_name = name.split('_')[1].split('.')[0]
        city_data = pd.read_csv(os.path.join(path, name))
        city_data.insert(0, 'City', city_name)
        if i == 0:
            df = city_data
        else:
            df = pd.concat([df, city_data])

    missing = 0
    for key in df.keys():
        if df[key].isnull().any():
            print(f"Missing values found in column: {key}")
            missing += 1
    if missing != 0:
        print(f"Error loading dataset. Missing values found in {missing} columns. Exiting program.")
        sys.exit()

    df.replace(999.90, np.nan, inplace=True)
    fig = px.line(df, x='YEAR', y='metANN', color='City', title='Average Temperature trends over Brazilian cities')
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()

if __name__ == "__main__":
    main()