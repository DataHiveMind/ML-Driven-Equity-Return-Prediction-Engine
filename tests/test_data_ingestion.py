
import pytest
import pandas as pd
from src.data_ingestion import fetch_stock_data, save_to_csv



@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]}), pd.DataFrame({'A': [1, 2], 'B': [4, 6]})),
        (pd.DataFrame({'A': [None, None], 'B': [None, None]}), pd.DataFrame()),
        (pd.DataFrame({'A': [1, 2], 'B': [3, 4]}), pd.DataFrame({'A': [1, 2], 'B': [3, 4]})),
    ]
)

def test_fetch_stock_data():
    ticker = "AAPL"
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    assert isinstance(stock_data, pd.DataFrame), "Fetched data is not a DataFrame."
    assert not stock_data.empty, "Fetched data is empty."
    assert 'Date' in stock_data.columns, "Date column is missing in the fetched data."
    assert stock_data['Date'].dtype == 'datetime64[ns]', "Date column is not in datetime format."
    assert stock_data.index.equals(stock_data['Date']), "Index does not match Date column."

def test_save_to_csv(tmp_path):
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    filename = tmp_path / "test_data.csv"
    save_to_csv(df, filename)
    
    assert filename.exists(), "CSV file was not created."
    saved_df = pd.read_csv(filename)
    pd.testing.assert_frame_equal(saved_df, df, check_dtype=True)

def test_cleaning_data(input_data, expected_output):
    from src.data_ingestion import cleaning_data
    cleaned_data = cleaning_data(input_data)
    pd.testing.assert_frame_equal(cleaned_data, expected_output)

    # Check if the cleaned data has the same number of columns as the input data
    assert cleaned_data.shape[1] == input_data.shape[1], "Data cleaning altered the number of columns unexpectedly."
    assert cleaned_data.shape[0] <= input_data.shape[0], "Data cleaning did not reduce the number of rows as expected."
    assert cleaned_data.shape[0] == expected_output.shape[0], "Data cleaning did not produce the expected number of rows."
    assert cleaned_data.shape[1] == expected_output.shape[1], "Data cleaning did not produce the expected number of columns."
    assert cleaned_data.columns.equals(expected_output.columns), "Data cleaning did not preserve the expected column names."
    assert cleaned_data.index.equals(expected_output.index), "Data cleaning did not preserve the expected index."
    
    # Check if the shape of the cleaned data matches the expected output
    assert cleaned_data.empty == expected_output.empty
    assert cleaned_data.shape == expected_output.shape, "Data cleaning did not produce the expected shape."
    assert cleaned_data.dtypes.equals(expected_output.dtypes), "Data cleaning did not preserve the expected data types."
    
    # Check for NaN values 
    assert not cleaned_data.isnull().values.any(), "Data cleaning did not remove all NaN values."
    assert cleaned_data.equals(expected_output), "Data cleaning did not produce the expected output."
    assert cleaned_data.notnull().all().all(), "Data cleaning did not ensure all values are non-null."
    assert cleaned_data.isna().sum().sum() == 0, "Data cleaning did not remove all NaN values."
    assert cleaned_data.isnull().sum().sum() == 0, "Data cleaning did not remove all NaN values."
    assert cleaned_data.isna().sum().sum() == 0, "Data cleaning did not remove all NaN values."
    assert cleaned_data.isnull().sum().sum() == 0, "Data cleaning did not remove all NaN values."
    