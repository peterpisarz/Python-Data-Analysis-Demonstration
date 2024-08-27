# Ficticious Data to show Data Analysis methods using pandas and matplotlib
# Data was generated by ChatGPT prompt
# Functions and code written by Peter Pisarz

from automobile_data import create_run
import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Function to plot data with respect to time
def plot(df, param):
    plt.plot(df['Time (s)'], df[f'{param}'], label=f'Engine Data: Time v {param}')
    plt.xlabel('Time (s)')

    units = re.search(r'\((.*?)\)', param)
    units = units.group(1) if units else 'RPM'
    plt.ylabel(f'{units}')
    plt.legend()

    if 'RPM' in param:
        plt.axhline(y=6000, color='red', linestyle='--', label='Redline at 6000rpm')

    plt.show()

# Function to find corresponding data values to a specific rpm
def getValueAtRPM(rpm, value):
    try:
        result = df.loc[df['RPM'] == rpm, value].values
        return result
    except ValueError as e:
        print(f'Result for {rpm} RPM')
        return None

def getRPMInRange(value, low, high):
    rpm_values = df.loc[(df[value] >= low) & (df[value] < high), 'RPM']
    rpm_list = rpm_values.tolist()
    return rpm_list

if __name__ == '__main__':

    df = create_run()

    #Display options to view df
    pd.set_option('display.width', 0)
    pd.set_option('display.max_columns', None)
    print('Here is the original dataframe:')
    print(df, '\n')

    # Fuel consumption at 2000 RPM
    loc_rpm = 2000
    param1 = 'Fuel Consumption (GPM)'
    result = getValueAtRPM(loc_rpm, param1)
    if result: print(f'The {param1} at {loc_rpm}rpm is {result[0]}.\n')

    # Get the oil pressure within a certain range
    low = 30.00
    high = 45.00
    param2 = 'Oil Pressure (psi)'
    result2 = getRPMInRange(param2, low, high)
    print(f'{param2} reads between {low} and {high} for the following RPM:\n', result2, '\n')

    # Get the average Engine Temperature
    avg_engine_temp = df['Engine Temperature (°F)'].mean()
    print(f"The average Engine Temperature is {avg_engine_temp} °F\n")

    # Get min and max values of Battery Voltage and their corresponding RPMs
    min_v, max_v = df['Battery Voltage (V)'].min(), df['Battery Voltage (V)'].max()
    min_v_rpm, max_v_rpm = df.loc[df['Battery Voltage (V)'] == min_v, 'RPM'].values, \
                           df.loc[df['Battery Voltage (V)'] == max_v, 'RPM'].values
    print(f'The minimum voltage is {min_v}(V) at {min_v_rpm[0]}RPM, and'
          f'the maximum voltage is {max_v}(V) at {max_v_rpm[0]}RPM.\n')

    # Create a new df with rows containing Throttle position greater than 84%
    rows = []
    for index, row in df.iterrows():
        if row['Throttle Position (%)'] > 85.00:
            rows.append(row)
    df_throttle = pd.DataFrame(rows, columns=df.columns)
    print('Here is the dataframe displaying rows with Throttle > 85%:')
    print(df_throttle, '\n')

    # Plot RPMs over Time
    plot(df, 'RPM')

    #Preprocessing data for KMeans
    plt.scatter(df['RPM'], df['Fuel Consumption (GPM)'])
    plt.xlabel('RPM')
    plt.ylabel('Fuel Consumption vs RPM')
    plt.title('')
    plt.show()

    X = df[['RPM', 'Fuel Consumption (GPM)']].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=2, random_state=42)
    df['Clusters'] = kmeans.fit_predict(X_scaled)

    centers = kmeans.cluster_centers_
    centers_original = scaler.inverse_transform(centers)

    plt.scatter(df['RPM'], df['Fuel Consumption (GPM)'], c=df['Clusters'], cmap='viridis')
    plt.scatter(centers_original[:, 0], centers_original[:, 1], c='red', s=200, alpha=0.75)
    plt.xlabel('RPM')
    plt.ylabel('Fuel Consumption vs RPM')
    plt.title('Clusters')
    plt.show()

    print("Cluster centers (scaled data):")
    print(centers)
    # print("\nCluster assignment for each input:")
    # print(df[['Time (s)', 'Clusters']])