import numpy as np

# temperatures of a whole week
temps = np.array([18.5,19,20,25.0,2,30,13.9])

# 1. print average temperatures
avg = np.mean(temps)
print(f"Average temperature:{avg:.2f}\u00B0C")

# 2. find the highest and lowest temperature
max = np.max(temps)
min = np.min(temps)
print(f"Max temperature:{max}\u00B0C")
print(f"Min temperature:{min}\u00B0C")

# 3. convert celsius to Fahrenheit
Fah_temps = temps*9/5
print(f"The Fahrenheit are:{Fah_temps}")

# 4. Identify the days where the temperatures was above 20℃
index = np.where(temps >= 20)[0]+1
print(f"The days (by index) where the temperature was above 20\u00B0C:{index}")