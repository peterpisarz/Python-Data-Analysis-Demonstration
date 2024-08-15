# Dataset created via ChatGPT prompts
# This data simulates the output of an automobile engine for a given time period

import pandas as pd
import numpy as np

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