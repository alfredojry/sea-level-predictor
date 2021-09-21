import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    df_x1 = pd.Series([int(i) for i in range(1880, 2050)])
    plt.plot(df_x1, intercept1 + slope1 * df_x1, 'r', label='fitted line')


    # Create second line of best fit
    df_c21 =df[df['Year'] >= 2000] 
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_c21['Year'], df_c21['CSIRO Adjusted Sea Level'])
    df_x2 = pd.Series([int(i) for i in range(2000, 2050)])
    plt.plot(df_x2, intercept2+ slope2 * df_x2, 'r', label='fitted line', color='blue')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
