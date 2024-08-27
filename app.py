import pandas as pd
import os
import json
from main import plot

def retrieve_run_data(run_number, directory):

    file_name = f'engine_run_{run_number}.json'
    file_path = os.path.join(directory, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No data found for engine run number {run_number}")

    with open(file_path, 'r') as f:
        engine_run_data = json.load(f)

    engine_df = pd.DataFrame(engine_run_data["Data"])

    return engine_df

if __name__ == '__main__':
    directory = r'C:\Users\peter\PycharmProjects\Python-Data\engine_runs'
    run_num = 1
    df = retrieve_run_data(run_num, directory)
    pd.set_option('display.max_columns', None)
    print(f'Here is the data frame for Engine Run {run_num}:')
    print(df)

    plot(df, 'RPM')