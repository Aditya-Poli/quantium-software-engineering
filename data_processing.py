import os
import pandas as pd

def clean_data(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input DataFrame by filling missing values with a space character and selecting only rows related to "pink morsel" products.

    Parameters:
        data_frame (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    data_frame.fillna(method='ffill', inplace=True)
    data_frame = data_frame.loc[data_frame["product"] == "pink morsel"]
    return data_frame

def combine_dataframes_from_dir(dir: str) -> pd.DataFrame:
    """
    This function takes a directory path as input and returns a combined
    pandas DataFrame object.

    Parameters:
        dir (str): The path to the directory containing the CSV files to be combined.

    Returns:
        pd.DataFrame: A pandas DataFrame object containing the combined data from all
        the CSV files in the directory.

    Example:
    ```
    import pandas as pd

    df = combine_dataframes_from_dir('path/to/directory')
    print(df.head())
    ```
    """
    data_frames = [pd.read_csv(os.path.join(dir, file_name)) for file_name in os.listdir(dir)]
    return pd.concat(data_frames)

def add_sales(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Parameters:
        data_frame (pd.DataFrame): The input DataFrame containing product information.

    Returns:
        pd.DataFrame: The modified DataFrame with a new column called "sales" that contains
                      the total sales for each product based on the quantity and price 
                      information.
    """
    data_frame["price"] = data_frame["price"].apply(lambda price: float(price[1:]))
    data_frame["sales"] = data_frame["quantity"] * data_frame["price"]
    data_frame.drop(["quantity", "price", "product"], axis=1, inplace=True)
    return data_frame

def write_csv(data_frame: pd.DataFrame, output_file_path: str) -> None:
    data_frame.to_csv(output_file_path, columns=["sales", "date", "region"], index=False)

if __name__ == "__main__":
    DATA_DIRECTORY = "./data"
    OUTPUT_FILE_PATH = "./formatted_data.csv"

    # read all csv's from the directory and 
    # combine all of them to a single data frame
    final_df = combine_dataframes_from_dir(DATA_DIRECTORY)

    # select only rows with Pink Morsels and clean it
    # fill the na values with the previous value
    final_df = clean_data(final_df)

    # add sales column by multiplying quantity and price column
    # remove the unwanted columns [quantity, price, product]
    final_df = add_sales(final_df)

    # write the final data to the csv
    write_csv(final_df, OUTPUT_FILE_PATH)