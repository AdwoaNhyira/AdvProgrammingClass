pip install yfinance
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
import yfinance as yf
sb.set_theme() # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = None
        self.start = start
        self.end = end
        self.df = self.get_data()


    def get_data(self):
        self.symbol = input("Provide a stock symbol: ")
        df = yf.download(self.symbol, DEFAULT_START, DEFAULT_END)
        self.calc_returns(df)
        return df
        #pass

    
    def calc_returns(self, df):
        df['changes'] = df['Close'].pct_change()
        df['instant'] = np.log(df['Close']).diff()
        #return df

        """method that adds change and return columns to data"""
        #pass

    
    def plot_return_dist(self):
        plt.hist(self.df['instant'], bins=50, density = True, color='g', edgecolor='w')
        plt.xlabel('Instant Returns')
        plt.ylabel('Frequency')
        plt.title('Histogram of Instant Returns')
        plt.grid(axis='y',alpha=.3)
        plt.show();
        """method that plots instantaneous returns as histogram"""
        #pass


    def plot_performance(self):
        plt.plot(self.df['changes'], label=self.symbol)
        plt.title("Percent Change")
        plt.grid(axis="y",alpha=.5)
        plt.legend(loc=1)
        plt.show();
        """method that plots stock object performance as percent """
        #pass



def main():
    # uncomment (remove pass) code below to test
    test = Stock() # optionally test custom data range
    print(test.df)
    test.plot_performance()
    test.plot_return_dist()
    #pass

if __name__ == '__main__':
    main() 