"""
src/data_ingestion.py

Purpose: 
This file was created to 
"""

import pandas as pd 
import yfinance as yf 

def fetch_stock_data(ticker, start_date, end_date)-> pd.DataFrame:
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
    -----------
    dataframe (pd.DataFrame): DataFrame to clean.

    Returns:
    -----------
    pd.DataFrame: Cleaned DataFrame.
    """
    # Fill NaN values with forward fill method
    if dataframe.isnull().values.any():
        print("Cleaning data: Filling NaN values with forward fill method.")
        dataframe.fillna(method='ffill', inplace=True)
    else:
        print("No NaN values found in the DataFrame.")
    # Reset index after filling NaN values
    dataframe.reset_index(drop=True, inplace=True)
    
    # Drop rows with any NaN values
    if dataframe.isnull().values.any():
        print("Cleaning data: Dropping rows with NaN values.")
        dataframe = dataframe.dropna()
    else:
        print("No NaN values found in the DataFrame.")
    # Reset index after dropping rows
    dataframe.reset_index(drop=True, inplace=True)
    # Ensure the DataFrame is not empty after cleaning
    if dataframe.empty:
        raise ValueError("DataFrame is empty after cleaning. Please check the input data.")
    # Drop rows with NaN values in the 'Close' column
    if 'Close' in dataframe.columns:
        if dataframe['Close'].isnull().any():
            print("Cleaning data: Dropping rows with NaN values in 'Close' column.")
            dataframe = dataframe.dropna(subset=['Close'])
        else:
            print("No NaN values found in 'Close' column.")
    else:
        print("'Close' column not found in the DataFrame. Skipping NaN check for 'Close' column.")
    # Drop rows with NaN values in the 'Volume' column
    if 'Volume' in dataframe.columns:
        if dataframe['Volume'].isnull().any():
            print("Cleaning data: Dropping rows with NaN values in 'Volume' column.")
            dataframe = dataframe.dropna(subset=['Volume'])
        else:
            print("No NaN values found in 'Volume' column.")
    else:
        print("'Volume' column not found in the DataFrame. Skipping NaN check for 'Volume' column.")
    # Reset index after dropping rows
    dataframe.reset_index(drop=True, inplace=True)
    # Ensure the DataFrame is not empty after cleaning
    if dataframe.empty:
        raise ValueError("DataFrame is empty after cleaning. Please check the input data.")
    # Convert 'Date' column to datetime format if it exists
    if 'Date' in dataframe.columns:
        dataframe['Date'] = pd.to_datetime(dataframe['Date'], errors='coerce')
        if dataframe['Date'].isnull().any():
            print("Cleaning data: Dropping rows with NaT values in 'Date' column.")
            dataframe = dataframe.dropna(subset=['Date'])
        else:
            print("All dates are valid.")
    else:
        print("'Date' column not found in the DataFrame. Skipping date conversion.")
    # Ensure the DataFrame is not empty after cleaning
    if dataframe.empty:
        raise ValueError("DataFrame is empty after cleaning. Please check the input data.")
    # Reset index after dropping rows
    dataframe.reset_index(drop=True, inplace=True)
    # Ensure the DataFrame is not empty after cleaning
    if dataframe.empty:
        raise ValueError("DataFrame is empty after cleaning. Please check the input data.")
    # Return the cleaned DataFrame
    print("Data cleaning complete.")
    return dataframe
   

def save_to_csv(dataframe, filename, directory='data'):
    """
    Save DataFrame to a CSV file.

    Parameters:
    dataframe (pd.DataFrame): DataFrame to save.
    filename (str): Name of the output CSV file.
    
    Returns:
    pd.DataFrame: as a CSV File
    """
    dataframe.to_csv(f"{directory}/{filename}", index=False)
    print(f"Data saved to {directory}/{filename}")

