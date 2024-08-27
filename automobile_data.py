# Dataset created via ChatGPT prompts
# This data simulates the output of an automobile engine for a given time period

import pandas as pd
import numpy as np
import os
import json

def generate_engine_data(engine_run):
    # Generate time data
    time_data = np.arange(0, 50, 1)  # Relative time from 0 to 49 seconds

    # Manually specify RPM values to simulate acceleration
    rpm_data = [800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500,
                1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500,
                2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500,
                3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500,
                4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500]  # RPM increasing over time

    # Generate realistic data for other automobile parameters based on RPM
    battery_voltage_data = np.clip(13 + (np.array(rpm_data) - 800) / 5000 + np.random.normal(0, 0.2, 50), 12.0, 14.8)
    fuel_consumption_lph = np.clip(0.5 + (np.array(rpm_data) - 800) / 4000 + np.random.normal(0, 0.1, 50), 0.2, 2.0)  # in L/h
    fuel_consumption_gpm = fuel_consumption_lph * 0.0044028675  # Convert from L/h to gallons per minute (GPM)
    engine_temperature_c = np.clip(70 + (np.array(rpm_data) - 800) / 50 + np.random.normal(0, 2, 50), 70, 110)  # in Celsius
    engine_temperature_f = engine_temperature_c * 9/5 + 32  # Convert from Celsius to Fahrenheit
    throttle_position_data = np.clip((np.array(rpm_data) - 800) / 50 + np.random.normal(0, 5, 50), 0, 100)
    oil_pressure_data = np.clip(20 + (np.array(rpm_data) - 800) / 50 + np.random.normal(0, 5, 50), 20, 80)

    # Introduce a few outliers
    outliers = [5, 15, 35]
    for outlier in outliers:
        rpm_data[outlier] = rpm_data[outlier] + np.random.randint(-500, 500)
        battery_voltage_data[outlier] = battery_voltage_data[outlier] + np.random.uniform(-1.5, 1.5)
        fuel_consumption_gpm[outlier] = fuel_consumption_gpm[outlier] + np.random.uniform(-0.001, 0.001)
        engine_temperature_f[outlier] = engine_temperature_f[outlier] + np.random.randint(-10, 10)
        throttle_position_data[outlier] = throttle_position_data[outlier] + np.random.uniform(-20, 20)
        oil_pressure_data[outlier] = oil_pressure_data[outlier] + np.random.uniform(-10, 10)

    # Create a DataFrame
    engine_df = pd.DataFrame({
        'Time (s)': time_data,
        'RPM': rpm_data,
        'Battery Voltage (V)': battery_voltage_data.round(2),
        'Fuel Consumption (GPM)': fuel_consumption_gpm.round(4),
        'Engine Temperature (°F)': engine_temperature_f.astype(int),
        'Throttle Position (%)': throttle_position_data.round(2),
        'Oil Pressure (psi)': oil_pressure_data.round(2)
    })

    # Convert the DataFrame to a dictionary
    engine_data_dict = engine_df.to_dict(orient='list')

    return engine_df, {f"Engine Run": engine_run, "Data": engine_data_dict}


def get_run_number(directory):
    existing_files = [f for f in os.listdir(directory) if f.startswith('engine_run_') and f.endswith('.json')]
    if existing_files:
        run_numbers = [int(f.split('_')[2].split('.')[0]) for f in existing_files]
        next_run_number = max(run_numbers) + 1
    else:
        next_run_number = 1
    return next_run_number

def create_run():
    # Directory for storing engine run data
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(current_directory, 'engine_runs')
    os.makedirs(directory, exist_ok=True)

    # Get the next run number
    engine_run_number = get_run_number(directory)

    # Generate data for the current engine run
    engine_df, engine_run_data = generate_engine_data(engine_run_number)

    # Define the file name
    file_name = f'engine_run_{engine_run_number}.json'
    file_path = os.path.join(directory, file_name)

    # Save the data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(engine_run_data, f, indent=4)

    print(f"Engine run {engine_run_number} data saved to {file_path}")

    return engine_df