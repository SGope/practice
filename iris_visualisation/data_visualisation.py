### This code is a practice project for some basic data visualisation tasks using the Iris dataset ###
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

def scatter_plot(data):
    """
    This function creates a scatter plot of the Iris dataset for petal length vs petal width
    Args:
        data: a Dataframe object containing the Iris dataset
    Returns:
        No returns: Creates a scatter plot
    """
    plt.scatter(data['petal length (cm)'], data['petal width (cm)'])
    plt.xlabel('Petal length (in cm)')
    plt.ylabel('Petal width (in cm)')
    plt.title('Scatter plot of Petal length vs Petal width')
    plt.show()
    return None

def histogram(data):
    """
    This function creates a histogram on various features in the Iris dataset
    Args:
        data: a Dataframe object containing the Iris dataset
    Returns:
        No returns: Creates a histogram
    """
    fig, axes = plt.subplots(nrows=2, ncols=2, tight_layout = True)
    for i, ax in enumerate(axes.flat):
        ax.hist(data[[data.columns[i]]], label = data.columns[i])
        ax.set_xlabel(data.columns[i])
    fig.suptitle('Histogram of different features in Iris dataset')
    plt.show()
    return None

def main():
    # Loading the Iris dataset from scikit-learn library
    iris = load_iris(as_frame=True)
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    
    # Checking for missing values in the dataset
    missing = 0                                                 # Flag to check for missing values
    for key in df.keys():
        if df[key].isnull().any():
            print(f"Missing values found in column {key}")
            missing += 1
    # Asking the user if the dataset should be redownloaded in case of missing values
    if missing == 0:
        print("No missing values were found")
    else:
        user_input = input(print("Would you like to redownload the dataset? (enter y/n)"))
        if user_input == 'y' or user_input == 'Y':
            iris = load_iris(as_frame=True)
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
        elif user_input == 'n' or user_input == 'N':
            pass
        else:
            print(f"Wrong input entered: {user_input}")
    print("Proceeding with various data visualisation tasks on the Iris dataset")

    # The first visualisation task is to create a scatter plot.
    print("First visualisation task. Plotting a scatter plot.")
    # Call the function to create a scatter plot
    scatter_plot(df)

    # The second visualisation task is to create a histogram.
    print("Second visualisation task. Plotting a histogram.")
    # Call the function to create a histogram
    histogram(df)

if __name__ == "__main__":
    main()