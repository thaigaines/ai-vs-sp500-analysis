import matplotlib.pyplot as plt
import pandas as pd

def clean_data(df):
    """
    Stock Price Dataframe cleaner

    Parameters:
    - df: pandas Dataframe with stock prices

    Returns:
    - Cleaned Dataframe with values filled or removed entirely.

    """

    # Forward fill missing values
    df = df.ffill()

    # Drop row if all are missing
    df = df.dropna(how="all")

    return df

def init_plot(title, xlabel, ylabel):
    """
    Pyplot Init Shortcut

    Parameters:
    - title: plot title
    - xlabel: x-axis label
    - ylabel: y-axis label

    Returns:
    - Initialized plot
    
    """
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()