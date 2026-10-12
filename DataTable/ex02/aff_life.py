import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load

"""
 this program loads the file life_expectancy_years.csv,
 and displays the information of Morocco's life expectancy vs France.
"""
if __name__ == "__main__":
    data = load("population.csv");
    countries = ['Morocco', 'Belgium']
    countries_data = data[data['country'].isin(countries)].set_index('country').T.loc[:'2050']
    countries_data = countries_data.replace({'M': 'e6', 'K': 'e3', 'B': 'e9'}, regex=True).astype(float)
    ax = countries_data.plot(title="population projection")
    ax.yaxis.set_major_formatter(ticker.EngFormatter())
    plt.ylabel("population")
    plt.xlabel("Year")
    plt.show()
