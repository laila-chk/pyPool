import matplotlib.pyplot as plt
from load_csv import load

"""
 this program loads the file life_expectancy_years.csv,
 and displays the information of Morocco's life expectancy based on it.
"""
if __name__ == "__main__":
    data = load("life_expectancy_years.csv");
    Morocco_data = data[data['country'] == 'Morocco'].set_index('country').T
    Morocco_data.plot( title="Morocco Life expectancy projection", legend = False)
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.show()
