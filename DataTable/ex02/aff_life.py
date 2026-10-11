import matplotlib.pyplot as plt
from load_csv import load

"""
 this program loads the file life_expectancy_years.csv,
 and displays the information of Morocco's life expectancy vs France.
"""
if __name__ == "__main__":
    data = load("life_expectancy_years.csv");
    countries = ['Morocco', 'France']
    countries_data = data[data['country'].isin(countries)].set_index('country').T
    countries_data.plot( title="Morocco Life expectancy projection")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.show()
