# Load a data for Auckland and Christchurch and compare the temperature between two cities in a year monthly basis

import pandas as pd
import matplotlib.pyplot as plt

class tempCompare:
  #Constructor to initialize empty Dataframes ready to store the data from csv files
  def __init__(self):
    self.akl = None
    self.chch = None

  # Load the CSV files
  def loadFile(self):
    self.akl = pd.read_csv('./week4/afterclass_activities/Auckland_records.csv')
    self.chch = pd.read_csv('./week4/afterclass_activities/Christchurch_records.csv')

  # Show the plot of temperature comparison of year 2024
  def showPlot(self):
    # Filter data for 2024
    akl_2024 = self.akl[self.akl['YEAR'] == 2024].iloc[0]
    chch_2024 = self.chch[self.chch['YEAR'] == 2024].iloc[0]

    # Get months for plotting
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

    # Extract temperature values for 2024
    akl_temps = akl_2024[months].values
    chch_temps = chch_2024[months].values

    # Create a comparison plot
    plt.figure(figsize=(10, 5))
    plt.plot(months, akl_temps, marker='o', label='Auckland', color='blue')
    plt.plot(months, chch_temps, marker='o', label='Christchurch', color='red')

    # Custom the plot and show
    plt.title('Monthly Temperature Comparison (2024)')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)', )
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
  tc = tempCompare()
  tc.loadFile()
  tc.showPlot()

if __name__ == "__main__":
  main()