import pandas as pd 
import yfinance as yf 

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    
    Parameters:
    ticker (str): Stock ticker symbol.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: DataFrame containing stock data with Date as index.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)
    return stock_data

def cleaning_data(dataframe):
    """
    Paratmeters:
    dataframe(pd.DataFrame): Data

    Returns:

    """
    dataframe.drop_na()

    return dataframe
   

def save_to_csv(dataframe, filename):
    """
    Save DataFrame to a CSV file.

    Parameters:
    dataframe (pd.DataFrame): DataFrame to save.
    filename (str): Name of the output CSV file.
    
    Returns:
    pd.DataFrame: as a CSV File
    """
    dataframe.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

